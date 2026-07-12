from django.http import JsonResponse
from django.views import View


class HealthView(View):

    def get(self, request):

        return JsonResponse(
            {
                "application": "SAMANAK Enterprise",
                "status": "healthy",
                "database": "unknown",
                "redis": "unknown",
                "version": "1.0.0",
            }
        )
