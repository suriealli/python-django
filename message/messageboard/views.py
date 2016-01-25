from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse
from messageboard.models import Message
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    messages = Message.objects.all().order_by('vote_date')
    context = {'messages' : messages,}
    return render(request, 'message/index.html', context)


def postmessage(request):
    postname = request.POST['name']
    postcontext = request.POST['context']
    if postname.replace(' ','').strip() == '':
        return render(request, 'message/index.html', {'error_message' : 'You did not input your name',})
    elif postcontext.strip().replace(' ','') == '':
        return render(request, 'message/index.html', {'error_message' : 'You did not input context',})
    elif len(postname) >= 20:
        return render(request,'message/index.html' , {'error_message' : 'you name is too long,please check!',})
    elif len(postcontext) >= 200:
        return render(request,'message/index.html' , {'error_message' : 'you contenxt is too long,please check!',})
    else:
        m = Message(name = postname, context = postcontext, vote_date = timezone.now())
        m.save()
        return HttpResponseRedirect(reverse('index'))
        
