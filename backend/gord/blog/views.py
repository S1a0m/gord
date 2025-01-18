from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BlogPost
from .serializers import BlogPostListSerializer, BlogPostDetailSerializer


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()

    # Liste tous les blogs avec leurs sommaires (sans sections)
    def get_serializer_class(self):
        # Utilise BlogPostListSerializer pour la liste et BlogPostDetailSerializer pour les détails
        if self.action == 'list':
            return BlogPostListSerializer
        elif self.action == 'retrieve':
            return BlogPostDetailSerializer
        return super().get_serializer_class()

    # Liste tous les blogs avec leurs sommaires (et sections "outlines" seulement)
    def list(self, request, *args, **kwargs):
        blogs = BlogPost.objects.all()
        serializer = BlogPostListSerializer(blogs, many=True)
        return Response(serializer.data)

    # Récupère un blog spécifique avec toutes ses sections (y compris outlines et autres)
    @action(detail=True, methods=['get'], url_path='with-sections')
    def retrieve_with_sections(self, request, pk=None):
        try:
            blog = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)

        serializer = BlogPostDetailSerializer(blog)
        return Response(serializer.data)

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
