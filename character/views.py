from django.shortcuts import render
from django.http import HttpResponse


def about_character(request):
    return HttpResponse('<h1 align="center">Character</h1>')

def about_weapons(request, weapon_name):
    match weapon_name:
        case 'sword':   weapon = 'sword'
        case 'bow':     weapon = 'bow'
        case 'shield':  weapon = 'shield'
    return HttpResponse(f'<h1 align="center">Weapons</h1> <p><h1> {weapon} </h1></p>')

def main_page(request):
    return HttpResponse('<h1 align="center">Main Page</h1>')

def about_maps(request):
    return HttpResponse('<h1 align="center">Maps</h1>')
