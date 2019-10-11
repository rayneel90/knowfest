from django.db import models


class SignInput(models.Model):
    source = models.CharField("Mobile", max_length=10, null=True, blank=True)
    account = models.CharField('account', max_length=14, blank=False)
    image = models.FileField('Image', blank=False)
    creation_time = models.DateTimeField(auto_now_add=True)

class SignOutput(models.Model):
    input = models.ForeignKey(SignInput, on_delete=models.CASCADE)