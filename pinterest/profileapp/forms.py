from django.forms import ModelForm

from .models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
        #user 필드는 서버에서 처리
