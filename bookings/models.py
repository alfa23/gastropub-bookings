import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from phone_field import PhoneField


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking")
    booking_date = models.DateField(auto_now=False)
    booking_time = models.TimeField(auto_now=False)
    booking_covers = models.PositiveIntegerField(default=2,
        validators=[MinValueValidator(1, 'There must be at least one diner!'),
        MaxValueValidator(16, 'More than 16 diners? Please call to book!')]
    )
    booking_comment = models.TextField(max_length=250, blank=True)
    booking_confirmed = models.BooleanField(default=False)
    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-booking_date']


class UserReg(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact_no = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return str(self.user)
