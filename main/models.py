from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Advocate(models.Model):
    # states = (
    # ('Andhra Pradesh', 'Andhra Pradesh'),
    # ('Arunachal Pradesh', 'Arunachal Pradesh'),
    # ('Assam', 'Assam'),
    # ('Bihar', 'Bihar'),
    # ('Chhattisgarh', 'Chhattisgarh'),
    # ('Goa', 'Goa'),
    # ('Gujarat', 'Gujarat'),
    # ('Haryana', 'Haryana'),
    # ('Himachal Pradesh', 'Himachal Pradesh'),
    # ('Jharkhand', 'Jharkhand'),
    # ('Karnataka', 'Karnataka'),
    # ('Kerala', 'Kerala'),
    # ('Madhya Pradesh', 'Madhya Pradesh'),
    # ('Maharashtra', 'Maharashtra'),
    # ('Manipur', 'Manipur'),
    # ('Meghalaya', 'Meghalaya'),
    # ('Mizoram', 'Mizoram'),
    # ('Nagaland', 'Nagaland'),
    # ('Odisha', 'Odisha'),
    # ('Punjab', 'Punjab'),
    # ('Rajasthan', 'Rajasthan'),
    # ('Sikkim', 'Sikkim'),
    # ('Tamil Nadu', 'Tamil Nadu'),
    # ('Telangana', 'Telangana'),
    # ('Tripura', 'Tripura'),
    # ('Uttar Pradesh', 'Uttar Pradesh'),
    # ('Uttarakhand', 'Uttarakhand'),
    # ('West Bengal', 'West Bengal')
    # )   

# Accessing individual states:
# For example, to access the first state:
# first_state = indian_states[0][0]

    # areas = (
    # ("Civil Law", "Civil Law"),
    # ("Criminal Law", "Criminal Law"),
    # ("Corporate Law", "Corporate Law"),
    # ("Commercial Law", "Commercial Law"),
    # ("Family Law", "Family Law"),
    # ("Real Estate Law", "Real Estate Law"),
    # ("Intellectual Property Law", "Intellectual Property Law"),
    # ("Labour Law", "Labour Law"),
    # ("Employment Law", "Employment Law"),
    # ("Environmental Law", "Environmental Law"),
    # ("Tax Law", "Tax Law"),
    # ("Constitutional Law", "Constitutional Law")
    # )

# Accessing individual areas of law:
# For example, to access the first area of law:
# first_area = areas_of_law[0][0]

    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank = True )
    practice_area = models.CharField( max_length = 500, null = True, blank=True)
    experience = models.IntegerField( null = True, blank=True)
    advocate_id = models.TextField( unique = True , null = True, blank=True)
    location  = models.CharField( max_length=500, null = True, blank=True )
    state = models.CharField( max_length = 100, null = True, blank=True)
    languages = models.CharField(max_length=100, null = True, blank=True)
    ratings = models.FloatField( null = True, blank=True)
    ratingno = models.IntegerField( null = True, blank=True)
    profile_pic = models.ImageField(upload_to = "advocate_pics", null = True, blank=True)
    # islawyer = models.BooleanField( value = True )
    # phone_number = models.PhoneNumberField(_(""))
# , null=True, blank=True


class Client(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank = True )

    # islawyer = models.BooleanField( value = False )