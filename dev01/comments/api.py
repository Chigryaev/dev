from rest_framework import viewsets, status, authentication, permissions
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from articles.models import Article
from .models import Comment
from rest_framework.decorators import action


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    authentication_classes = (
        # authentication.TokenAuthentication,
        authentication.BasicAuthentication,
    )
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)

    def retrieve(self, request, pk=None):
        query = self.queryset.filter(post=pk)
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data)
