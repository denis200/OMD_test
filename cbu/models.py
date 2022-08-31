from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model


User = get_user_model()


class UserTable(models.Model):
    user = models.OneToOneField(
        User, 
        related_name="usertable", 
        on_delete=models.DO_NOTHING
    )

    def __str__(self) -> str:
        return self.user.username


class CBUData(models.Model):
    user_table = models.ForeignKey(
        UserTable, 
        on_delete=models.CASCADE
    )
    unit = models.PositiveIntegerField()
    reach = ArrayField( 
        base_field= models.FloatField(),
        blank=True
    )
