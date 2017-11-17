from django.db import models

# Create your models here.
class CommonFields(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    class Meta:
        abstract = True

class Epic(CommonFields):
    pass

class Story(CommonFields):
    epics = models.ForeignKey(Epic, on_delete=models.CASCADE)

class Task(CommonFields):
    stories = models.ForeignKey(Story, on_delete=models.CASCADE)

class Subtask(CommonFields):
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

class Issue(CommonFields):
    pass