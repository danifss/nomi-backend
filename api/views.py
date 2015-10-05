from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
import django.utils.translation as t
import math
from rest_framework import generics
from core.models import Attribute, Profile
from core.serializers import AttributeSerializer, ProfileSerializer

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