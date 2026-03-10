from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, SocialMedia,
    HeroSection, HeroStat,
    AboutSection, AboutFeature, Credential,
    ServicesSection, Service, ServiceFeature, ServiceTag,
    ProjectsSection, Project,
    ContactSection,
)


# ============================================================
# INLINE MODELS
# (HeroStat, AboutFeature, Credential hazina FK kwa hivyo
#  zinasimamiwa kama models zao wenyewe kwenye sidebar)
# ============================================================

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1
    fields = ('text', 'order')


class ServiceTagInline(admin.TabularInline):
    model = ServiceTag
    extra = 1
    fields = ('text',)


# ============================================================
# SITE SETTINGS ADMIN
# ============================================================

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('🏢 Company Info', {
            'fields': ('company_name', 'company_tagline', 'logo_url')
        }),
        ('📞 Contact Details', {
            'fields': ('phone1', 'phone2', 'whatsapp_number', 'email', 'address', 'working_hours')
        }),
        ('📜 Certifications', {
            'fields': ('crb_number', 'brela_number', 'tin_number', 'license_year')
        }),
        ('🔍 SEO & Meta Tags', {
            'classes': ('collapse',),
            'fields': ('meta_description', 'meta_keywords', 'og_image_url', 'site_url')
        }),
    )

    def has_add_permission(self, request):
        return False if SiteSettings.objects.exists() else True

    def has_delete_permission(self, request, obj=None):
        return False


# ============================================================
# SOCIAL MEDIA ADMIN
# ============================================================

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('platform_badge', 'url_display', 'icon', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active', 'platform')
    ordering = ('order',)

    fieldsets = (
        ('Platform Info', {
            'fields': ('platform', 'url', 'icon')
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )

    def platform_badge(self, obj):
        colors = {
            'facebook': '#1877f2',
            'instagram': '#e4405f',
            'twitter': '#1da1f2',
            'linkedin': '#0a66c2',
            'youtube': '#ff0000',
            'tiktok': '#000000',
            'whatsapp': '#25d366',
            'telegram': '#0088cc',
            'other': '#6c757d',
        }
        color = colors.get(obj.platform, '#6c757d')
        return format_html(
            '<span style="background:{};color:white;padding:3px 10px;border-radius:12px;font-size:0.8rem">'
            '<i class="{}"></i> {}</span>',
            color, obj.icon, obj.get_platform_display()
        )
    platform_badge.short_description = "Platform"

    def url_display(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url[:50] + '...' if len(obj.url) > 50 else obj.url)
    url_display.short_description = "URL"


# ============================================================
# HERO SECTION ADMIN
# ============================================================

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('🏷️ Badge', {
            'fields': ('badge_icon', 'badge_text')
        }),
        ('📝 Title', {
            'fields': ('title_line1', 'title_line2'),
            'description': 'title_line1 = nyeupe, title_line2 = gradient color'
        }),
        ('📄 Description', {
            'fields': ('description',)
        }),
        ('🔘 Buttons', {
            'fields': (
                ('btn_primary_text', 'btn_primary_icon', 'btn_primary_url'),
                ('btn_secondary_text', 'btn_secondary_icon', 'btn_secondary_url'),
            )
        }),
    )
    def has_add_permission(self, request):
        return False if HeroSection.objects.exists() else True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroStat)
class HeroStatAdmin(admin.ModelAdmin):
    list_display = ('number', 'label', 'order')
    list_editable = ('order',)
    ordering = ('order',)


# ============================================================
# ABOUT SECTION ADMIN
# ============================================================

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('📌 Section Header', {
            'fields': ('subtitle', 'title_line1', 'title_line2')
        }),
        ('📝 Content', {
            'fields': ('paragraph1', 'paragraph2')
        }),
    )
    def has_add_permission(self, request):
        return False if AboutSection.objects.exists() else True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ('icon_preview', 'text', 'order')
    list_editable = ('order',)
    ordering = ('order',)

    def icon_preview(self, obj):
        return format_html('<i class="{}" style="font-size:1.2rem;color:#00c2ff"></i> {}', obj.icon, obj.icon)
    icon_preview.short_description = "Icon"


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('icon_preview', 'title', 'value', 'order')
    list_editable = ('order',)
    ordering = ('order',)

    def icon_preview(self, obj):
        return format_html('<i class="{}" style="font-size:1.2rem;color:#00c2ff"></i>', obj.icon)
    icon_preview.short_description = "Icon"


# ============================================================
# SERVICES SECTION ADMIN
# ============================================================

@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('📌 Section Header', {
            'fields': ('subtitle', 'title_line1', 'title_line2')
        }),
        ('📝 Intro Text', {
            'fields': ('intro_icon', 'intro_paragraph', 'intro_highlight')
        }),
    )

    def has_add_permission(self, request):
        return False if ServicesSection.objects.exists() else True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('order_num', 'service_preview', 'name', 'is_active', 'in_contact_form', 'order')
    list_editable = ('is_active', 'in_contact_form', 'order')
    list_filter = ('is_active', 'in_contact_form')
    search_fields = ('name', 'description')
    ordering = ('order',)

    fieldsets = (
        ('📋 Basic Info', {
            'fields': ('name', 'description', 'icon', 'order')
        }),
        ('🖼️ Image', {
            'fields': ('image_url',),
            'description': 'Weka URL ya picha. Picha inapaswa kuwa na ubora mzuri (min 400x200px).'
        }),
        ('⚙️ Settings', {
            'fields': ('is_active', 'in_contact_form')
        }),
    )
    inlines = [ServiceFeatureInline, ServiceTagInline]

    def order_num(self, obj):
        return format_html('<span style="font-weight:bold;color:#00c2ff">#{}</span>', obj.order)
    order_num.short_description = "#"

    def service_preview(self, obj):
        if obj.image_url:
            return format_html(
                '<img src="{}" style="width:60px;height:40px;object-fit:cover;border-radius:4px">',
                obj.image_url
            )
        return format_html('<i class="{}" style="font-size:1.5rem;color:#facc15"></i>', obj.icon)
    service_preview.short_description = "Preview"


@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('service', 'text', 'order')
    list_editable = ('order',)
    list_filter = ('service',)
    ordering = ('service', 'order')


@admin.register(ServiceTag)
class ServiceTagAdmin(admin.ModelAdmin):
    list_display = ('service', 'text')
    list_filter = ('service',)
    search_fields = ('text',)


# ============================================================
# PROJECTS SECTION ADMIN
# ============================================================

@admin.register(ProjectsSection)
class ProjectsSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('📌 Section Header', {
            'fields': ('subtitle', 'title_line1', 'title_line2')
        }),
    )

    def has_add_permission(self, request):
        return False if ProjectsSection.objects.exists() else True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_preview', 'title', 'category', 'location', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('is_featured', 'is_active', 'category')
    search_fields = ('title', 'category', 'location')
    ordering = ('order',)

    fieldsets = (
        ('📋 Project Info', {
            'fields': ('title', 'category', 'location')
        }),
        ('🖼️ Image', {
            'fields': ('image_url',)
        }),
        ('⚙️ Settings', {
            'fields': ('is_featured', 'is_active', 'order'),
            'description': 'Featured project inachukua nafasi kubwa zaidi kwenye grid'
        }),
    )

    def project_preview(self, obj):
        if obj.image_url:
            return format_html(
                '<img src="{}" style="width:80px;height:50px;object-fit:cover;border-radius:4px">',
                obj.image_url
            )
        return "—"
    project_preview.short_description = "Preview"


# ============================================================
# CONTACT SECTION ADMIN
# ============================================================

@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('📌 Section Header', {
            'fields': ('subtitle', 'title_line1', 'title_line2')
        }),
        ('🃏 Card Titles', {
            'fields': ('info_card_title', 'form_card_title')
        }),
        ('💬 WhatsApp', {
            'fields': ('whatsapp_message_header',)
        }),
    )

    def has_add_permission(self, request):
        return False if ContactSection.objects.exists() else True

    def has_delete_permission(self, request, obj=None):
        return False
