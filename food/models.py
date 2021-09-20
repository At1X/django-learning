from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
#start food category
class myManagers(models.Manager):
    def published(self):
        return self.filter(auth='Narges')


class category(models.Model):
    parent = models.ForeignKey('self',null=True, default=None, blank=True,  on_delete=models.SET_NULL, related_name='children')
    name = models.CharField(max_length=10)
    theslg = models.SlugField(max_length=10)
    check = models.BooleanField(default=False, verbose_name= 'آیا اجازه دارید؟')

    class Meta:
        verbose_name= 'گروه'
        verbose_name_plural = 'گروه‌ها'
        ordering = ('parent__id',)

    def __str__(self):
        return self.name

#end food category
class foodArgus(models.Model):
    FOOD_RATE = (
        ('Best', (
        ('1','1'),
        ('2','2'),
        ('3','3'),
         )),
        ('Nice', (
        ('4','4'),
        ('5','5'),
        ))
    )
    USERS = {
        ('Atid','Atid'),
        ('Narges', 'Narges'),
        ('Yasin', 'Yasin'),
        ('Ardalan', 'Ardalan'),
    }
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    desc = models.TextField()
    rate = models.CharField(max_length=1, choices=FOOD_RATE)
    auth = models.CharField(max_length=10, choices=USERS)
    group = models.ManyToManyField(category, related_name='articles')
    date = models.DateTimeField(default=timezone.now)
    pic = models.ImageField(upload_to= 'foodpics/')

    class Meta:
        verbose_name = "غذا"
        verbose_name_plural = "غذاها"

    def __str__(self):
        return self.name
    def showornot(self):
        return self.group.filter(check=True)
    objects = myManagers()
# Create your models here.
