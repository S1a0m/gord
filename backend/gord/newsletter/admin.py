from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Subscriber, Newsletter


@admin.action(description="Envoyer la newsletter aux abonnés actifs")
def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        if newsletter.status != Newsletter.DRAFT:
            continue

        # Récupérer les abonnés actifs
        subscribers = Subscriber.objects.filter(is_active=True)
        for subscriber in subscribers:
            # Créer le contenu HTML de l'email avec un lien de désabonnement unique
            email_html_body = render_to_string('newsletter_template.html', {
                'title': newsletter.title,
                'subject': newsletter.subject,
                'content': newsletter.content,
                'preview_url': newsletter.preview_url,
                'unsubscribe_url': f"http://192.168.24.114/{subscriber.unsubscribe_token}",
            })
# /api/newsletter/subscribe/unsubscribe/')}?token=
            # Envoyer l'email avec HTML
            send_mail(
                subject=newsletter.subject,
                message='Ce message nécessite un client email compatible HTML.',  # Texte alternatif
                from_email='precieuxdev1@gmail.com',  # Remplacez par votre email d'envoi
                recipient_list=[subscriber.email],
                fail_silently=False,
                html_message=email_html_body,  # Contenu HTML
            )

        # Mettre à jour le statut de la newsletter
        newsletter.status = Newsletter.SENT
        newsletter.save()


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'unsubscribe_token')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'subject', 'publish_date', 'preview_url', 'status')
    search_fields = ('title',)
    list_filter = ('publish_date',)
    actions = [send_newsletter]
