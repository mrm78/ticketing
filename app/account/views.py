from asyncio import start_unix_server
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account.models import *


class Login(APIView):
    def post(self, req):
        data = req.data
        user = User.objects.filter(username=data.get('username')).first()
        if not user or not user.check_password(data.get('password')):
            return Response({'code':101, 'message':'invalid credentials'}, status=422)
        refresh, access = user.new_token()
        return Response({'code':100, 'message':'', 'data':{'refresh_token':refresh, 'access_token':f'Bearer {access}'}})
        
        




