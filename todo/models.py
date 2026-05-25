from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    completed = models.BooleanField(default=False, verbose_name="Terminée")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créée le")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
