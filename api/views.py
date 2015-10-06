from rest_framework import generics
from core.models import Attribute, Profile, ATTRS
from core.serializers import AttributeSerializer, ProfileSerializer
from custom_users.models import CustomUser
from custom_users.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status


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


class UserDetails(generics.ListCreateAPIView):
    """<b>User</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request, pk=None):
        """
        Gets User with specified id




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
            self.queryset = self.queryset.filter(pk=int_pk)
        except:
            self.queryset = []
        return self.list(request)


class UserByProfile(generics.ListCreateAPIView):
    """<b>User</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request, pk=None):
        """
        Gets User which the given profile belongs to




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
            profile = Profile.objects.get(pk=int_pk)
            self.queryset = self.queryset.filter(pk=profile.user.id)
        except:
            self.queryset = []
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


class AttributeDetails(generics.ListCreateAPIView):
    """ <b>Attribute Details</b> """
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
        Gets Attribute by given id




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
            self.queryset = self.queryset.filter(pk=int_pk)
        except:
            self.queryset = []
        return self.list(request)


class Relations(generics.ListCreateAPIView):
    """ <b>Relations by Profile</b> """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request, pk=None):
        """
        Gets every Connections by Profile




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
            self.queryset = profile.connections.all()
        except:
            self.queryset = []
        return self.list(request)


class UserProfileList(generics.ListCreateAPIView):
    """ <b>Profiles for user</b> """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request, pk=None):
        """
        Gets every Profile of a given user




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
            user = CustomUser.objects.get(pk = int_pk)
            self.queryset = self.queryset.filter(user=user)
        except:
            self.queryset = []
        return self.list(request)


class ProfileDetails(generics.ListCreateAPIView):
    """ <b>Profiles for user</b> """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request, pk=None):
        """
        Gets Profile for given id




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
            self.queryset = self.queryset.filter(pk=int_pk)
        except:
            self.queryset = []
        return self.list(request)


class ProfilePossibleAttributes(generics.ListCreateAPIView):
    """<b>Possible Attributes List</b>"""
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
        Gets every possible attribute for user to insert into his profile




        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        resp = {}
        for a in ATTRS:
            resp[a[0]] = a[1]
        return Response(resp, status=status.HTTP_200_OK)
