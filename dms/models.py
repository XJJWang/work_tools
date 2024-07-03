from django.db import models
from django.core.validators import MinValueValidator

class Bookshelf(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书架'
        verbose_name_plural = '书架'

class Project(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

class Filebook(models.Model):
    bookshelf = models.ForeignKey(Bookshelf,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name + '   |   ' + self.project.name + '   |   ' + self.bookshelf.name

    class Meta:
        verbose_name = '档案盒'
        verbose_name_plural = '档案盒'



class Document(models.Model):
    filebook = models.ForeignKey(Filebook,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        )
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="请输入大于等于1的正整数",
        default=1,
    )
    principal = models.CharField(max_length=100)
    def __str__(self):
        return self.name + '   |   ' + self.filebook.name + '   |   ' + self.filebook.project.name

    class Meta:
        verbose_name = '文件'
        verbose_name_plural = '文件'

