from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import APIView


# Create your views here.


class get_product(APIView):
    def get(self,request):
        POD=Product.objects.all()
        PJDO=ProductModelSerializers(POD,many=True)
        return Response(PJDO.data)
    

    def post(self, request):
        PJDO=ProductModelSerializers(data=request.data)
        if PJDO.is_valid():
            PJDO.save()
            return Response({'success':'data has been inserted successfully..'})
        else:
            return Response({'error' : 'data is not valid..'})