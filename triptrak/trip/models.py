from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)  # USA = US, EUROPE = EU
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    # From 'User' model, we can get all trips associated to a user using -> User.trips
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self) -> str:
        return f"{self.country.upper()} | {self.city.title()}"


class Note(models.Model):
    EXCURSIONS = (
        ('event', 'Event'),
        ('dining', 'Dining'),
        ('experience', 'Experience'),
        ('general', 'General'),
    )
    # From 'Trip' model, we can access all notes by -> Trip.notes
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    type = models.CharField(max_length=100, choices=EXCURSIONS)
    img = models.ImageField(upload_to='notes', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"{self.name.title()} in {self.trip.city.title()}"
