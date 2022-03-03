from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.GET:
        response = request.GET
#        return HttpResponse(f"<h1>Hello {response['name']}! {response['message']}</h1>")
        data = {"name": response['name'], "message": response['message']}
        return render(request, 'base.html', context=data)
    else:
        return HttpResponse("Используйте правильный GET запрос")