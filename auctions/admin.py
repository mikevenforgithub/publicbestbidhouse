from django.contrib import admin

from .models import Listing
from .models import Bids
from .models import Categories
from .models import Comment
from .models import Watchlist

# Register your models here.
admin.site.register(Listing)
admin.site.register(Bids)
admin.site.register(Categories)
admin.site.register(Comment)
admin.site.register(Watchlist)

