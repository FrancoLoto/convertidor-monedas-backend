from cloudinary.models import CloudinaryField
from django.db import models
from django.utils import timezone


class New(models.Model):

    class Meta:
        ordering = ('-created_at',)

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    thumbernail = CloudinaryField('Image', overwrite=True, format="jpg")
    content = models.TextField()
    time_read = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
