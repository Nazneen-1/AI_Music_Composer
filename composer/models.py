from django.db import models
from django.contrib.auth.models import User

class Composition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="AI_Composition")
    style = models.CharField(max_length=50, choices=[
        ("Classical", "Classical"),
        ("Jazz", "Jazz"),
        ("Pop", "Pop"),
    ])
    # store relative path under MEDIA_ROOT, Django FileField handles it
    file = models.FileField(upload_to="compositions/")
    created_at = models.DateTimeField(auto_now_add=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
