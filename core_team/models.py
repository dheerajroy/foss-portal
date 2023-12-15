from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CoreTeamMember(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='core_team_pictures')
    position = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    current_qualification = models.CharField(max_length=50)
    phone_number = models.PositiveBigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999999)])
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} | {self.position}'
