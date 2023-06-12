from django.db import models

class ChatMessage(models.Model):
    session_id = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.message}"
