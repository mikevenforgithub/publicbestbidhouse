from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    Type_of_Category = models.CharField( max_length=25)
    

    def __str__(self):
        return f"{self.Type_of_Category}"


class Listing(models.Model):
    Name = models.CharField(max_length=25)
    Description = models.CharField(max_length=500) 
    Starting_Bid = models.IntegerField()
    Category_of_Listing = models.ForeignKey(Categories, related_name="category", on_delete= models.CASCADE)
    Listed_by = models.ForeignKey(User, blank=True, default=1, related_name="Listed_by", on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to= "images/")
    
    
       
    def __str__(self):
        return f"{self.Name} - Starting Bid at {self.Starting_Bid}"

class Bids(models.Model):
    Bid_Price = models.IntegerField(blank=True)   
    Bid_on = models.CharField(max_length=25, null=True)
    bid_by = models.CharField(max_length=25, null=True, blank=True, default=0)

    def __str__(self):
        return f"Bid of {self.Bid_Price}"

class Comment(models.Model):
    comment = models.CharField(max_length=150)
    listing = models.CharField(max_length=25, null=True)
    Date_of_Comment = models.DateTimeField(auto_now_add=True, blank=True)
    comment_by = models.CharField(max_length=25, null=True, blank=True, default=0)

    def __str__(self):
        return f"Comment on the {self.Date_of_Comment}"

class Watchlist(models.Model):
    ofuser = models.ForeignKey(User, blank=True, default=1, related_name="ofuser", on_delete=models.CASCADE)
    listings = models.ForeignKey(Listing, blank=True, default=1, related_name="listings", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listings.Name}"

class Logo(models.Model):
    name = models.CharField(max_length=150)
    logo = models.FileField(upload_to='media/images')

    def __str__(self):
        return f"{self.name}"

