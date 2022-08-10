from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timezone, timedelta

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
       return self.name

    def get_last_post(self):
        return Jobs.objects.filter(group__name=self).order_by('-last_update').first() #group__name is defining relationship in  Jobs and Product model
    
    def natural_key(self):
        return(self.name)

class Jobs(models.Model):

    Request_For_Quotation = models.CharField(max_length=150)
    product = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    budget = models.DecimalField(decimal_places=2, max_digits=65)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    group = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='jobs')
    period = models.PositiveIntegerField(default='Days')
    last_update = models.DateTimeField(auto_now_add=True)
    applicants = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.product

     
    #function that take job created date and subtract it with current date, then compare the difference to 31 days
        

    def get_date_diff(self):
        date = self.last_update
        now = datetime.now(timezone.utc) #get current date in your time zone
        difference = now - date
        '''
        Compare created date with 31 days 
        '''
        if (difference <= timedelta(days=31)):
            result = True
        else:
            result = False
        

        return result
        
    def natural_key(self):

        dicti = {
                 "Product Id": self.id,
                 "Client": self.client.natural_key(),
                 "Group product": self.group.natural_key(),
                 "Product name": self.product,
                 "Requirements": self.description,
                 "Delivery period": self.period,
                 "Created data": self.last_update
                }
        return dicti



class Apply(models.Model):
    
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE, related_name='supplier')
    zimra = models.FileField(upload_to='uploads')
    praz = models.FileField(upload_to='uploads')
    quotation = models.FileField(upload_to='uploads', default='quotation')
    clients = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier')
    applied = models.DateField(auto_now_add=True)
    zimra_date = models.CharField(max_length=20, default='invalid') 
    praz_date = models.CharField(max_length=10, default='invalid')
    doc_validity = models.CharField(max_length=22, default='Invalid documents')
    suppliers = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    
    def natural_key(self):

        return(self.jobs.natural_key(),) 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    address = models.CharField(max_length=75, null=True)
    contacts = models.CharField(max_length=30, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



    
        


