from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from aplicativo.models import Pessoa
from aplicativo.serializers import PessoaSerializer
from rest_framework.response import Response
from rest_framework import status


from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

class PessoaViewSet(viewsets.ModelViewSet):
    authetication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaList(generics.ListCreateAPIView):
    authetication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authetication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

















# class PessoaList(APIView):
#     def get(self, request):
#         pessoa = Pessoa.objects.all()
#         serializer = PessoaSerializer(pessoa, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PessoaSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 





    



# Create your views here.
