from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """New users register. """
    if request.method != 'POST':
        # Make the blank form visible
        form = UserCreationForm()
    else: 
        # Form completed; process data
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
        
        login(request, new_user)
        return redict('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)