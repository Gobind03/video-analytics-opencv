from django.forms import ModelForm, DateTimeInput, SelectDateWidget
from . import models


class CameraModelForm (ModelForm):
    class Meta:
        model = models.CameraModel
        fields = ['title', 'description', 'preferred_analytics', 'rtvsp_url', 'is_active']

    def __init__(self, *args, **kwargs):
        super(CameraModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'