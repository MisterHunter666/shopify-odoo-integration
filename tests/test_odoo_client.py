
import httpx
import respx

from shopify_odoo_integration.config import Settings
from shopify_odoo_integration.odoo_client import OdooClient


def build_settings() -> Settings:
    return Settings(
        SHOPIFY_SHOP="demo.myshopify.com",
        SHOPIFY_CLIENT_ID="test-id",
        SHOPIFY_CLIENT_SECRET="test-secret",
        ODOO_URL="http://localhost:8069",
        ODOO_DB="odoo19",
        ODOO_API_KEY="test-api-key",
        _env_file=None,
    )


@respx.mock
def test_get_version_returns_server_version() -> None:
    respx.get("http://localhost:8069/web/version").mock(
        return_value=httpx.Response(
            200,
            json={"version": "19.0-test"},
        )
    )

    client = OdooClient(build_settings())

    result = client.get_version()

    assert result["version"] == "19.0-test"


@respx.mock
def test_search_contacts_sends_authenticated_request() -> None:
    route = respx.post(
        "http://localhost:8069/json/2/res.partner/search_read"
    ).mock(
        return_value=httpx.Response(
            200,
            json=[{"id": 1, "name": "My Company", "email": "info@example.com"}],
        )
    )

    client = OdooClient(build_settings())

    result = client.search_contacts()

    assert route.called
    assert route.calls.last.request.headers["Authorization"] == "bearer test-api-key"
    assert route.calls.last.request.headers["X-Odoo-Database"] == "odoo19"
    assert result[0]["name"] == "My Company"
