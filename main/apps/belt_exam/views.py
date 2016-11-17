from django.shortcuts import render, redirect
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'belt_exam/index.html')
