from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=200)
	pub_data = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to = 'images/')

	def summary(self):
		return self.body[:20]
