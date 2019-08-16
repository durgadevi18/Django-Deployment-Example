from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns=[

    url('relative_url_templates/',views.relative_url_templates,name='relative_url_templates'),
    url('other/',views.other,name='other'),

]
