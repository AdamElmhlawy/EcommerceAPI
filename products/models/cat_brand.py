from django.db import models
from .common import SlugModel

class Category(SlugModel):
    description = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, related_name="children")


class Brand(SlugModel):
    pass