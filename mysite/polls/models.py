from django.db import models

class Capture(models.Model):
	base_language=models.Charfield(max_length=25)
	company_name=models.Charfield(max_length=35)
	id=models.AutoField(primary_key=True)
