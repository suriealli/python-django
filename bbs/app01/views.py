from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
# Create your views here.
def index(request):
    return render_to_response('index.html',)


def contact_me(request):
    pass
