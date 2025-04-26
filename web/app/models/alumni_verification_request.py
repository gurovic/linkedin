import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver

from app.models.alumnipassword import AlumniPassword


class AlumniVerificationRequest(models.Model):
    ANSWER_CHOICES = [
        ('NA', 'Not answered'),
        ('AC', 'Accepted'),
        ('DE', 'Declined')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verification_requests')
    surname = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    university = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    photo = models.ImageField(upload_to="verif/", blank=True)
    approved = models.CharField(max_length=120, choices=ANSWER_CHOICES, default='NA')
    confirmation_sent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.surname} {self.first_name}, {self.get_approved_display()}'
        #return f'{self.user.last_name} {self.user.first_name}, {self.get_approved_display()}'

@receiver(post_save, sender=AlumniVerificationRequest)
def handle_approved_request(sender, instance, created, **kwargs):
    if not created and instance.approved == "AC":
        try:
            alumni_password = AlumniPassword.objects.get(user=instance.user)
            password_info = (
                f"\n\nВаши учетные данные для входа:\n"
                f"Имя пользователя: {instance.user.username}\n"
                f"Пароль: {alumni_password.password}"
            )
        except AlumniPassword.DoesNotExist:
            password_info = ""

        send_mail(
            "Ваш запрос на верификацию одобрен",
            f"Уважаемый(ая) {instance.user.first_name},\n\nВаш запрос на "
            f"верификацию был одобрен. Теперь вы имеете статус подтвержденного"
            f" выпускника.{password_info}\n\nС уважением,\nАдминистрация",
            "noreply@yoursite.com",
            [instance.email],
            fail_silently=False,
        )
        AlumniPassword.objects.filter(user=instance.user).delete()


@receiver(post_save, sender=AlumniVerificationRequest)
def handle_cancelled_request(sender, instance, created, **kwargs):
    if not created and instance.approved == "DE":
        send_mail(
            "Ваш запрос на верификацию отклонен",
            f"Уважаемый(ая) {instance.user.first_name},\n\nК сожалению, ваш "
            f"запрос на верификацию был отклонен. Для получения дополнительной"
            f" информации, пожалуйста, свяжитесь с администрацией.\n\n"
            f"С уважением,\nАдминистрация",
            "noreply@yoursite.com",
            [instance.email],
            fail_silently=False,
        )


