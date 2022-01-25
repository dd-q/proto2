from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *


def update_user(request, id):
    profile = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('mypageapp:update_user', id = id)
    else:
        try :
            pet = Pet.objects.get(user_id = id)
        except :
            pet = Pet.objects.filter(user_id = id)

        form = UserForm(instance = profile)
        return render(request, 'mypageapp/user_profile.html', {'form':form, 'pet':pet},
        )


def create_pet(request, id):
    pet = Pet.objects.get(user_id = id)    
    if request.method=='POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('mypageapp:update_user', id = id)
        else:
            return HttpResponse('다시해라')
    else:
        form = PetForm()
        return render(request, 'mypageapp/pet_profile.html', 
        {'form':form},
        
        )

# def show(request, id):
    pet = Pet.objects.get(user_id = id)
    return render(request, 'mypageapp/user_profile.html', {'pet':pet})

