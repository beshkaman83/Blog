from post.models import Tag, Category, Post
from post.api.serializers import TagModelSerializer, CategorySerializer, PostSerializer
from rest_framework import viewsets



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
