from django.db import models

from datetime import datetime

# Create your models here.

class Notes(models.Model):

	br=(('CSE','cse'),
		('ECE','ece'),
		('EEE','eee'),('CIVIL','civil'),('MEC','mec'))
	sub=(('DJANGO','django'),('PYTHON','Python'),('C-Lang','c-lang'),
		('java','java'))

	branch=models.CharField(max_length=20,choices=br)
	subject=models.CharField(max_length=50,choices=sub)
	material=models.FileField(upload_to="studymaterial/",null=True,blank=True)
	description=models.TextField(max_length=500)
	uploadingdate=models.DateField(default=datetime.now)

	def __str__(self):
		return self.branch
		