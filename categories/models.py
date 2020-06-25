from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        "categories.Category", related_name='children', 
        on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name