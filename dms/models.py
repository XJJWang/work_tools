from django.db import models
from django.core.validators import MinValueValidator

class Bookshelf(models.Model):
    name = models.CharField(max_length=50, verbose_name="书架")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书架'
        verbose_name_plural = '书架'

class Cell(models.Model):
    bookshelf = models.ForeignKey(Bookshelf,on_delete=models.CASCADE, max_length=50, verbose_name="书架")
    name = models.CharField(max_length=50, verbose_name="格子")

    def __str__(self):
        return self.bookshelf.name + self.name

    class Meta:
        verbose_name = '格子'
        verbose_name_plural = '格子'

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="项目名")
    year = models.CharField(max_length=4, verbose_name="项目年份")
    intro = models.TextField(verbose_name="项目简介",null=True, blank=True)
    short_name = models.CharField(max_length=50, verbose_name="项目简称")
    def __str__(self):
        return self.short_name if self.short_name else self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

class Filebook(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE, max_length=50, verbose_name="格子")
    project = models.ForeignKey(Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="项目名",
        )
    name = models.CharField(max_length=200, verbose_name="档案盒名字")
    put_in_date =  models.DateField(auto_now_add=False, verbose_name="入库时间")
    remark = models.CharField(max_length=200, null=True, blank=True, verbose_name="备注")
    def __str__(self):
        return self.name + '   |   ' + self.project.name + '   |   ' + self.cell.bookshelf.name + self.cell.name

    class Meta:
        verbose_name = '档案盒'
        verbose_name_plural = '档案盒'



class Document(models.Model):
    filebook = models.ForeignKey(Filebook,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        max_length=200, verbose_name="档案盒",
        )
    name = models.CharField(max_length=200, verbose_name="文件名")
    put_in_amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="请输入大于等于1的正整数",
        default=1,
        verbose_name="入库份数"
    )
    amount_now = models.PositiveIntegerField(verbose_name="库存")
    principal = models.CharField(max_length=100, verbose_name="交接人")
    remark = models.CharField(max_length=200, null=True, blank=True, verbose_name="备注")
    put_in_date =  models.DateField(auto_now_add=False,  verbose_name="入库时间", null=True, blank=True)
    short_name = models.CharField(max_length=50, verbose_name="文件简称", blank=True, null=True)
    def __str__(self):
       
        
        if self.short_name:
            name = self.short_name
        else:
            name = self.name
        return name + '   |   ' + self.filebook.name + '   |   ' + self.filebook.project.short_name



    class Meta:
        verbose_name = '文件'
        verbose_name_plural = '文件'

