from django.shortcuts import render

from userapp.models import *
from userapp.serializers import*
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
# Create your views here.

class UserRegisterView(APIView):

    permission_classes =[AllowAny]

    def post(self,request):

        user_serializer = UserRegisterSerializer(data= request.data)

        if user_serializer.is_valid():

            serializer = user_serializer.save()

            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    permission_classes = [IsAuthenticated]

    authentication_classes =[BasicAuthentication]

    def post(self,request):

        user = request.user

        token,created = Token.objects.get_or_create(user = user)

        return Response({"message":"login sucess","token":token.key},status=status.HTTP_200_OK)
    


    # JWT
    # ======


    #  def post(self,request):

    #     user = request.user

    #     refresh = RefreshToken.for_user(user) #usernmae password user_id
        
    #     return Response(
    #         {
    #             "message":"login success",
    #             "access": str(refresh.access_token),
    #             "refresh": str(refresh)
    #         },
    #         status=status.HTTP_200_OK
    #     )
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework_simplejwt.authentication import JWTAuthentication
# pip install djngofranework_simplejwt
# settings---> rest_framework.authtoken,simplejwt

# # class ProductListCreateView(ListCreateAPIView):

#     queryset = ProductModel.objects.all()

#     serializer_class = Productserializer

#     permission_classes=[IsAuthenticated]

#     authentication_classes = [JWTAuthentication]

#     def perform_create(self,serializer):

#         serializer.save(user = self.request.user)

# class ProductretriveupdatedeleteView(RetrieveUpdateDestroyAPIView):

#     serializer_class = Productserializer

#     permission_classes =[IsAuthenticated]

#     authentication_classes =[JWTAuthentication]

#     def get_queryset(self):

#         return ProductModel.objects.filter(user = self.request.user)


class AddListTicket(APIView):

    authentication_classes =[TokenAuthentication]

    permission_classes =[IsAuthenticated]

    def post(self,request):

        serializer = SupportTicketSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user =request.user)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):

        data =SupportTicketModel.objects.filter(user =request.user)

        serializer = SupportTicketSerializer(data,many =True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
class RetriveUpdateDelete(APIView):

    permission_classes =[IsAuthenticated]

    authentication_classes =[TokenAuthentication]

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        support = get_object_or_404(SupportTicketModel,id=id,user= request.user)

        serializer = SupportTicketSerializer(support,many= False)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,**kwargs):

        id = kwargs.get('pk')

        support = get_object_or_404(SupportTicketModel,id=id,user= request.user)

        serializer = SupportTicketSerializer(support,data= request.data )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,**kwargs):

        id = kwargs.get('pk')

        support = get_object_or_404(SupportTicketModel,id=id)

        support.delete()

        return Response({"message":"deleted"},status=status.HTTP_200_OK)




