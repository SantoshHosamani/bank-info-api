from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class Branch(models.Model):
    name = models.CharField(max_length=256)  
    ifsc = models.CharField(max_length=500, unique=True)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE,)
    address = models.TextField()
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
 
       
    def __str__(self):
        return "{} - {} - {} - {} - {} - {}- {}".format(self.ifsc,self.name, self.bank,self.address, self.city,self.district,self.state)
        
