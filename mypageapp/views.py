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

# Q1해결. try/excetp 문 이용해서 한 계정에 두 번 등록되지 않도록.
def create_pet(request, id):
    # pet = Pet.objects.get(user_id = id)    
    if request.method=='POST':
        form = PetForm(request.POST, request.FILES)
        form.user = User.objects.get(id=id)
        if form.is_valid():
            print(form.user)
            profile = form.save(commit=False)
            profile.user = form.user
            # print(id)
            # print(profile.user)
            profile.save()
            return redirect('mypageapp:update_user', id = id)
        else:
            return HttpResponse('다시해라')
    else:
        form = PetForm()
        # form.user = User.objects.get(id=id)
        # form.user = id
        # print(form.user)
        return render(request, 'mypageapp/pet_profile.html', 
        {'form':form},
        )

def update_pet(request, id):
    profile = Pet.objects.get(user_id=id)
    profile.user = User.objects.get(id=id)
    if request.method=='POST':
        form = PetForm(request.POST, request.FILES, instance = profile)
        form.user = User.objects.get(id=id)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = form.user
            
            profile.save()
            return redirect('mypageapp:update_user', id = id)
    else:
        form = PetForm(instance = profile)
        print(form)
        return render(request, 'mypageapp/update_pet.html', {'form':form},
        )


# def show(request, id):
    # pet = Pet.objects.get(user_id = id)
    # return render(request, 'mypageapp/user_profile.html', {'pet':pet})

