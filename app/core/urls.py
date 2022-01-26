"""dashboard_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include


handler404 = "home.views.error_404"
handler500 = "home.views.error_500"
handler403 = "home.views.error_403"
handler400 = "home.views.error_400"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("auth.urls")),
    path("customers/", include("customer.urls")),
    path("purchases/", include("purchase.urls")),
    path("sales/", include("sale.urls")),
    path("schemes/", include("scheme.urls")),
    path("vehicles/", include("vehicle.urls")),
]
