import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from dtb.views import TelegramBotWebhookView, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', index, name="index"),
    path('super_secter_webhook/', csrf_exempt(TelegramBotWebhookView.as_view())),
]
