import json

from django.forms import model_to_dict

from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)