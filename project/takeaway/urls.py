"""takeaway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from core.authn.views.views import login_user, logout_user

urlpatterns = [
    path('django-admin/', admin.site.urls),
    re_path(r'^', include(('core.company.urls.root', 'company'))),
    re_path(r'^login/$', login_user, name='login'),
    re_path(r'^logout/$', logout_user, name='logout'),
    re_path(r'^product/', include(('core.product.urls.root', 'product'))),
    re_path(r'^cart/', include(('core.cart.urls.root', 'cart'))),
    re_path(r'^restaurant/', include(('core.restaurant.urls.root', 'restaurant'))),
    re_path(r'^user/', include(('core.user.urls.root', 'user'))),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

