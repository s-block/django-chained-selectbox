from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^chainedselectchoices$',
        views.ChainedSelectChoices.as_view(),
        name = 'chained_select_choices'
    ),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
