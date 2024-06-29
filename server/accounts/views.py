from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Account
from .serializers import CreatAccountSerializer, AccountsSerializer


class CreateAccountView(CreateAPIView):
    serializer_class = CreatAccountSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountsDetailView(RetrieveAPIView):
    serializer_class = AccountsSerializer

    def get(self, request):
        accounts = Account.objects.filter(user=request.user)
        serializer = self.serializer_class(accounts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
