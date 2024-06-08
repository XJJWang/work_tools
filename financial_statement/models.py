from django.db import models

class BasicInfo(models.Model):
	name = models.CharField(max_length=200)
	territorial_bond_total = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
	treasury_bond_total = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
	def __str__(self):
		return self.name