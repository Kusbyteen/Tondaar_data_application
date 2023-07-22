from django.shortcuts import render

# Create your views here.
def home_view(request):
    # Your view logic goes here
    return render(request, 'home.html')
