from django.conf.urls import include, url
from api import views
from push_notifications.api.rest_framework import GCMDeviceViewSet
from push_notifications.api.rest_framework import APNSDeviceViewSet


urlpatterns = [
    url(r'^device/gcm/?$', GCMDeviceViewSet.as_view({'post': 'create'}), name='create_gcm_device'),
    url(r'^device/apns/?$', APNSDeviceViewSet.as_view({'post': 'create'}), name='create_apns_device'),

    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^attribute/$', views.AttributeList.as_view()),
    url(r'^attribute/(?P<pk>[0-9]+)/$', views.AttributeDetails.as_view()),
    url(r'^attribute/profile/$', views.AttributePost.as_view()),
    url(r'^attribute/profile/(?P<pk>[0-9]+)/$', views.AttributeByProfile.as_view()),
    url(r'^attribute/profile/(?P<pk>[0-9]+)/(?P<name>.+)/$', views.AttributeByProfileDelete.as_view()),
    url(r'^profile/$', views.ProfileList.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)$', views.ProfileDetails.as_view()),
    url(r'^profile/user/$', views.ProfilePost.as_view()),
    url(r'^profile/user/(?P<pk>[0-9]+)$', views.UserProfileList.as_view()),
    url(r'^profile/relation/$', views.MakeRelation.as_view()),
    url(r'^profile/relation/(?P<pk>[0-9]+)/$', views.Relations.as_view()),
    url(r'^profile/relation/user/(?P<pk>[0-9]+)/$', views.RelationsByUser.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),
    url(r'^user/profile/(?P<pk>[0-9]+)/$', views.UserByProfile.as_view()),
    url(r'^user/login/$', views.UserLogin.as_view()),
    url(r'^choices/attributes/$', views.ProfilePossibleAttributes.as_view()),
    url(r'^choices/colors/$', views.ColorsAttributes.as_view()),

]
