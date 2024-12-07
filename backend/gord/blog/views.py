from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    @action(detail=True, methods=['post'])
    def increment_view_post(self, request, pk=None):
        """
        Incrémente le nombre de vues d'un post de blog spécifique.
        """
        # Récupérer le blog post à partir de l'identifiant (pk)
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response(
                {"error": "Blog post introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Incrémenter le compteur de vues
        blog_post.number_read += 1
        blog_post.save()

        # Retourner une réponse avec le nombre de vues mis à jour
        return Response(
            {"message": f"Le nombre de vues est maintenant à {blog_post.number_read}"},
            status=status.HTTP_200_OK
        )
