from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index, name = 'Index'),
    path('ListProduct', views.ShowProduct, name= 'Show'),
    path('ProductDetail/<int:id>', views.ProductDetail, name= 'ProductDetail'),
    path('the-gioi.htm', views.ListTheGioi, name= 'ProductDetail')

]
