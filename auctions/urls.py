from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addlisting", views.addlisting, name="addlisting"),
    path("comment", views.comment, name="comment"),
    path("categories/", views.categories, name="categories"),
    path("error", views.error, name="error"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("<str:Name>", views.listing, name="listing"),
    path("watchlist/<str:Name>", views.listing, name="listing"),
    path("categories/<str:category>/", views.catsearch, name="catsearch"),
    path("addwatch/<str:Name>", views.addwatchlist, name="addwatchlist"),
    path("closelisting/<str:Name>", views.closelisting, name="closelisting"),
    path("delete/<str:Name>", views.removefromwatchlist, name="removefromwatchlist"),
    path("comment/<str:Name>", views.comment, name="comment"),
    path("watchlist/delete/<str:Name>", views.removefromwatchlist, name="removefromwatchlist")   
]
