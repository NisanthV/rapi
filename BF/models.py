from django.contrib.auth.models import User
from django.db import models

class NotesData(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    data_time=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="notes")

    def __str__(self):
        return self.title