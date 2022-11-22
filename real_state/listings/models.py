from django.db import models

# Models are basically the representation of the database schema. For example, on table in the database will be converter into a python object.
# This allow to iterate to the database with python. 


# The "Model" allows the class to be interpreted as a database table.
class Listing(models.Model):
    # THe model will create a id for us.
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address =  models.CharField(max_length=100)
#   image = models.ImageField()

    def __str__(self):
        return self.title

