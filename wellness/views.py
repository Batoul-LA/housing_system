from django.shortcuts import render, redirect
from .forms import WellnessCheckForm
from .models import WellnessCheck
from rest_framework import viewsets
from .serializers import WellnessCheckSerializer

def add_wellness_check(request):
    if request.method == 'POST':
        form = WellnessCheckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wellness_list')
    else:
        form = WellnessCheckForm()
    return render(request, 'wellness/add_check.html', {'form': form})

def wellness_list(request):
    checks = WellnessCheck.objects.select_related('room', 'employee').order_by('-inspection_date')
    return render(request, 'wellness/wellness_list.html', {'checks': checks})

def index(request):
    return render(request, 'wellness/index.html')

class WellnessCheckViewSet(viewsets.ModelViewSet):
    queryset = WellnessCheck.objects.all()
    serializer_class = WellnessCheckSerializer