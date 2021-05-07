from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
from django.template import loader
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt

method_decorator(csrf_protect)


@csrf_exempt
@require_POST
def create(request):
    return JsonResponse({'message': "Object created"})


@csrf_exempt
@require_GET
def show_books(request):
    books = [("Властелин колец", "Джон Р. Р. Толкин"), ("Гордость и предубеждение", "Джейн Остин"),
             ("Тёмные начала", "Филип Пулман")]
    return JsonResponse({"list": books})


@csrf_exempt
@require_GET
def details(request):
    book = {"Жанр": "Фэнтези", "Автор": "Дж. Р. Р. Толкин", "Язык оригинала": "английский",
                "Дата первой публикации": "29 июля и 11 ноября 1954", "Издательство": "George Allen & Unwin"}
    return JsonResponse(book)


@csrf_exempt
@require_GET
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
