from django.http.response import JsonResponse

def index():
    return JsonResponse({"message":"Welcome to the weather app."})