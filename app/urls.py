from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView 


urlpatterns = [
    path('',views.home, name='home'),
    path('adminuser/', views.adminhome, name='adminhome'),
    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('deleteproduct/<int:skuproduct>/', views.deleteproduct, name='deleteproduct'),
    path('editproduct/<int:skuproduct>/', views.editproduct, name='editproduct'),
    path('seller/', views.sellerhome, name='sellerhome' ),
    path('addsale/<int:sku>/', views.seller_addsale, name='seller_addsale'),
    path('quitsale/<int:sku>/', views.seller_quitproduct, name='seller_quitproduct'),
    path('makesale/', views.make_sale, name="make_sale"),
    path('cleansale/', views.clean_sale, name="clean_sale"),
]




