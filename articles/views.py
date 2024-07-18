from account.permissions import IsAuthor
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly, IsSubscriberOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(), IsAuthor()]
        return [IsAuthorOrReadOnly(), IsSubscriberOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
