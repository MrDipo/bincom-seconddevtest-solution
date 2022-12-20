"""resultsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include
# from dashboard import views
from django.views.generic import RedirectView # permanent redirect to project root
from django.conf import settings # for serving static files
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pu-single/', views.pu_single)
]

# using app urlconf to specify urls instead
urlpatterns += [
    path('dashboard/', include('dashboard.urls')),
]

# permanently redirect to app view first
# urlpatterns += [
#     path('', RedirectView.as_view(url='dashboard/pu-single/', permanent=True)),
# ]

# allow django serve static doucments
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
