from django.shortcuts import render,redirect
from .models import signup
from django.views import generic
from django.views.generic import CreateView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib import auth
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'app/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
def index(request):

    if 'uid'in request.session:
       uid=request.session['uid']
       userrecord=signup.objects.get(id=uid)
       username=userrecord.Name
       context={'usernm':username}
       return render(request,'app/index.html',context)
    else:
       return render(request,'app/index.html',{})
def reg(request):
    if request.method=='POST':
        data1 = request.POST.get('nm','')
        data2 = request.POST.get('us', '')
        data3 = request.POST.get('em', '')
        data4 = request.POST.get('ps', '')

        song_obj = signup(Name=data1 ,Username=data2, Email=data3, Password=data4)
        song_obj.save()
        return render(request, 'app/index.html')
    else:
        return render(request, 'app/index.html')
def login(request):
    if request.method == 'POST':
        Uss = request.POST['us']
        Pss = request.POST['ps']
        try:
            d1 = signup.objects.get(Username=Uss,Password=Pss)

        except signup.DoesNotExist:
           ''' d1 = None
            d2 = None
            if (Uss == d1 and Pss == d2):
              return render(request, 'app/index.html')
            else:
               return render(request, 'app/index.html')'''
        else:
            if (Uss == d1.Username and Pss == d1.Password):
                request.session['uid'] = d1.id
                return render(request, 'app/index.html')
            else:
                return render(request, 'app/index.html')
    return render(request, 'app/index.html')
def logout(request):
    auth.logout(request)
    try:
        del request.session['userid']
    except KeyError:
        pass
    return render(request,'app/index.html')
def blog(request):
    return render(request, 'app/blog.html', {})
def contact(request):
    return render(request, 'app/contact.html', {})
def about(request):
    return render(request, 'app/about.html', {})
def services(request):
    return render(request, 'app/services.html', {})
def single(request):
    return render(request, 'app/single.html', {})
def work(request):
    return render(request, 'app/work.html', {})

def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))