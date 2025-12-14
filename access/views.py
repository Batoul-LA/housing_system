from django.shortcuts import render ,redirect
from django.http import HttpResponse
import segno
from django.http import HttpResponse
from .forms import AccessLogForm
from rest_framework import viewsets
from .models import QR, AccessLog
from .serializers import QRSerializer, AccessLogSerializer

def generate_qr(request, qr_id):
    qr_obj = QR.objects.get(id=qr_id)
    qr = segno.make(qr_obj.code)

    response = HttpResponse(content_type='image/png')
    qr.save(response, kind='png')
    return response

def index(request):
    return HttpResponse("App is working.")

def scan_qr(request):
    if request.method == 'POST':
        form = AccessLogForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('access-home')

    else:
        form = AccessLogForm()
    return render(request, 'access/scan_qr.html', {'form': form})

def access_log_list(request):
    logs = AccessLog.objects.select_related('qr', 'employee').order_by('-timestamp')
    return render(request, 'access/access_log_list.html', {'logs': logs})

class QRViewSet(viewsets.ModelViewSet):
    queryset = QR.objects.all()
    serializer_class = QRSerializer

class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer