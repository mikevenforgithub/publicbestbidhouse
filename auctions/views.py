from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User
from .models import Listing
from .models import Bids
from .models import Categories
from .models import Comment
from .models import Watchlist
from .models import Logo
from .forms import AddListing
from .forms import AddComment
from .forms import AddBids
from .forms import Addtowatchlist
from .forms import CloseListing

def index(request):

    l = Logo.objects.filter(name="bbb").first()
    return render(request, "auctions/index.html", {
    "listings": Listing.objects.all(),
    "categories": Categories.objects.all(),
    "logo": l.logo
    })


def login_view(request):
    l = Logo.objects.filter(name="bbb").first()
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html",{
            "logo": l.logo
        })


def logout_view(request):
    
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    l = Logo.objects.filter(name="bbb").first()
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html",{
            "logo": l.logo
        })


def addlisting(request):
    l = Logo.objects.filter(name="bbb").first()
    form = AddListing()
    if request.method == "POST":
        form = AddListing(request.POST, request.FILES)
        if form.is_valid():
            newlist = form.save(commit=False)
            newlist.Listed_by = request.user
            newlist.save()
            return render(request, "auctions/index.html", {
                "listings": Listing.objects.all(),
                "categories": Categories.objects.all(),
                "logo": l.logo
                })
    else:
        return render(request, "auctions/addlisting.html", {
            'form':form,
            "categories": Categories.objects.all(),
            "logo": l.logo
            })
    

def categories(request):
    l = Logo.objects.filter(name="bbb").first()
    return render(request, "auctions/categories.html", {
    "categories": Categories.objects.all(),
    "logo": l.logo
    })

def catsearch(request, category):
    l = Logo.objects.filter(name="bbb").first()
    catx = Categories.objects.filter(Type_of_Category=category).first()
    cat_v = catx.id
    listx = Listing.objects.filter(Category_of_Listing=cat_v)
    li = len(listx)
    return render(request,"auctions/catsearch.html",{
        "listings":listx,
        "category":category, 
        "categories": Categories.objects.all(),   
        "l": li,
        "logo": l.logo
    })


def listing(request, Name):
    l = Logo.objects.filter(name="bbb").first()
    listing = Listing.objects.filter(Name=Name).first()
    comf = Comment.objects.filter(listing=Name)
    bids = Bids.objects.filter(Bid_on=Name).all()
    highestbid = bids.order_by("Bid_Price").last()
    user = request.user
    usercur = User.objects.filter(username=user).first()
    watchlist = Watchlist.objects.filter(ofuser=usercur)
    form = AddBids()
    formc = AddComment()
    if request.method == "POST":
        form = AddBids(request.POST)
        if form.is_valid():
            newbid = form.save(commit=False)
            newbid.Bid_on = Name
            newbid.bid_by = request.user 
            if int(str(newbid.Bid_Price)) >= int(str(listing.Starting_Bid)):
                if highestbid is None: 
                    newbid.save()
                    return render(request, "auctions/index.html", {
                    "listings": Listing.objects.all(),
                    "categories": Categories.objects.all(),
                    "logo": l.logo
                    })
                elif int(str(newbid.Bid_Price)) >= int(str(highestbid.Bid_Price)): 
                        newbid.save()
                        return render(request, "auctions/index.html", {
                        "listings": Listing.objects.all(),
                        "categories": Categories.objects.all(),
                        "logo": l.logo
                        })
                else:
                    return render(request, "auctions/listing.html", {
                            "comments": comf,    
                            "listing": listing,
                            "Name":Name,
                            "currentbid":highestbid,
                            "form":form,
                            "Message": "Your Bid is too low !",
                            "watchlist":watchlist,
                            "formc" : formc,
                            "categories": Categories.objects.all(),  
                            "logo": l.logo
                            })
            else:
                return render(request, "auctions/listing.html", {
                        "comments": comf,    
                        "listing": listing,
                        "Name":Name,
                        "currentbid":highestbid,
                        "form":form,
                        "Message": "Your Bid is too low !",
                        "watchlist":watchlist,
                        "formc" : formc,
                        "categories": Categories.objects.all(),  
                        "logo": l.logo
                        })
    else:
        return render(request, "auctions/listing.html", {
        "comments": comf,    
        "listing": listing,
        "Name":Name,
        "currentbid":highestbid,
        "form":form,
        "user":user,
        "watchlist":watchlist,
        "formc" : formc,
        "categories": Categories.objects.all(),
        "logo": l.logo  
        })
 
def comment(request, Name):
    l = Logo.objects.filter(name="bbb").first()
    form = AddComment()
    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.comment_by = request.user
            newcomment.listing = Name
            newcomment.save()
            return render (request, "auctions/index.html", {
                "listings": Listing.objects.all(),
                "categories": Categories.objects.all(),
                "logo": l.logo
                })

    else:
        return render(request, "auctions/comment.html", {
            'form':form,
            "categories": Categories.objects.all(),
            "logo": l.logo
            })



def error(request):
    return render (request, "auctions/error.html")


def watchlist(request):
    l = Logo.objects.filter(name="bbb").first()
    user = request.user.username
    usercur = User.objects.filter(username=user).first()
    watchlist = Watchlist.objects.filter(ofuser=usercur.id)
    li = len(watchlist)
    return render (request, "auctions/watchlist.html",{
        "watchlist": watchlist,
        "categories": Categories.objects.all(),
        "l":li,
        "logo": l.logo

    })

def removefromwatchlist(request, Name):
    l = Logo.objects.filter(name="bbb").first()
    if request.method == "POST":
        form = Addtowatchlist(request.POST)
        if form.is_valid():
            user1 = request.user.username
            usercur = User.objects.filter(username=user1).first()
            item = Listing.objects.filter(Name=Name).first()
            userwatchitemdel = Watchlist.objects.filter(ofuser=usercur, listings=item).delete()
            return render (request, "auctions/index.html", {
                        "listings": Listing.objects.all(),
                        "categories": Categories.objects.all(),
                        "logo": l.logo
                        })


def addwatchlist(request, Name):
    l = Logo.objects.filter(name="bbb").first()
    if request.method == "POST":
        form = Addtowatchlist(request.POST)
        if form.is_valid():
            user1 = request.user.username
            usercur = User.objects.filter(username=user1).first()
            liss = Listing.objects.filter(Name=Name).first()
            watch = Watchlist.objects.filter(ofuser=usercur)
            if liss.Name not in watch:
                newwatch = Watchlist.objects.create(ofuser=usercur,listings=liss)
                return render (request, "auctions/index.html", {
                        "listings": Listing.objects.all(),
                        "categories": Categories.objects.all(),
                        "logo": l.logo
                        })  
            if liss.Name in watch:
                return render (request, "auctions/watchlist.html",{
                    "watchlist": watch,
                    "categories": Categories.objects.all(),
                    "logo": l.logo
                })  


def closelisting(request, Name):
    l = Logo.objects.filter(name="bbb").first()
    if request.method == "POST":
        form = CloseListing(request.POST)
        if form.is_valid():
            liss = Listing.objects.filter(Name=Name).first()
            liss.closed = True
            liss.save()
            return render(request, "auctions/index.html", {
                "listings": Listing.objects.all(),
                "categories": Categories.objects.all(),
                "logo": l.logo
                })
