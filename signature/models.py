from django.db import models


class SignInput(models.Model):
    source = models.CharField("Mobile", max_length=10, null=True, blank=True)
    cust_id = models.CharField('Cust ID', max_length=14, blank=False)
    image = models.ImageField('Signature', blank=False, upload_to='sign')
    creation_time = models.DateTimeField(auto_now_add=True)

class SignOutput(models.Model):
    input = models.ForeignKey(SignInput, on_delete=models.CASCADE)
    status = models.CharField("status", max_length=7)
    authentic = models.BooleanField("auth", null=True)
    score = models.FloatField("Match Score", null=True)