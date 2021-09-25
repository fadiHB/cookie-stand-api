# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )

from django.http.response import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandSerializer


class CookieStandList(generics.ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email
        token["username"] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



#########################################################################################
####### DID NOT WORKING YET
####### TRYING TO FIND A WAY TO CHECK THE SECURTY KEY FOR THE INCOMMING TOKEN
#########################################################################################

# from django.conf import settings
# from django.core.signing import Signer
from django.views.decorators.csrf import csrf_exempt
# from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework_simplejwt.backends import TokenBackend
# from django.core.exceptions import ValidationError
# from rest_framework.response import Response
# https://stackoverflow.com/questions/46230983/validate-and-get-the-user-using-the-jwt-token-inside-a-view-or-consumer

# from rest_framework_simplejwt.backends import TokenBackend
# token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
# data = {'token': token}
#         try:
#             valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
#             user = valid_data['user']
#             request.user = user
#         except ValidationError as v:
#             print("validation error", v)
@csrf_exempt 
def verify_token(req):
    if req.method == "POST":
        if req.user.is_authenticated: # (not AnonymousUser)
            token = req.headers.get('Authorization').split(' ')[1]
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            try: # (not auth user)
                user = req.user
                user_token = valid_data['user']
                
                result = user == user_token
                return JsonResponse({"result": result})
            except:
                return JsonResponse({"result": False})
        else:
            return JsonResponse({"result": False})


        
    

        # print(req.POST)
        # return HttpResponse("<div><h1>"+ key+"</h1></div>")
        ## get the both the givven token and the key
        ## decode the token to get the SIGNATURE key
        ## check if the keys are identical
        ## return boolean
        # print(token)

