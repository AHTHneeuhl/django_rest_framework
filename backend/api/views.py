import json
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

from products.models import Products


def api_home(request, *args, **kwargs):
    model_data = Products.objects.all().order_by("?").first()
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "content"])
        json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={"content-type": "application/json"})
