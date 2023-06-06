from . import views
from django.urls import path
app_name='shop_app'
urlpatterns = [
    path('', views.all_category, name='all_category'),
    path('<slug:cat_slug>/', views.all_category, name="product_category"),
    path('<slug:cat_slug>/<slug:product_slug>/', views.pro_detail, name="product_detail")

]
