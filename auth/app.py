"""Backend de acceso a /docs/ para la landing de LibraDesk — config sobre
`libra_web_kit.docs_auth`, misma mecánica que las otras cinco landings (ver
wiki/entities/libra-web-kit.md).

El visitante entra con las credenciales de **su instancia**: el login valida
contra `POST /auth/verify` del producto, que es un chequeo stateless con
secreto compartido y no crea sesión en la instancia. Por eso el formulario
pide primero el slug del cliente.
"""
from libra_web_kit.docs_auth import build_docs_login_app, DocsLoginTheme

app = build_docs_login_app(
    product_name="LibraDesk",
    apex_domain_default="libradesk.com.ar",
    secret_key_env="DOCS_SESSION_SECRET",
    secret_key_default="libradesk-docs-secret-change-me",
    verify_path="/auth/verify",
    slug_placeholder="tu-empresa",
    # Índigo, el acento de la landing de LibraDesk.
    theme=DocsLoginTheme(accent="#4f46e5", accent_hover="#4338ca"),
)
