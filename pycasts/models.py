from django.db import models

from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=500)
    guid = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"