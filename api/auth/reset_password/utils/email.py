from django.core.mail import EmailMessage


def send_email_reset_password(email, username, token):
    title = 'Сброс пароля'
    link = f'http://localhost:3000/reset-password/{token}'
    # TODO: change link to production
    message = f'Для сброса пароля перейдите по ссылке: {link}. Ваш логин: {username}'
    email = EmailMessage(title, message, to=[email])
    email.send()
