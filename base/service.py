from django.core.mail import send_mail


def vacancy_alert(user_email, username):
    send_mail(
        'Вы успешно зарегестировались на сайте Sphere candle! Добро пожаловать',
        f'Уважаемый/ая {username} , Ваша анкета успешна оставлена! Ожидайте ответа от нас на почту!',
        'kano.hideyoshi@mail.ru',
        [user_email], fail_silently=False)
