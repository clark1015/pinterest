from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        #username의 칸을 비활성화 해주는 코드

