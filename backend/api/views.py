from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Products
from products.serializers import ProductsSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """DRF API View"""
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
    return Response(serializer.data)
