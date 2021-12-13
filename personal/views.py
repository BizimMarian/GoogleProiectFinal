from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.
# def home_screen_view(request):
#     return render(request,"interface.html")

def display(request):
    return render(request,'interface.html')

def show_Actions(request):
    items = Actiune.objects.all()
    context = {
        'items': items,
        'header': 'Actiune'
    }

    return render(request,'interface.html',context)


def show_Horrors(request):
    items = Horror.objects.all()
    context = {
        'items': items,
        'header': 'Horror'
    }

    return render(request,'interface.html',context)

def show_Comedies(request):
    items = Comedie.objects.all()
    context = {
        'items': items,
        'header': 'Comedii'
    }

    return render(request,'interface.html',context)

def show_Dramas(request):
    items = Drama.objects.all()
    context = {
        'items': items,
        'header': 'Drame'
    }

    return render(request,'interface.html',context)


def New_Actiune(request):
    if request.method == "POST":
        form = ActiuneForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'interface.html')


    else:
        form = ActiuneForm()
        return  render(request,'buttons.html',{'form':form})

def New_Horror(request):
    if request.method == "POST":
        form = HorrorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'interface.html')


    else:
        form = HorrorForm()
        return  render(request,'buttons.html',{'form':form})

def New_Comedie(request):
    if request.method == "POST":
        form = ComedieForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'interface.html')


    else:
        form = ComedieForm()
        return  render(request,'buttons.html',{'form':form})


def New_Drama(request):
    if request.method == "POST":
        form = DramaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'interface.html')


    else:
        form = DramaForm()
        return  render(request,'buttons.html',{'form':form})



def Remove_actiune(request,pk):
    Actiune.objects.filter(id=pk).delete()
    items = Actiune.objects.all()
    context = {
        'items': items
    }
    return render(request,'interface.html',context )


def Remove_horror(request,pk):
    Horror.objects.filter(id=pk).delete()
    items = Horror.objects.all()
    context = {
        'items': items
    }
    return render(request,'interface.html',context )

def Remove_drame(request,pk):
    Drama.objects.filter(id=pk).delete()
    items = Drama.objects.all()
    context = {
        'items': items
    }
    return render(request,'interface.html',context )


def Remove_comedie(request,pk):
    Comedie.objects.filter(id=pk).delete()
    items = Comedie.objects.all()
    context = {
        'items': items
    }
    return render(request,'interface.html',context )











