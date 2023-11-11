kofiguracja vscode 
plugin ->rest client
gdy zainstalowany mozna zrobić plik test.http 
i w nim wpisać GET adres url
to będziemy mieli podgląd tego co się tam dzieje 



## Utworzenie i Projektu Django
### uruchominie wirtualnego środowiska
python -m venv path/venv

### aktywacja środowiska w terminalu
z katalogu path\venv\Scripts\activate
uruchamiam activate

```np. projekt\venv\Scripts\activate```

### tworze projekt django

django-admin startproject nazwa_projektu .

### startowanie servera django

python manage.py runserver


## Modyfikacja

### Przygotowanie aplikacji która służy do jakiegoś konkretnego celu

będąc w katalogu projektu uruchamiamy w terminalu:
```
    python manage.py startapp nazwa_aplikacji
```

widoki powinny być definiowane we views i zaimportowane do `````\nazwa_projektu\urls`````

Przykład wywołania widoku w pliku urls:
``` python
    from nazwa_aplikacji import views
    ...
    path('hello/<name>/', views.return_name),
```

przykład definicji widoku w katalogu aplikacji:


```python
def home(request, name): # request to http request - domyslny parametr funkcji
    return HttpResponse("hello world")

def return_name(request, name):
    return HttpResponse(f"hello {name}")


```