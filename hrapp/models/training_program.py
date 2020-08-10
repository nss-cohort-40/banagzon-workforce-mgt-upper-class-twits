from django.db import models

class TrainingProgram(models.Model):

    
    training_title = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    max_capacity = models.IntegerField()
    

    class Meta:
        verbose_name = ("Training Program")
        verbose_name_plural = ("Training Programs")