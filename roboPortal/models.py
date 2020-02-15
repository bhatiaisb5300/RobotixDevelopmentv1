from django.db import models
from django.contrib.auth.models import User
class portalUser(models.Model):
    user = models.OneToOneField(User,related_name="portal",on_delete= models.CASCADE)
    verified = models.BooleanField(default= False)
    resume = models.FileField(null= True, blank= True)
    description = models.TextField(blank= True,null= True)
    joined_team = models.BooleanField(default= False)
    user_team_id = models.IntegerField(blank= True, null= True)
    is_admin = models.BooleanField(default= False)#team admin
    is_member = models.BooleanField(default= False)#robotics team member
    def __str__(self):
        return self.user.username + " extended portalUser class"
class UserLink(models.Model):
    link = models.ForeignKey(User, on_delete= models.CASCADE)
class Token(models.Model):
    token = models.CharField(max_length=150)
class Team(models.Model):
    name = models.CharField(blank = True, null= True, max_length= 150)
    admin = models.OneToOneField(User, related_name= "leader", on_delete = models.CASCADE)
    member= models.ManyToManyField(User, related_name= "member")
    token = models.CharField(max_length= 100,null= True, blank= True)
    selected = models.BooleanField(default= False)
    def __str__(self):
        return "Team" + self.name 
# Create your models here.
