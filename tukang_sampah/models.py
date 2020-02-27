from django.db import models

# Create your models here.
class Collected(models.Model):
	collected_trash_paper = models.FloatField(default=0)
	collected_trash_food = models.FloatField(default=0)
	collected_trash_plastic = models.FloatField(default=0)
	user = models.IntegerField()

	def sum_collected_trash(self, user_now):
		sum = 0
		collect = collected.objects.filter(user=user_now)
		
		for collected in collect:
			sum += collected.collected_trash_paper + collected.collected_trash_food + collected.collected_trash_plastic

		return sum

	def create_collected(self,collected_trash_paper,collected_trash_plastic,collected_trash_food,user):
		if not collected_trash_food:
			raise ValueError("Not Food")
		if not collected_trash_plastic:
			raise ValueError("Not Plastic")
		if not collected_trash_paper:
			raise ValueError("Not Paper")

		order = self.model(
				collected_trash_paper = collected_trash_paper,
				collected_trash_plastic = collected_trash_plastic,
				collected_trash_food = collected_trash_food,
				user = user,
			)

		order.save(using=self._db)
		return order