from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('suppliers/', views.suppliers_view, name='suppliers'),
    path('brands/', views.brands_view, name='brands'),
    path('products/', views.products_view, name='products'),

    path("list_users/", views.list_users, name="list_users"),
]
