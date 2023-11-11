from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from mathematics.services import AlgebraService


def home(request):  # request to http request - domyslny parametr funkcji
    return HttpResponse("hello world")


def return_name(request, name):
    return HttpResponse(f"hello {name}")


def calculator(request: HttpRequest, operation: str, a: int, b: int) -> HttpResponse:
    try:
        result = AlgebraService.calculate(operation, a, b)
    except ValueError as e:
        return HttpResponse(f'{e}')
    except KeyError:
        return HttpResponse(f'Nie poprawna operacja')
    return HttpResponse(f'{result}')


