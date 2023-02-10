from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    csv = models.FileField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title


class DemoModel(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    levels = models.CharField(max_length=256, blank=True, null=True)
    code = models.CharField(max_length=256, blank=True, null=True)
    units = models.CharField(max_length=256, blank=True, null=True)
    variable_code = models.CharField(max_length=256, blank=True, null=True)
    variable_name = models.CharField(max_length=256, blank=True, null=True)
    variable_category = models.CharField(max_length=256, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
