from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Manager(BaseUserManager):
	def create_user(self,first_name,is_mitra,is_customer,email,username,password=None):
		if not email:
			raise ValueError("Not Email")
		if not username:
			raise ValueError("Not Username")
		if not first_name:
			raise ValueError("Not first_name")

		user = self.model(
				email = self.normalize_email(email),
				first_name = first_name,
				username = username,
				is_mitra = is_mitra,
				is_customer = is_customer,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,username,password):
		user = self.create_user(
				email = self.normalize_email(email),
				username = username,
				password = password,
			)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Person(AbstractBaseUser):
	email = models.EmailField(verbose_name='email', max_length=100, unique=True)
	username = models.CharField(max_length=30, unique=True)
	first_name = models.CharField(max_length=30, unique=False)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last_login', auto_now_add=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_mitra = models.BooleanField(default=False)
	is_customer = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email','is_mitra','is_customer']

	objects = Manager()

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None):
		return self.is_admin

	def has_module_perms(self,app_label):
		return True