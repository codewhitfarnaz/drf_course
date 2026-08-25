from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer
from blog import serializers

"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


@api_view(['GET', 'POST'])
def hello_world(request):
    name = request.GET.get('name')
    lastname = request.GET.get('lastname')
    if request.method == "POST":
        data = request.data
        return Response({"message": f" hello {data["name"]} {data['lastname']}"})
    return Response({'message': "im from fbv and post"})


class HelloWorld(APIView):
    def get(self, request):
        return Response({"MESSAGE": "Hello World!"})

    def post(self, request):
        return Response({"MESSAGE": "Hello World!"})


class GetCryptoPrice(APIView):
    def get(self, request):
        cion = request.GET.get('coin')
        response = request.get(f"https://api.binance.com/api/v3/ticker/price?symbol={cion}")
        data = response.json()
        result = {
            "symbol": data["symbol"],
            "price": data["price"]
        }
        return response(data=result)

class ArticleListView(APIView):
    def get(self,request):
        queryset=Article.objects.all()
        ser=ArticleSerializer(instance=queryset,many=True)
        return Response(ser.data)

class ArticleDetailSerializer(APIView):
    def get(self,request,pk):
        instance=Article.objects.get(id=pk)
        serializer=ArticleSerializer(instance)
        return Response(serializer.data)

class AddArticleView(APIView):
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Article added successfully!"})
        return Response(serializer.errors)