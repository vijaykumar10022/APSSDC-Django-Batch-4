from django.db import models

# Create your models here.


class Materials(models.Model):
	branch=models.CharField(max_length=30)
	subject=models.CharField(max_length=20)
	notes=models.FileField(max_length=500)
	description=models.TextField(max_length=500,null=True)
	uploadingdate=models.CharField(max_length=20)

	def __str__(self):
		return self.subject +" "+self.branch
