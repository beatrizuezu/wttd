from django.conf.urls import url
from django.contrib import admin
from eventex.core import views as eventex_views
from eventex.subscriptions.views import subscribe


urlpatterns = [
	url(r'^$', eventex_views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^inscricao/$',subscribe)
]
