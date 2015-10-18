from django.db import models

# Create your models here.

class Shopinformation(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=128,)
  tel = models.CharField(max_length=64)
  addr = models.CharField(max_length=256)

  def __unicode__():
    return u'%s %s %s ;' %(self.name, self.tel, self.addr)
