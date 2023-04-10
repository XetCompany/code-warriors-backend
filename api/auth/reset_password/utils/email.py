from django.core.mail import EmailMessage


def send_email_reset_password(email, username, token):
    title = 'Сброс пароля'
    link = f'http://localhost:8000/api/auth/reset_password/password_reset/{token}'
    # TODO: change link to production
    message = f'Для сброса пароля перейдите по ссылке: {link}. Ваш логин: {username}'
    email = EmailMessage(title, message, to=[email])
    email.send()
