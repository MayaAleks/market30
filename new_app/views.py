from django.shortcuts import render

# Create your views here.
from .forms import PersonForm


def index(request):
    form = PersonForm()
    context={
        'form': form
    }
    if request.method =='POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context:{
                'form': form
            }
            return render(request, 'index.html', context)
    return render(request,'index.html', context)


def new_person_for(request):

    persons = Person.objects.all()
    context={
        'persons': persons
    }
    return render(request,'index.html', context)

