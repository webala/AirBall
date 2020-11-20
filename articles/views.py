from django.shortcuts import render
from .serializers import ArticleCreateSerializer
from .models import Article
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['POST', 'GET'])
def article_create_view(request):
    serializer = ArticleCreateSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return render(request, 'articles/create.html')