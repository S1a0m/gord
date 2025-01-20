from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from .models import BlogPost
from django.db.models import Q
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
        serializer = BlogPostListSerializer(blogs, many=True, context={'request': request})
        return Response(serializer.data)

    # Récupère un blog spécifique avec toutes ses sections (y compris outlines et autres)
    @action(detail=True, methods=['get'], url_path='with-sections')
    def retrieve_with_sections(self, request, pk=None):
        try:
            blog = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)

        serializer = BlogPostDetailSerializer(blog, context={'request': request})
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


class BlogPostSearchView(ListAPIView):
    """
    Recherche instantanée des blogs côté serveur.
    """
    serializer_class = BlogPostListSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '').strip()
        if search_query:
            # Rechercher dans le titre, contenu des sections et sommaires
            return BlogPost.objects.filter(
                Q(title__icontains=search_query) |
                Q(sections__section_content__icontains=search_query) |
                Q(summaries__summary__icontains=search_query)
            ).distinct()
        return BlogPost.objects.none()  # Retourne une liste vide si aucune recher
