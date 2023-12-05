from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ItemSerializer
from .models import Item

# def item_list(request) -> JsonResponse:
#     items = Item.objects.all()

#     item_list = [{
#         "name": item.name,
#         "price": item.price,
#         "desc": item.desc
#     } for item in items]

#     return JsonResponse({"menu_items": item_list})


@api_view(['GET'])
def item_list(request) -> JsonResponse:
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


def item_list_serialized(request) -> JsonResponse:
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def item_detail(request, pk: int) -> JsonResponse:
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
