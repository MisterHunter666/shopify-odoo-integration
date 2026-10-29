
from shopify_odoo_integration.config import Settings
from shopify_odoo_integration.odoo_client import OdooClient


def main() -> None:
    settings = Settings()
    client = OdooClient(settings)

    version = client.get_version()
    print("Conexión con el servidor Odoo: correcta")
    print(f"Versión del servidor: {version}")

    contacts = client.search_contacts()
    print(f"Contactos encontrados: {len(contacts)}")

    for contact in contacts:
        print(f"- ID: {contact['id']} | Nombre: {contact['name']}")


if __name__ == "__main__":
    main()
