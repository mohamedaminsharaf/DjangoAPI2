from django.db import models

class user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    
    
    def __str__(self):
        return self.name + ' , ' + self.email
    
    
class Nokta(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    nokta = models.CharField(max_length= 200)
    vote = models.SmallIntegerField(null=True)
    
    
    
    def __str__(self):
        v = str(self.vote)
        return self.nokta+ " , " + v
    