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



# @api_view(['GET', 'PUT', 'DELETE'])
# def pessoa_detail_change_and_delete(request, pk):
#     try:
#         pessoa = Pessoa.objects.get(pk = pk) #primary_key
#     except Pessoa.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PessoaSerializer(pessoa)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PessoaSerializer(pessoa, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         pessoa.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
        


    



# Create your views here.
