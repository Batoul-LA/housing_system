from django.shortcuts import render, get_object_or_404, redirect
from .forms import CameraForm, CameraRecordForm
from .models import Camera, CameraRecord
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CameraSerializer, CameraRecordSerializer

def index(request):
    return render(request, 'wellness/index.html')

# إدارة الكاميرات
def add_camera(request):
    if request.method == 'POST':
        form = CameraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring:camera_list')  

    else:
        form = CameraForm()
    return render(request, 'monitoring/add_camera.html', {'form': form})

def camera_list(request):
    cameras = Camera.objects.prefetch_related('records')
    return render(request, 'monitoring/camera_list.html', {'cameras': cameras})

# إدارة التسجيلات
def record_list(request):
    records = CameraRecord.objects.select_related('camera').order_by('-start_time')
    return render(request, 'monitoring/record_list.html', {'records': records})

def record_detail(request, pk):
    record = get_object_or_404(CameraRecord, pk=pk)
    return render(request, 'monitoring/record_detail.html', {'record': record})

def record_create(request):
    if request.method == 'POST':
        form = CameraRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('monitoring:record_list')  

    else:
        form = CameraRecordForm()
    return render(request, 'monitoring/record_form.html', {'form': form})

def record_delete(request, pk):
    record = get_object_or_404(CameraRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('monitoring:record_list')  
    return render(request, 'monitoring/record_confirm_delete.html', {'record': record})

class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

class CameraRecordViewSet(viewsets.ModelViewSet):
    queryset = CameraRecord.objects.all()
    serializer_class = CameraRecordSerializer