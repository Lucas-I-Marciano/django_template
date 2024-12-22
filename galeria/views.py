from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello World</h1><img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTPsp9j_fEDBRLmPBRlmWgGqdBgZ5CGaVoGPYAlVBsTYA3Iim6:https://e7.pngegg.com/pngimages/148/800/png-clipart-agnes-youtube-despicable-me-animation-youtube-child-toddler-thumbnail.png&s>")