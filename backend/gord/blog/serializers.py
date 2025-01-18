from rest_framework import serializers
from .models import BlogPost, Summary, BlogPostSection


class OutlineBlogPostSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostSection
        fields = ['id', 'section_content']


class BlogPostSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostSection
        fields = ['id', 'section_content']


class SummaryWithoutSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['id', 'summary', 'summary_link']


class BlogPostListSerializer(serializers.ModelSerializer):
    summaries = SummaryWithoutSectionsSerializer(many=True, read_only=True)
    sections = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'published_date', 'link', 'number_read', 'summaries', 'sections']

    def get_sections(self, obj):
        # Filtrer les sections de type outline uniquement
        outlines = obj.sections.filter(is_outline=True)
        return OutlineBlogPostSectionSerializer(outlines, many=True).data


class SummaryWithSectionsSerializer(serializers.ModelSerializer):
    section = BlogPostSectionSerializer(read_only=True)

    class Meta:
        model = Summary
        fields = ['id', 'summary', 'summary_link', 'section']


class BlogPostDetailSerializer(serializers.ModelSerializer):
    summaries = SummaryWithSectionsSerializer(many=True, read_only=True)
    # sections = BlogPostSectionSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'published_date', 'link', 'number_read', 'summaries']
