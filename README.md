# Shopify–Odoo Integration

Proyecto de integración backend para sincronizar información entre Shopify y Odoo, orientado a escenarios de migración e interoperabilidad entre plataformas de comercio electrónico y ERP.

## Objetivos

- Integrar Shopify mediante su GraphQL Admin API.
- Integrar Odoo 19 mediante su API externa JSON-2.
- Gestionar credenciales mediante variables de entorno.
- Implementar validaciones, pruebas automatizadas y controles de calidad.
- Preparar una base extensible para sincronización de productos, variantes, clientes, pedidos y stock.

## Tecnologías

- Python 3.13
- HTTPX
- Pydantic y Pydantic Settings
- Odoo 19
- PostgreSQL 15
- Docker Compose
- Pytest, Respx y Ruff

## Estado actual

- [x] Entorno Python y dependencias configurados.
- [x] Configuración tipada mediante variables de entorno.
- [x] Cliente inicial para Odoo JSON-2.
- [x] Consulta de contactos de Odoo.
- [x] Pruebas automatizadas del cliente y la configuración.
- [ ] Cliente Shopify GraphQL Admin API.
- [ ] Integración de productos y variantes.
- [ ] Sincronización de pedidos y stock.
- [ ] Automatización CI con GitHub Actions.

## Requisitos previos

- Python 3.13
- `uv`
- Docker Desktop con Docker Compose
- Una instancia local de Odoo 19

## Configuración local

1. Cloná el repositorio.
2. Instalá las dependencias:

   ```bash
   uv sync --dev
   ```

3. Copiá la plantilla de variables de entorno:

   ```bash
   cp .env.example .env
   ```

4. Completá `.env` con las credenciales de tu entorno local. No compartas ni publiques este archivo.
5. Iniciá Odoo y PostgreSQL:

   ```bash
   docker compose up -d
   ```

## Ejecutar las pruebas

```bash
uv run ruff check .
uv run pytest
```

## Probar la conexión con Odoo

Con Odoo en funcionamiento y las variables correspondientes configuradas en `.env`:

```bash
uv run python scripts/test_odoo_connection.py
```

El script consulta la versión del servidor y lee una cantidad limitada de contactos. No está diseñado para modificar datos.

## Seguridad

- `.env` contiene credenciales locales y no debe subirse a Git.
- `.env.example` debe incluir únicamente nombres de variables y valores de ejemplo no sensibles.
- Las claves API deben tener los permisos y la duración adecuados para el entorno.
- Las credenciales incluidas en pruebas deben ser ficticias.

## Licencia

Proyecto educativo y de portfolio. La licencia se definirá antes de su publicación.
