from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=200)
	territorial_bond_total = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
	treasury_bond_total = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)

	def __str__(self):
		return self.name


class Section(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	capital_total = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)

	def __str__(self):
		return self.name + self.project.name

class CapitalFlow(models.Model):
	project= models.ForeignKey(Project, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	pay_time = models.DateField()
	account = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)

	OPTION_A = 'Territorial'
	OPTION_B = 'Treasury'

	CHOICES = [
		(OPTION_A, 'Territorial'),
		(OPTION_B, 'Treasury'),
	]
	capital_type = models.CharField(max_length=50, choices=CHOICES)

	def __str__(self):
		return self.project.name + self.section.name + self.accounts




