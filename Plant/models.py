from django.db import models


# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=20)
    g_sunlight = models.IntegerField()
    water = models.IntegerField()
    g_temp = models.IntegerField()
    pid = models.AutoField(primary_key=True)
    size = models.CharField(max_length=1)

    def __str__(self):
        return self.pid, self.name, self.size, self.g_temp, self.g_sunlight


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    h_sunlight = models.IntegerField()
    h_temp = models.IntegerField()
    desired_size = models.CharField(max_length=1)

    def __str__(self):
        return self.user_id, self.desired_size, self.h_temp, self.h_sunlight
