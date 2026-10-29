
import httpx

from shopify_odoo_integration.config import Settings


class OdooClient:
    def __init__(self, settings: Settings) -> None:
        self.base_url = settings.odoo_url.rstrip("/")
        self.database = settings.odoo_db

        self.headers = {
            "Authorization": (
                f"bearer {settings.odoo_api_key.get_secret_value()}"
            ),
            "X-Odoo-Database": self.database,
            "Content-Type": "application/json",
            "User-Agent": "shopify-odoo-integration/0.1.0",
        }

    def get_version(self) -> dict:
        response = httpx.get(
            f"{self.base_url}/web/version",
            timeout=10.0,
        )
        response.raise_for_status()
        return response.json()

    def search_contacts(self, limit: int = 5) -> list:
        response = httpx.post(
            f"{self.base_url}/json/2/res.partner/search_read",
            headers=self.headers,
            json={
                "domain": [],
                "fields": ["id", "name", "email"],
                "limit": limit,
            },
            timeout=15.0,
        )
        response.raise_for_status()
        return response.json()
