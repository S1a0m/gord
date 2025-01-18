from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Subscriber, Newsletter


@admin.action(description="Envoyer la newsletter aux abonnés actifs")
def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        if newsletter.status != Newsletter.DRAFT:
            continue

        # Récupérer les abonnés actifs
        subscribers = Subscriber.objects.filter(is_active=True)
        for subscriber in subscribers:
            # Créer le contenu de l'email avec un lien de désabonnement unique
            email_body = render_to_string('newsletter_template.html', {
                'title': newsletter.title,
                'content': newsletter.content,
                'unsubscribe_url': f"{request.build_absolute_uri('/api/newsletter/subscribe/unsubscribe/')}?token={subscriber.unsubscribe_token}/",
            })

            # Envoyer l'email
            send_mail(
                subject=newsletter.subject,
                message=email_body,
                from_email='precieuxdev1@gmail.com',  # Remplacez par votre email d'envoi
                recipient_list=[subscriber.email],
                fail_silently=False,
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
    list_display = ('title', 'content', 'subject', 'publish_date', 'status')
    search_fields = ('title',)
    list_filter = ('publish_date',)
    actions = [send_newsletter]
