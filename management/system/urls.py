from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_gamer, name='view_gamer'),
    path('edit<int:id>', views.edit, name='edit'),
    path('delte<int:id>', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('search_games/', views.search_games, name='search_games'),
    path('gamers', views.games, name='games'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)