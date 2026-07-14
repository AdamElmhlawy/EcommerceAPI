from django.utils.text import slugify
from django.db import models

class SlugModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name