from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from users.validators import validate_email, validate_login

User = get_user_model()


class EditProfileForm(forms.Form):

    login = forms.CharField(max_length=150,
                            label='Имя пользователя',
                            help_text='Максимум 150 символов',
                            required=True)

    email = forms.EmailField(label='Почта',
                             required=False)



    def validate_edit_login(self, current_user):
        login = self.cleaned_data['login']

        if len(login.strip()) < 2:
            self.add_error('login', 'Длина имени не менее 2 символов!')
            return

        if login != current_user.username and User.objects.filter(username=login):
            self.add_error('login',
                           'Пользователь с таким именем уже существует!')
            return

        return True

    def validate_edit_email(self, current_user):
        email = self.cleaned_data['email']

        if email != current_user.email and User.objects.filter(email=email):
            self.add_error('email',
                           'Пользователь с такой почтой уже существует!')
            return

        return True

    def validate_all(self, current_user):
        return self.validate_edit_email(current_user) and self.validate_edit_login(current_user)


class SignupForm(forms.Form):
    """
    Форма регистрации

    Fields:
        login (CharField): имя пользователя
        email (EmailField): электронная почта
        password (CharField): пароль
        password_repeat (CharField): еще раз пароль

    """
    email = forms.CharField(max_length=200,
                            label='Адрес электронной почты',
                            widget=forms.EmailInput,
                            required=True,
                            validators=[validate_email])
    login = forms.CharField(max_length=150,
                            label='Имя пользователя',
                            help_text='Максимум 150 символов',
                            required=True,
                            validators=[validate_login])
    password = forms.CharField(max_length=255, label='Пароль',
                               help_text='Максимум 255 символов',
                               widget=forms.PasswordInput,
                               required=True,
                               min_length=8,
                               validators=[validate_password])
    password_repeat = forms.CharField(max_length=255,
                                      label='Повторите пароль',
                                      widget=forms.PasswordInput)

    def check_passwords_match(self):
        password = self.cleaned_data['password']
        password_repeat = self.cleaned_data['password_repeat']

        if password != password_repeat:
            self.add_error('password', 'Пароли не совпадают!')
            return
        return password
