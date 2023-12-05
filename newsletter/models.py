from django.db import models
from django.core.mail import EmailMultiAlternatives

class SubscribeUsers(models.Model):
    email = models.EmailField(
        max_length=250
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )

    class Meta:
        """Meta class for email news notifications."""
        verbose_name = 'Email news notification'
        verbose_name_plural = 'Email news notifications'

    def __str__(self):
        """Return the name of the email news notification."""
        return self.email


class EmailNewsNotification(models.Model):
    """Model for email news notifications."""
    email_name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Email name',
        help_text='Email name.'
    )
    content = models.TextField(
        max_length=1500,
        null=False,
        blank=False,
        verbose_name='Content',
        help_text='Content.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )
    
    class Meta:
        """Meta class for email news notifications."""
        verbose_name = 'Email news notification'
        verbose_name_plural = 'Email news notifications'

    def __str__(self):
        """Return the name of the email news notification."""
        return self.email_name

    def save(self, *args, **kwargs):
        super().save()
        users = SubscribeUsers.objects.all()
        recipients = [user.email for user in users]
        subject, from_email, to = (
            self.email_name, 'shop_nature', recipients
        )
        text_content = ''
        if self.content:
            html_content = (
                '<h1 style="color:indigo; text-align:center">' +
                self.email_name +
                '</h1><br><p style="text-align:center; font-style: italic;">'
                'Only for our customers!</p><br>'
                '<p>' + self.content + '</p><br>'
                '<p style="text-align:center"><em>Meet out new plants!</em></p>'
                '<br><br><p style="color:SlateBlue;'
                'background-color:Lavender; padding:1em 2em;'
                'text-align:center; font-weight:bold">' + '</p>'
                '<br><br><strong>Visit our shop now! </strong><br><br>'
                '<a href="https://ecommerce-project-uch6.onrender.com">'
                'Go to Shop Nature</a><br><br>'
                '<p>Thank you for being with us!</p>'
                '<em>Shop Nature</em>'
            )
        else:
            html_content = (
                '<h1 style="color:indigo; text-align:center">' +
                self.email_name +
                '</h1><br><p>' + self.content + '</p>'
                '<br><br><strong>Visit our shop now! </strong><br><br>'
                '<a href="https://ecommerce-project-uch6.onrender.com">'
                'Go to Shop Nature</a><br><br>'
                '<p>Thank you for being with us!</p>'
                '<em>Shop Nature</em>'
            )
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, 'text/html')
        try:
            msg.send()
            print("Email sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")
