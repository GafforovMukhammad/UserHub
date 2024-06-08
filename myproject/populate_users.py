import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

import random
from myapp.models import User
from faker import Faker 
fakegan = Faker()

def populate(N=19):
	for _ in range(N):
		first_name = fakegan.first_name()
		last_name = fakegan.last_name()
		email = fakegan.email()
		date_of_birth = fakegan.date_of_birth(minimum_age = 18, maximum_age = 90)


		#Create a new user 
		User.objects.create(
			first_name = first_name,
			last_name  = last_name,
			email = email,
			date_of_birth = date_of_birth
		)
if __name__ == '__main__':
	print("Populating database with fake users...")
	populate(20) #number of fake users
	print("Database populated succesfully!")
