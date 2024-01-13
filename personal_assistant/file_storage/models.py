from django.db import models


class File(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f"{self.title}"

