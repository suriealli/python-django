from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Message

# Create your views here.
from django.shortcuts import render_to_response
# Create your views here.
def index(request):
    #contact_me='contact'
    return render_to_response('blog/index.html',locals())


def contact_me(request):
    messages = Message.objects.all().order_by('vote_date')
    context = {'messages' : messages,}
    return render_to_response('blog/message.html',locals())

def postmessage(request):
    postname = request.POST['name']
    postcontext = request.POST['context']
    if postname.replace(' ','').strip() == '':
        return render(request, 'blog/message.html', {'error_message' : 'You did not input your name',})
    elif postcontext.strip().replace(' ','') == '':
        return render(request, 'blog/message.html', {'error_message' : 'You did not input context',})
    elif len(postname) >= 20:
        return render(request,'blog/message.html' , {'error_message' : 'you name is too long,please check!',})
    elif len(postcontext) >= 200:
        return render(request,'blog/message.html' , {'error_message' : 'you contenxt is too long,please check!',})
    else:
        m = Message(name = postname, context = postcontext, vote_date = timezone.now())
        m.save()
        return HttpResponseRedirect(reverse('message'))
