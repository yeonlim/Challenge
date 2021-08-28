from django.contrib import admin
from django.urls import path, include
import challenge.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', challenge.views.calendar_view, name="calendar"),
    path('event/new/', challenge.views.event, name="event"),
    path('event/edit/<int:event_id>', challenge.views.event, name="edit"),
  
    path('community/', include('community.urls')),
    path('chatting/', include('chatting.urls')),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)