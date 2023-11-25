from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(user_email):
    """
    Задача на отправку приветственного письма пользователю после регистрации.
    :param user_email: Почта пользователя.
    :return:
    """

    subject = 'Добро пожаловать в управление библиотекой.'
    message = 'Благодарим Вас за регистрацию в нашем приложении.'
    from_email = 'book-management@email.com'
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)

    print(f'Отправка приветственного письма по электронной почте {user_email}')
    print(f'Тема: {subject}')
    print(f'Сообщение: {message}')
