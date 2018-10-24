from django.db import models

# Create your models here.



class FileModel(models.Model):
    file = models.FileField(verbose_name="File")
    spesificCode = models.CharField(max_length=40,verbose_name="Spesific Code")
    counter = models.IntegerField(verbose_name="Number of Download")
    exportDate = models.DateTimeField(auto_now_add=True,verbose_name="Export Date")
    description = models.CharField(verbose_name ="Description",max_length = 50,blank=True, null=True)
    lifetime = models.CharField(verbose_name ="Life Time",max_length = 20,blank=True, null=True)
    

    def __str__(self):
        return self.spesificCode

    def __unicode__(self):
        return 
