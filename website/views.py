from django.shortcuts import render
from .models import (
    SiteSettings, SocialMedia,
    HeroSection, HeroStat,
    AboutSection, AboutFeature, Credential,
    ServicesSection, Service,
    ProjectsSection, Project,
    ContactSection,
)


def index(request):
    """Main view ya homepage - inapakia data yote kutoka database."""

    # Load singleton models (zinaunda instance kama hazijaundwa)
    site_settings = SiteSettings.load()
    hero = HeroSection.load()
    about = AboutSection.load()
    services_section = ServicesSection.load()
    projects_section = ProjectsSection.load()
    contact = ContactSection.load()

    context = {
        # Site-wide settings
        'site': site_settings,
        'social_links': SocialMedia.objects.filter(is_active=True).order_by('order'),

        # Hero section
        'hero': hero,
        'hero_stats': HeroStat.objects.all().order_by('order'),

        # About section
        'about': about,
        'about_features': AboutFeature.objects.all().order_by('order'),
        'credentials': Credential.objects.all().order_by('order'),

        # Services section
        'services_section': services_section,
        'services': Service.objects.filter(is_active=True).prefetch_related('features', 'tags').order_by('order'),
        'contact_form_services': Service.objects.filter(is_active=True, in_contact_form=True).order_by('order'),

        # Projects section
        'projects_section': projects_section,
        'projects': Project.objects.filter(is_active=True).order_by('order'),

        # Contact section
        'contact_section': contact,
    }

    return render(request, 'website/index.html', context)
