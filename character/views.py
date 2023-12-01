from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def main_page(request):
    return HttpResponse('<h1 align="center">Main Page</h1>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1 align="center">Страница была уничтожена главным боссом<h1>')


def all_characters(request):
    return HttpResponse('<h1 align="center">Now we have only hero</h1>')

def about_character(request, character_name):
    match character_name:
        case 'hero':    return HttpResponse('<h1 align="center">Hero</h1>')
        case _:         return HttpResponse('<h1 align="center "> What character u mean? </h1>')

def all_weapons(request):
    return HttpResponse('<h1 aling="center"> Weapons </h1> <p> Sword </p> <p> Shield </p> <p> Bow </p>')

def about_weapons(request, weapon_name):
    match weapon_name:
        case 'sword':   weapon = 'sword'
        case 'bow':     weapon = 'bow'
        case 'shield':  weapon = 'shield'
        case _:         weapon = 'Now we have only: sword, shield and bow'
    return HttpResponse(f'<h1 align="center"> {weapon} </h1>')


def about_maps(request, map_name):
    match map_name:
        case 'start':   return HttpResponse('<h1 align="center">First map</h1>')
        case 'second':  return HttpResponse('<h1 align="center">Second map</h1>')
        case _:         return HttpResponse('<h1 align="center">We have only first and second maps</h1>')

def all_maps(request):
    return HttpResponse('<h1 align="center">Now we have only started map and river map</h1>')



