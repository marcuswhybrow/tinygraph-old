from django.db import models

class Host(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    

class DataSource(models.Model):
    host = models.ForeignKey(Host)
    name = models.CharField(max_length=100)
    

# class Data(models.Model):
#     source
#     created = models.DateTimeField(auto_now_add=True)