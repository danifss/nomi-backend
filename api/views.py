from rest_framework import generics
from core.models import Attribute, Profile
from core.serializers import AttributeSerializer, ProfileSerializer
from custom_users.models import CustomUser
from custom_users.serializers import CustomUserSerializer

class UserList(generics.ListCreateAPIView):
    """<b>User List</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request):
        """
        Gets every User




        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        return self.list(request)


class AttributeList(generics.ListCreateAPIView):
    """<b>Attribute List</b>"""
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request):
        """
        Gets every Attribute




        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        return self.list(request)


class ProfileList(generics.ListCreateAPIView):
    """ <b>Profile list</b>"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request):
        """
        Gets every Profiles




        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        return self.list(request)

class AttributeByProfile(generics.ListCreateAPIView):
    """ <b>Attribute List by Profile</b> """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request, pk=None):
        """
        Gets every Attribute by Profile




        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            profile = Profile.objects.get(pk = int_pk)
            self.queryset = Attribute.objects.filter(profile=profile)
        except:
            self.queryset = []
        return self.list(request)
