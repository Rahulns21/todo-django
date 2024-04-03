from django.db import models
from autoslug import AutoSlugField

class Task(models.Model):
    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self) -> str:
        return self.task
    
    def save(self, *args, **kwargs):
        # If title has changed, update the slug
        if self.id:
            original_task = Task.objects.get(id=self.id)
            if original_task.task != self.task:
                self.slug = None
        super().save(*args, **kwargs)

    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='task', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)