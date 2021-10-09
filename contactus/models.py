from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    issue = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
