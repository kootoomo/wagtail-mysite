from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting 

@register_setting
class SocialMediaSettings(BaseSetting):
    # Social media settings for our custom website.
    youtube = models.URLField(blank=True, null=True, help_text="Youtube channel URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("youtube"),
            FieldPanel("instagram"),
        ], heading="Social Media Settings")
    ]
