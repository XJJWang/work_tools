from django.db import models # type: ignore


class Project(models.Model):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=50, null=True, blank=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class ProjectInvestment(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=11, decimal_places=2, default=0.00)
    def __str__(self):
        return self.name + str(self.amount)


class Section(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(
        max_digits=11, decimal_places=2, default=0.00)

    def __str__(self):
        return self.project.name + '|' + self.name  

class CapitalFlow(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    pay_time = models.DateField()
    account = models.DecimalField(
        max_digits=11, decimal_places=2, default=0.00)
    capital_type = models.CharField(max_length=50)
    remark = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.project.name + self.section.name + str(self.account)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    project = models.ManyToManyField(Project, through='Permission')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create_time"]


class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    CHOICES = [
        ('Viewing', 'Viewing'),
        ('Editing', 'Editing'),
    ]
    user_permission = models.CharField(max_length=50, choices=CHOICES)
    date_joined = models.DateField()
    def __str__(self):
        return self.user.name + ' | ' +self.project.name


class ProjectInfo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
