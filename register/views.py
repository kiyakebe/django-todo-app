from django.shortcuts import render, redirect
from forms import RegiisterFrom


# Create your views here.
def register(response):
    if(response.method == "POST"):
        form = RegiisterFrom(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegiisterFrom(response.POST)
        
    return render(response, "register/register.html", {"form": form})