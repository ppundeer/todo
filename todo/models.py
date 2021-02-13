from django.db import models

class todoItem(models.Model):
    content = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content