# models.py
from django.db import models
from django.contrib.auth.models import User

class FileRevision(models.Model):
    file = models.FileField(upload_to='files/')
    version = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('filename', 'version', 'user')

    def __str__(self):
        return f"{self.filename} (version {self.version}) by {self.user.username}"