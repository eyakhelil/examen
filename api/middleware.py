from django.http import JsonResponse
from django.conf import settings

class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.api_key = getattr(settings, "API_KEY", None)

    def __call__(self, request):
        
        if request.path.startswith("/graphql"):
            key = request.headers.get("X-API-KEY")
            if key != self.api_key:
                return JsonResponse({"error": "Unauthorized"}, status=401)
            
        return self.get_response(request)
