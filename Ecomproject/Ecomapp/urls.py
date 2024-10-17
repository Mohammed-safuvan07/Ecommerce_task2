from django.urls import path,include

from Ecomapp import views
app_name='Ecomapp'
urlpatterns = [

    path('',views.AllProdCat,name='AllProdCat'),
    path('<slug:c_slug>/',views.AllProdCat,name='products_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdDetail,name='ProdDetails'),
]