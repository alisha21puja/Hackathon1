from django.db import models
from django.conf import settings

from django.utils.timezone import now

# from froala_editor.fields import FroalaField

from django.contrib.auth import get_user_model
from Organizer.models import OrganiseEvent,EventDetails
from django.contrib.auth.models import User


# Create your models here.


class ParticipateEvent(models.Model):
	us = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
	Event_id = models.ForeignKey(OrganiseEvent,on_delete=models.CASCADE,primary_key=True)
=======
	Event_id = models.ForeignKey(OrganiseEvent,on_delete=models.CASCADE)
>>>>>>> 00486efd62bd717f2eaff3e6c9f80a737c54bef9

    
