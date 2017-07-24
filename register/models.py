from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.
class jfuser(models.Model):
	def __unicode__(self):
	 	return  unicode(self.user)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phno=models.IntegerField(default=70000000)
	college=models.CharField(default='college',max_length=50)
	nofc=models.IntegerField(default=0)

class jfadmin(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)


class jfcompany(models.Model):
	cid=models.CharField(primary_key=True,max_length=100, blank=True, unique=True, default=uuid.uuid4)
	name=models.CharField(default='company',max_length=50)

class usercompanies(models.Model):
	user=models.ForeignKey(jfuser,on_delete=models.CASCADE)
	cid=models.CharField(default='company',max_length=50)
	paid=models.BooleanField(default=False)
	image=models.ImageField(upload_to='paid')

#class test(models.Model):
	jfcompany=models.OneToOneField(jfcompany,on_delete=models.CASCADE)
	nofp=models.IntegerField(default=0)

#class testscore(models.Model):




	


