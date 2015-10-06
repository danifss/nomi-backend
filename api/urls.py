from django.conf.urls import include, url
from api import views

urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^attribute/$', views.AttributeList.as_view()),
    url(r'^attribute/(?P<pk>[0-9+])/$', views.AttributeDetails.as_view()),
    url(r'^attribute/profile/(?P<pk>[0-9+])/$', views.AttributeByProfile.as_view()),
    url(r'^profile/$', views.ProfileList.as_view()),
    url(r'^profile/(?P<pk>[0-9+])$', views.ProfileDetails.as_view()),
    url(r'^profile/user/(?P<pk>[0-9+])$', views.UserProfileList.as_view()),
    url(r'^profile/relation/(?P<pk>[0-9+])/$', views.Relations.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9+])/$', views.UserDetails.as_view()),
    url(r'^user/profile/(?P<pk>[0-9+])/$', views.UserByProfile.as_view()),
    url(r'^possible-attributes/$', views.ProfilePossibleAttributes.as_view()),

]
