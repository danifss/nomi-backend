from django.conf.urls import include, url
from api import views

urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^attribute/$', views.AttributeList.as_view()),

    url(r'^profile/$', views.ProfileList.as_view()),

    url(r'^attributeByProfile/(?P<pk>.+)/$', views.AttributeByProfile.as_view()),
]
