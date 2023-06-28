from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#class BlogList(ListAPIView):
#  serializer_class = PostSerializer
#  queryset = Post.object.all()

#class BlogDetail(RetrieveAPIView):
#  serializer_class = PostSerializer
#  queryset = Post.object.all()

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def blog_list(request):
  if request.method == 'GET':
    data = Post.object.all()

    serializer = PostSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.erors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT', 'DELETE'])
@permission_classes([permissions.AllowAny])
def blog_detail(request, id):
  try:
    blog = Post.object.get(id=id)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'PUT':
    serializer = PostSerializer(blog, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)