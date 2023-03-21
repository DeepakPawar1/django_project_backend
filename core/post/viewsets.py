from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.abstract.viewsets import AbstractViewSet
from core.post.models import Post
from core.post.serializers import PostSerializer


class PostViewSet(AbstractViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    http_method_names = ['post','get','put','delete']
    print("in pvset")
    def get_queryset(self):
        return Post.objects.all()
    
    def get_object(self):
        print(self.kwargs['pk'],";;;;;<<<>>>>>>")
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj

    def create(self,request,*args,**kwargs):
        print("increate")
        serializer = self.get_serializer(data=request.data)
        print("###########serializer",serializer)
        serializer.is_valid(raise_exception=True)
        print("$$$$$$$$$$performing create")
        self.perform_create(serializer)
        print("<><><><><><><>after creation")
        return Response(serializer.data,status=201)