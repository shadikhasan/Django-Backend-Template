from django.http import JsonResponse
from django.db import connection
from django.conf import settings


def _environment_label() -> str:
    module_name = (settings.SETTINGS_MODULE or "").lower()
    if "prod" in module_name:
        return "Production"
    if "test" in module_name:
        return "Testing"
    if "dev" in module_name:
        return "Development"
    return "Development" if settings.DEBUG else "Production"


def health_check(request):
    try:
        connection.ensure_connection()
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {str(e)}"

    overall_status = "ok" if db_status == "ok" else "error"
    http_status = 200 if overall_status == "ok" else 500

    return JsonResponse(
        {
            "status": overall_status,
            "database": db_status,
            "environment": _environment_label(),
            "version": getattr(settings, "APP_VERSION", "1.0.0"),
        },
        status=http_status
    )