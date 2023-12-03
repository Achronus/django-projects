from django.db import models
from django.utils.text import slugify

# Create your models here.
class Link(models.Model):
    name: str = models.CharField(max_length=50, unique=True)
    url: str = models.URLField(max_length=200)
    slug: str = models.SlugField(unique=True, blank=True)
    num_clicks: int = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.id}: {self.name} | Num clicks: {self.num_clicks}'

    def increment_clicks(self) -> None:
        self.num_clicks += 1
        self.save()

    def save(self, *args, **kwargs) -> None:
        # Set slug of newly created object
        if not self.slug:
            self.slug = slugify(self.name)
            self.save()
        
        return super().save(*args, **kwargs)
    