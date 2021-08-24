from django.db import models


class MatchData(models.Model):
    name = models.CharField(max_length=2550, unique=True)
    message = models.CharField(max_length=2550, unique=True,blank=False)
    email = models.CharField(max_length=2550, unique=True)

    class Meta:
        db_table = "Email_Field"
