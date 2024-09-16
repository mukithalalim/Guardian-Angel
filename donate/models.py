from django.db import models

# Create your models here.
class Payment(models.Model):
	"""
    This class contains the essential fields and behaviors of the data you’re storing. 
	Each model maps to a single database table.

    This class is used to create a database table containg those attributes.
    """
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	amount = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	bkash = models.CharField(max_length=200, null=True)
	trxid = models.CharField(max_length=200, null=True)

	def __str__(self):
		"""
		This method will show the list as username in the django database Users table.

		:param name: self - used to access the attributes and methods of the class in python.
		:param type: reference
		:return: str
		"""
		return self.name