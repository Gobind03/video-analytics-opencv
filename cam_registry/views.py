from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import CameraModel

# Create your views here.
from cam_registry.forms import CameraModelForm

# View to register a camera
@login_required(login_url='/accounts/login')
def register_cam(request):
    if request.method == "POST":
        form_fields = CameraModelForm(request.POST)
        if form_fields.is_valid():
            model_instance = form_fields.save(commit=False)
            model_instance.registered_by = request.user
            model_instance.save()
            return redirect(reverse('cam_registry_list'))
        else:
            context = {
                'form_fields': form_fields,
                'error_message': None
            }
    else:
        context = {
            'form_fields': CameraModelForm(),
            'error_message': None
        }

    return render(request, 'camera_registry/insert.html', context=context)


def list_cam(request):
    cam_list = CameraModel.objects.all()
    return render(request, 'camera_registry/list.html', context= {'cam_list': cam_list})

