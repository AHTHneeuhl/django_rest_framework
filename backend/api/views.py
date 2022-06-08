from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Products


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """DRF API View"""
    model_data = Products.objects.all().order_by("?").first()
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "content"])
    return Response(data)
