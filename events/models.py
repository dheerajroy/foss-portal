from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Event(models.Model):
    poster = models.ImageField(upload_to='posters')
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField()
    publish = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.title} | {self.date_time}'


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.PositiveBigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999999)])
    current_qualification = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} | {self.current_qualification} | {self.phone_number}'


class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.PositiveBigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999999)])
    current_qualification = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=50, blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} | {self.rating} | {self.current_qualification} | {self.phone_number}'
