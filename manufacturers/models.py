from django.db import models


class Manufacturer(models.Model):
	name = models.CharField(max_length=100)
	logotype = models.ImageField(
		upload_to='manufacturers/logotype',
		blank=True)
	email = models.EmailField(max_length=254, blank=True)
	website = models.URLField(max_length=200, blank=True)

	def __str__(self):
		return self.name