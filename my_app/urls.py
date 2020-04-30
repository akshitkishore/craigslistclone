from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
#path('admin/', admin.site.urls),
path('', views.home, name='home'),
path('new_search', views.new_search, name='new_search'),

]