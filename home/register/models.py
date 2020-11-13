from django.db import models

# Create your models here.

class Register(models.Model):
    useremail = models.EmailField(max_length=64)
    userpw = models.CharField(max_length=64)
    username = models.TextField(max_length=32)
    # createtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sdesigne_user'
