from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Manager(BaseUserManager):
	def create_user(self,first_name,alamat,no_hp,username,password=None):
		if not no_hp:
			raise ValueError("Not no_hp")
		if not username:
			raise ValueError("Not Username")
		if not first_name:
			raise ValueError("Not first_name")
		if not alamat:
			raise ValueError("Not alamat")

		user = self.model(
				no_hp = no_hp,
				first_name = first_name,
				username = username,
				alamat = alamat,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,no_hp,username,password):
		user = self.create_user(
				first_name = 'SUPERUSER',
				alamat = 'SUPERUSER',
				no_hp = no_hp,
				username = username,
				password = password,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Person(AbstractBaseUser):
	no_hp = models.BigIntegerField(unique=True)
	username = models.CharField(max_length=30, unique=True)
	first_name = models.CharField(max_length=30, unique=False)
	alamat = models.CharField(max_length=100, unique=False)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last_login', auto_now_add=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['no_hp']

	objects = Manager()

	def __str__(self):
		return self.username

	def has_perm(self,perm,obj=None):
		return self.is_admin

	def has_module_perms(self,app_label):
		return True