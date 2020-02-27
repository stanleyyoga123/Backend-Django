from django.db import models
from account.models  import Person

# Create your models here.
class Order(models.Model):
	order_trash_paper = models.FloatField(default=0)
	order_trash_food = models.FloatField(default=0)
	order_trash_plastic = models.FloatField(default=0)
	user = models.ForeignKey(Person, on_delete = models.CASCADE)
	is_taken = models.BooleanField(default=False)

	def change_taken(self, user):
		order = Order.objects.get(user = user)
		order.is_taken = True
		order.save()

	def create_order(self, order_trash_paper, order_trash_food, order_trash_plastic, user):
		if not order_trash_plastic:
			raise ValueError('Not plastic')
		if not order_trash_food:
			raise ValueError('Not Food')
		if not order_trash_paper:
			raise ValueError('Not Paper')

		order = self.model(
				order_trash_paper = order_trash_paper,
				order_trash_food = order_trash_food,
				order_trash_plastic = order_trash_plastic,
				user = user,
			)

		order.is_taken = False

		order.save(using=self._db)
		return order