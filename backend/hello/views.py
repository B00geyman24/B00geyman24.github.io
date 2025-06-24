from django.http import HttpResponse


def hello_view(request):
    name = request.GET.get('name', 'Guest')
    message = request.GET.get('message', 'Hello')
    return HttpResponse(f'Hello {name}! {message}!')
