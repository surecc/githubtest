from django.db import models

# Create your models here.

# the category of the commidities
class Category(models.Model):
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=1)
    coding = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'%s_%s' %(self.name, self.gender)
    
    class Meta:
        ordering = ['coding']

# the sellers of the commidities
class Seller(models.Model):
    domain = models.URLField(blank=True)
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

# the detail of commidities 
class Commidity(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    price = models.FloatField()
    desc = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)
    sellers = models.ForeignKey(Seller)
    
    def __unicode__(self):
        return u'%s:%s' %(self.name, self.price)
    
    class Meta:
        ordering = ['name']

# the details of the Pictures
class Picture(models.Model):
    dir = models.FilePathField()
    size = models.FloatField(blank=True)
    height = models.IntegerField(blank=True)
    width = models.IntegerField(blank=True)
    var_total = models.IntegerField(blank=True)
    var1 = models.FloatField(blank=True)
    var2 = models.FloatField(blank=True)
    var3 = models.FloatField(blank=True)
    var4 = models.FloatField(blank=True)
    var5 = models.FloatField(blank=True)
    in_time = models.DateTimeField(blank=True)
    commidities = models.ForeignKey(Commidity)
    
    def __unicode__(self):
        return self.var_total
    
    class Meta:
        ordering = ['in_time']