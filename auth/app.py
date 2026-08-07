"""Backend de acceso a /docs/ para la landing de Gestiolibra -- config sobre
libra_web_kit.docs_auth (extraído 2026-07-26, ver
wiki/analyses/auditoria-duplicacion-familia-libra.md)."""
from libra_web_kit.docs_auth import build_docs_login_app, DocsLoginTheme

app = build_docs_login_app(
    product_name="Gestiolibra",
    apex_domain_default="gestiolibra.com.ar",
    secret_key_env="DOCS_SESSION_SECRET",
    secret_key_default="gestiolibra-docs-secret-change-me",
    verify_path="/auth/verify",
    slug_placeholder="tu-negocio",
    theme=DocsLoginTheme(accent="#7c3aed", accent_hover="#6d28d9"),
)
