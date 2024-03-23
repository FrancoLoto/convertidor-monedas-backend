from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import New
from .serializers import NewSerializer


class NewsListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):

        if New.objects.all().exists():

            news = New.objects.all()

            serialiazer = NewSerializer(news, many=True)

            return Response({'news': serialiazer.data},
                            status=status.HTTP_200_OK)

        else:
            return Response({'error': 'No news found.'},
                            status=status.HTTP_404_NOT_FOUND)


class NewDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, slug, format=None):

        if New.objects.filter(slug=slug).exists():

            new = New.objects.get(slug=slug)
            serializer = NewSerializer(new)

            return Response({'new': serializer.data},
                            status=status.HTTP_200_OK)

        else:
            return Response({'error': 'New with that slug does not exist.'},
                            status=status.HTTP_404_NOT_FOUND)
