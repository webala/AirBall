from django.shortcuts import render
from .serializers import ArticleCreateSerializer, ArticleSerializer
from .models import Article
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.



def home_view(request):
    return render(request, 'pages/home.html', {})

@api_view(['GET'])
def article_list_view(request):
    qs = Article.objects.all()
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def article_create_view(request):
    serializer = ArticleCreateSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return render(request, 'articles/create.html', {})