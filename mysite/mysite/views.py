from django.http import HttpResponse, JsonResponse


def home_view(request):
    # return HttpResponse("<h1>Welcome To Home Page</h1>")
    return JsonResponse({"status": "successful", "page": "home"})
