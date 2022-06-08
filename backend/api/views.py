from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Products
from products.serializers import ProductsSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """DRF API View"""
    instance = Products.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductsSerializer(instance).data
    return Response(data)
