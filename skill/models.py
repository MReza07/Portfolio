from django.db import models


# Create your models here.
class my_skill(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50, blank=False)
    dese = models.TextField(max_length=509, blank=True)
    datetime = models.DateField(auto_now_add=True)

    def summary(self):
        return self.dese[0:100]

    def __str__(self):
        return self.title


class contact_info(models.Model):
    cname = models.CharField(max_length=50, blank=False)
    cemail = models.EmailField()
    csubject = models.CharField(max_length=50, blank=False)
    cmessage = models.TextField()

    def __str__(self):
        return self.cname
