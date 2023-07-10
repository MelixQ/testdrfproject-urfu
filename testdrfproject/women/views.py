from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women
from .serializers import WomenSerializer


# Create your views here.
class WomenAPIView(APIView):
    def get(self, request):
        women = Women.objects.all()
        return Response({'posts': WomenSerializer(women,many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )

        return Response({'post': WomenSerializer(post_new).data})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
