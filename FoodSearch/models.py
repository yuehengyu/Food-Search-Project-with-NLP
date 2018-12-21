from django.db import models

# Create your models here.
class stateInfo(models.Model):
    State_Code=models.IntegerField(primary_key=True)
    State_Name=models.CharField(max_length=50)
    Abbreviation = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table='state'

