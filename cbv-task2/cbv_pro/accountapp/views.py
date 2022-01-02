from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(username=un,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('show_lap')
        else:
            print('Invalid credentials')
            messages.error(request,'Invalid credentials')
    tempname_name = 'authapp/login.html'
    return render(request,tempname_name)


def registerview(request):
    form  = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    template_name = 'authapp/register.html'
    return render(request,template_name, context)

def logoutview(request):
    logout(request)
    return redirect('login')