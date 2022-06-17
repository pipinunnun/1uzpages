from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """регистрация нового пользователя"""
    if request.method != 'POST':
        #пустая строка
        form = UserCreationForm()
    else:
        #обработка заполненой формы
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #выполнение входа/перенаправление на домашнюю страниицу
            login(request, new_user)
            return redirect('blogs:index')

    #пустая строка
    context = {'form': form}
    return render(request, 'registration/register.html', context)