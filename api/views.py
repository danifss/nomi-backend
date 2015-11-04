from rest_framework import generics
from core.models import Attribute, Profile, ATTRS, COLORS
from core.serializers import AttributeSerializer, ProfileSerializer, RelationSerializer
from custom_users.models import CustomUser
from custom_users.serializers import CustomUserSerializer
from httplib import HTTPResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from push_notifications.models import GCMDevice
import json


class UserLogin(generics.ListCreateAPIView):
    """<b>User Login</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get']

    def get(self, request):
        """
        Gets user id if credentials are correct




        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        - 400 BAD REQUEST

        email -- registration email
        password -- registration password
        ---
        omit_parameters:
        - form
        """
        if 'password' in request.GET and 'email' in request.GET:
            try:
                user = CustomUser.objects.get(email__iexact = request.GET.get('email'))
                if user.check_password(request.GET.get('password')):
                    return Response(status=status.HTTP_200_OK, data={'id': user.id, 'first_name': user.first_name,
                                                                     'last_name': user.last_name})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            except:
                pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListCreateAPIView):
    """<b>User List</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get', 'post']
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

    @csrf_exempt
    def post(self, request):
        """
        Creates a User




        <b>Details</b>

        METHODS : POST




        <b>Example:</b>


        {

            "email": "123qwe@gmail.com",

            "password": "123qwe",

            "first_name": "Ivo",

            "last_name": "Silva"

        }



        <b>RETURNS:</b>

        - 200 OK.



        ---
        omit_parameters:
            - form
        """

        # passwords are sent in clear text
        # in need of ssl or to send already hashed passwords

        #{
        #    "email": "ivopintodasilva@gmail.com",
        #    "password": "123qwe",
        #    "first_name": "Ivo",
        #    "last_name": "Silva"
        #}

        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        # print request.META

        if 'password' in request.data\
                and 'first_name' in request.data and 'last_name' in request.data \
                and 'email' in request.data:
            #password = request.data['password']
            try:
                latest_id = CustomUser.objects.latest('id').id + 1
            except:
                latest_id = 0

            request.data['username'] = str(latest_id)
            #username = request.data['username']

            request.data['is_active'] = True
            print request.data

            #serializer = self.serializer_class(data=request.data)
            #if serializer.is_valid():
            #    serializer.save()
            #    user = CustomUser.objects.get(username=username)
            #    user.set_password(password)
            #    user.save()
            #    return Response(status=status.HTTP_200_OK)
            #print 'serializer not valid'

            try:
                CustomUser.objects.get(email = str(request.data['email']))
                return Response(status=status.HTTP_401_UNAUTHORIZED, data='Email is already registered.')
            except:
                try:
                    new_user = CustomUser.objects.create(username=str(request.data['username']), email = str(request.data['email']), first_name = request.data['first_name'], last_name = request.data['last_name'])
                    new_user.set_password(str(request.data['password']))
                    new_user.save()
                    return Response(status=status.HTTP_200_OK, data={'id': new_user.id})
                except:
                    pass

        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetails(generics.ListCreateAPIView):
    """<b>User</b>"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    allowed_methods = ['get', 'delete', 'put']
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

    def delete(self, request, pk=None):
        """
        Delete User with specified id




        <b>Details</b>

        METHODS : DELETE



        <b>RETURNS:</b>

        - 200 OK.

        - 404 NOU FOUND.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            self.queryset = self.queryset.get(pk=int_pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def put(self, request, pk=None):
        """
        Edits a User




        <b>Details</b>

        METHODS : PUT




        <b>Example:</b>


        {

            "email": "123qwe@gmail.com",

            "password": "123qwe",

            "first_name": "Ivo",

            "last_name": "Silva"

        }



        <b>RETURNS:</b>

        - 200 OK.

        - 404 BAD REQUEST.



        ---
        omit_parameters:
            - form
        """

        # passwords are sent in clear text
        # in need of ssl or to send already hashed passwords

        #{
        #    "email": "ivopintodasilva@gmail.com",
        #    "password": "123qwe",
        #    "first_name": "Ivo",
        #    "last_name": "Silva"
        #}

        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        #print request.META

        try:
            int_pk = int(pk)
            user = self.queryset.get(pk=int_pk)


            if 'password' in request.data:
                user.set_password(request.data['password'])
            if 'email' in request.data:
                user.email = request.data['email']
            if 'first_name' in request.data:
                user.first_name = request.data['first_name']
            if 'last_name' in request.data:
                user.last_name = request.data['last_name']
            user.save()

            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


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


class AttributePost(generics.ListCreateAPIView):
    """<b>Attribute List</b>"""
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    allowed_methods = ['post']

    @csrf_exempt
    def post(self, request):
        """
        Creates an Attribute and adds to profile




        <b>Details</b>

        METHODS : POST




        <b>Example:</b>


        {

            "name": "FACEBOOK",

            "value": "123qwe",

            "profile": 1

        }



        <b>RETURNS:</b>

        - 200 OK.



        ---
        omit_parameters:
            - form
        """


        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        #print request.META

        if 'name' in request.data and 'value' in request.data \
                and 'profile' in request.data:
            profile_pk = request.data['profile']
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                profile = Profile.objects.get(pk=profile_pk)
                profile.attributes.add(obj)

                users_to_notify = []
                for p in profile.connections.all():
                    users_to_notify += [p.user]
                devices = GCMDevice.objects.all().filter(user__in=users_to_notify)
                devices.send_message(ProfileSerializer(profile).data)

                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


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


class ProfilePost(generics.ListCreateAPIView):
    """ <b>Profile Post</b>"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    allowed_methods = ['post']

    @csrf_exempt
    def post(self, request):
        """
        Creates a Profile and adds to user




        <b>Details</b>

        METHODS : POST




        <b>Example:</b>


        {

            "name": "Pessoal",

            "user": 1,

            "color": "RED"

        }



        <b>RETURNS:</b>

        - 200 OK.



        ---
        omit_parameters:
            - form
        """


        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        #print request.META
        try:
            if 'name' in request.data and 'user' in request.data \
                    and 'color' in request.data:

                profile = Profile.objects.create(
                    name=request.data['name'],
                    user=CustomUser.objects.get(pk=request.data['user']),
                    color=request.data['color']
                )
                return Response(status=status.HTTP_200_OK, data = ProfileSerializer(profile).data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AttributeByProfileDelete(generics.ListCreateAPIView):
    """ <b>Attribute List by Profile</b> """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    allowed_methods = [ 'delete',]

    def delete(self, request, pk=None, name=None):
        """
        Deletes Attribute from Profile




        <b>Details</b>

        METHODS : DELETE



        <b>Example:</b>







        <b>RETURNS:</b>

        - 200 OK.

        - 400 NOT FOUND.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            profile = Profile.objects.get(pk=int_pk)
            attributes = profile.attributes.all()

            for attribute in attributes:
                if attribute.name == name:
                    profile.attributes.remove(attribute)
                    profile.save()
                    return Response(status=status.HTTP_200_OK, data=ProfileSerializer(profile).data)

            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AttributeByProfile(generics.ListCreateAPIView):
    """ <b>Attribute List by Profile</b> """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    allowed_methods = ['get', 'put']
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




    @csrf_exempt
    def put(self, request, pk=None):
        """
        Edits an Attribute of a given profile




        <b>Details</b>

        METHODS : PUT




        <b>Example:</b>


        {

            "name": "FACEBOOK",

            "value": "facebook.com/daniel"


        }



        <b>RETURNS:</b>

        - 200 OK.

        - 404 BAD REQUEST.



        ---
        omit_parameters:
            - form
        """

        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        #print request.META

        try:
            int_pk = int(pk)
            profile = Profile.objects.get(pk=int_pk)
            attributes = profile.attributes.all()

            if 'name' in request.data and 'value' in request.data:
                for attribute in attributes:
                    if attribute.name == request.data['name']:
                        attribute.value = request.data['value']
                        attribute.save()

                        users_to_notify = []
                        for p in profile.connections.all():
                            users_to_notify += [p.user]
                        devices = GCMDevice.objects.all().filter(user__in=users_to_notify)
                        devices.send_message(ProfileSerializer(profile).data)
                        return Response(status=status.HTTP_200_OK, data=AttributeSerializer(attribute).data)

            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AttributeDetails(generics.ListCreateAPIView):
    """ <b>Attribute Details</b> """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    allowed_methods = ['get', 'delete', 'put']
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

    def delete(self, request, pk=None):
        """
        Delete Attribute by given id




        <b>Details</b>

        METHODS : DELETE



        <b>RETURNS:</b>

        - 200 OK.

        - 404 NOT FOUND.

        ---
        omit_parameters:
        - form
        """
        try:
            int_pk = int(pk)
            self.queryset = self.queryset.get(pk=int_pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def put(self, request, pk=None):
        """
        Edits an Attribute




        <b>Details</b>

        METHODS : PUT




        <b>Example:</b>


        {

            "name": "FACEBOOK",

            "value": "facebook.com/daniel"


        }



        <b>RETURNS:</b>

        - 200 OK.

        - 404 BAD REQUEST.



        ---
        omit_parameters:
            - form
        """

        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        #print request.META

        try:
            int_pk = int(pk)
            attribute = self.queryset.get(pk=int_pk)

            if 'name' in request.data:
                attribute.name = request.data['name']
            if 'value' in request.data:
                attribute.value = request.data['value']
            attribute.save()

            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


class Relations(generics.ListCreateAPIView):
    """ <b>Relations by Profile</b> """
    queryset = Profile.objects.all()
    serializer_class = RelationSerializer
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


class RelationsByUser(generics.ListCreateAPIView):
    """ <b>Relations by User</b> """
    queryset = Profile.objects.all()
    serializer_class = RelationSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request, pk=None):
        """
        Gets every Connections for a given user




        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """

        resp = []

        try:
            int_pk = int(pk)
            user = CustomUser.objects.get(pk=int_pk)
            user_profiles = Profile.objects.filter(user=user)
            for p in user_profiles:
                for connect in p.connections.all():
                    if connect.user != user:
                        print connect
                        resp += [connect]
            self.queryset = resp
        except:
            self.queryset = []
        return self.list(request)


class MakeRelation(generics.ListCreateAPIView):
    """ <b>Relation between profiles</b> """
    queryset = Profile.objects.all()
    serializer_class = RelationSerializer
    allowed_methods = ['put', 'delete']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    @csrf_exempt
    def put(self, request):
        """
        Creates a Relation between two profiles




        <b>Details</b>

        METHODS : PUT




        <b>Example:</b>


        {

            "profileId1": 1,

            "profileId2": 3

        }



        <b>RETURNS:</b>

        - 200 OK.



        ---
        omit_parameters:
            - form
        """

        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        # print 'X-CSRFToken: '+request.META["CSRF_COOKIE"]
        # print request.data


        if 'profileId1' in request.data and 'profileId2' in request.data \
                and request.data['profileId1'] != request.data['profileId2']:
            try:
                profile1 = Profile.objects.get(pk=request.data['profileId1'])
                profile2 = Profile.objects.get(pk=request.data['profileId2'])

                profile1.connections.add(profile2)
                profile2.connections.add(profile1)

                return Response(status=status.HTTP_200_OK, data=CustomUserSerializer(profile2.user).data)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request):
        """
        Delete a Relation between two profiles




        <b>Details</b>

        METHODS : DELETE




        <b>Example:</b>


        {

            "profileId1": 1,

            "profileId2": 3

        }



        <b>RETURNS:</b>

        - 200 OK.

        - 404 NOT FOUND.



        ---
        omit_parameters:
            - form
        """

        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        # print 'X-CSRFToken: '+request.META["CSRF_COOKIE"]
        # print request.META

        if 'profileId1' in request.data and 'profileId2' in request.data \
                and request.data['profileId1'] != request.data['profileId2']:
            try:
                profile1 = Profile.objects.get(pk=request.data['profileId1'])
                profile2 = Profile.objects.get(pk=request.data['profileId2'])

                if profile1 not in profile2.connections.all() or \
                        profile2 not in profile1.connections.all():
                    return Response(status=status.HTTP_400_BAD_REQUEST)

                profile1.connections.remove(profile2)
                profile2.connections.remove(profile1)

                return Response(status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserProfileList(generics.ListCreateAPIView):
    """ <b>Profiles for user</b> """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    allowed_methods = ['get', 'delete']
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

    def delete(self, request, pk=None):
        """
        Deletes every Profile of a given user




        <b>Details</b>

        METHODS : DELETE



        <b>RETURNS:</b>

        - 200 OK.

        - 404 NOT FOUND.

        ---
        omit_parameters:
        - form
        """

        try:
            int_pk = int(pk)
            user = CustomUser.objects.get(pk = int_pk)
            self.queryset = self.queryset.get(user=user).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProfileDetails(generics.ListCreateAPIView):
    """ <b>Profiles for user</b> """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    allowed_methods = ['get', 'delete', 'put']
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

    def delete(self, request, pk=None):
        """
        Deletes Profile for given id




        <b>Details</b>

        METHODS : DELETE



        <b>RETURNS:</b>

        - 200 OK.

        - 400 NOT FOUND.

        ---
        omit_parameters:
        - form
        """

        try:
            int_pk = int(pk)
            self.queryset = self.queryset.get(pk=int_pk).delete()
            return Response(status=status.HTTP_200_OK, data={'delete': 'success'})
        except:
            pass
        return Response(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def put(self, request, pk=None):
        """
        Edits a Profile




        <b>Details</b>

        METHODS : PUT




        <b>Example:</b>


        {

            "name": "Pessoal",

            "color": "RED"


        }



        <b>RETURNS:</b>

        - 200 OK.

        - 404 BAD REQUEST.



        ---
        omit_parameters:
            - form
        """

        #X-CSRFToken: vp9PVkKgRzj8900v62TBN3ZkxMauXnHD

        #print request.META

        try:
            int_pk = int(pk)
            profile = self.queryset.get(pk=int_pk)

            if 'name' in request.data:
                profile.name = request.data['name']
            if 'color' in request.data:
                profile.color = request.data['color']
            profile.save()

            return Response(status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfilePossibleAttributes(generics.ListCreateAPIView):
    """<b>Possible Attributes List</b>"""
    queryset = []
    # gives an error if it doesn't have a serializer class defined
    serializer_class = ProfileSerializer
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
        return self.list(request)


class ColorsAttributes(generics.ListCreateAPIView):
    """<b>Possible Colors List</b>"""
    queryset = []
    # gives an error if it doesn't have a serializer class defined
    serializer_class = ProfileSerializer
    allowed_methods = ['get']
    #pagination_class = GeoJsonPagination

    #def finalize_response(self, request, *args, **kwargs):
    #    response = super(ResourceList, self).finalize_response(request, *args, **kwargs)
    #    response['last_object_update'] = getListLastUpdate(self.get_queryset())
    #    return response

    def get(self, request):
        """
        Gets every possible colors for profiles




        <b>Details</b>

        METHODS : GET



        <b>RETURNS:</b>

        - 200 OK.

        ---
        omit_parameters:
        - form
        """
        resp = {}
        for a in COLORS:
            resp[a[0]] = a[1]
        return Response(resp, status=status.HTTP_200_OK)
        return self.list(request)
