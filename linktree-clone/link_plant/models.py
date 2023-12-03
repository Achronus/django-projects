from django.db import models


class Profile(models.Model):
    BG_CHOICES: tuple[tuple[str, str], ...] = (
        # Format -> (Saved in database, human readable format)
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )

    name: str = models.CharField(max_length=100)
    slug: str = models.SlugField(max_length=100)
    bg_colour: str = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self) -> str:
        return self.name


class Link(models.Model):
    text: str = models.CharField(max_length=100)
    url: str = models.URLField()

    # Many to one relationship (many links to 1 profile)
    profile: Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')  # Adds profile.links using 'related_name'

    def __str__(self) -> str:
        return f'{self.text} - {self.profile.name}'
