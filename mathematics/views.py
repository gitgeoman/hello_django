from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from mathematics.services import AlgebraService
from django.template.loader import render_to_string


# pełne
# def hello(request):  # request to http request - domyslny parametr funkcji
#     rendered = render_to_string("mathematics/calculations.html", {'text': f'hello'})
#     return HttpResponse(rendered)

# na skróty przy zastosowaoniu reneder
def hello(request):  # request to http request - domyslny parametr funkcji
    return render(
        request=request,
        template_name="mathematics/calculations.html",
        context={'text': f'hello'})


# pełne
# def return_name(request, name: str = ''):
#     rendered = render_to_string("mathematics/calculations.html", {'text': f'hello {name}'})
#     return HttpResponse(f"Hello {name}")

# na skróty przy zastososaniu rendera
def return_name(request, name: str = ''):
    rendered = render_to_string("mathematics/calculations.html", {'text': f'hello {name}'})
    return render(
        request=request,
        template_name="mathematics/calculations.html",
        context={
            'text': f'hello {name}',
            'text2': f'this is text2 ',
            'lista': [10,2, 'a', 'b'],
            'tupla': ('x', 'y', 100),
            'slownik': {'klucz':'wartosc'},
            'zbior': {
                "aaa":1,
                "bbb":2,
                "ccc":3
            },
        }
    )


def calculator(request: HttpRequest, operation: str, a: int, b: int) -> HttpResponse:
    try:
        result = AlgebraService.calculate(operation, a, b)
    except ValueError as e:
        return HttpResponse(f'{e}')
    except KeyError:
        return HttpResponse(f'Nie poprawna operacja')
    return HttpResponse(f'{result}')

