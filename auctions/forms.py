from django.forms import ModelForm
from .models import Listing
from .models import Comment
from django import forms
from .models import Bids
from .models import Watchlist

class AddListing(ModelForm):
    class Meta:
        model = Listing 
        fields = ('Name', 'Description', 'Starting_Bid', 'Category_of_Listing', 'image')

class CloseListing(ModelForm):
    class Meta:
        model = Listing 
        fields = ('closed',)

class AddComment(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class AddBids(ModelForm):
    class Meta:
        model = Bids
        fields = ('Bid_Price',)

class Addtowatchlist(ModelForm):
    class Meta:
        model = Watchlist
        fields = '__all__'

