"""cafesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views as shop_views
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from shop.views import ReviewDetail , ReviewCreate , ReviewUpdate , ReviewDelete , BillingCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',shop_views.index,name='index'),
    path('<int:id>/',shop_views.detail,name='detail'),
    path('checkout/',shop_views.checkout,name='checkout'),
    path('myorders/',shop_views.myorders,name='myorders'),
    path('order/<int:id>/',shop_views.order_details,name='order_details'),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', users_views.profile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/reset_password_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/reset_password_confirm.html'),
         name='password_reset_confirm'),
    path('review/', shop_views.reviews, name='reviews'),
    path('receipt/<int:id>/', shop_views.receipt, name="receipt"),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
    path('review/new/', ReviewCreate.as_view(), name='review-create'),
    path('billing/', BillingCreate.as_view(), name='billing'),
    path('review/update/<int:pk>/', ReviewUpdate.as_view(), name='review-update'),
    path('review/delete/<int:pk>/', ReviewDelete.as_view(), name='review-delete'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
