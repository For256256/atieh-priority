from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def health(request):
    return JsonResponse(
        {
            "name": "SAMANAK",
            "status": "ok",
            "version": "1.0.0",
        }
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/health/", health),
]
