from django.db import models


# ============================================================
# HELPER: Singleton Mixin - model inayoruhusiwa instance 1 tu
# ============================================================
class SingletonModel(models.Model):
    """Mixin ya kuhakikisha model ina instance moja tu (singleton)."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # Hairuhusiwi kufuta singleton

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ============================================================
# 1. SITE SETTINGS - Mipangilio ya jumla ya website
# ============================================================
class SiteSettings(SingletonModel):
    """Mipangilio ya jumla: logo, jina, simu, email, n.k."""

    company_name = models.CharField(max_length=200, default="M2N ENGINEERING")
    company_tagline = models.CharField(max_length=200, default="ELECTRICAL CONTRACTORS · TANZANIA")
    logo_url = models.URLField(
        blank=True,
        default="image/logo.png",
        help_text="URL ya picha ya logo (inaweza kuwa relative kama 'image/logo.png' au URL kamili)"
    )

    phone1 = models.CharField(max_length=30, default="+255 629 625 288")
    phone2 = models.CharField(max_length=30, default="+255 695 550 288")
    whatsapp_number = models.CharField(
        max_length=30,
        default="255629625288",
        help_text="Nambari ya WhatsApp bila + (mfano: 255629625288)"
    )

    email = models.EmailField(default="info@m2nengineering.co.tz")
    address = models.CharField(max_length=300, default="Mkamba Street, Kidatu Ward, Kilombero, Morogoro, Tanzania")
    working_hours = models.CharField(max_length=200, default="Mon-Fri: 8:00 - 17:00 | Sat: 8:00 - 13:00")

    crb_number = models.CharField(max_length=100, default="CRB Class V")
    brela_number = models.CharField(max_length=100, default="BRELA #192412951")
    tin_number = models.CharField(max_length=100, default="TIN: 192-412-951")
    license_year = models.CharField(max_length=20, default="2027")

    # SEO
    meta_description = models.TextField(
        default="M2N Engineering is a premier electrical contracting company based in Kilombero, Morogoro. We deliver world-class electrical solutions, civil construction, and plumbing works across Tanzania.",
        blank=True
    )
    meta_keywords = models.TextField(
        default="electrical contractors Tanzania, civil construction, plumbing works, Kilombero, Morogoro, M2N Engineering",
        blank=True
    )
    og_image_url = models.URLField(
        blank=True,
        default="https://m2nengineeringcoltd.onrender.com/image/logo.png",
        help_text="Open Graph image URL kwa social media previews"
    )
    site_url = models.URLField(
        blank=True,
        default="https://m2nengineeringcoltd.onrender.com",
        help_text="URL kamili ya website"
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "⚙️ Site Settings"

    def __str__(self):
        return f"Site Settings — {self.company_name}"


# ============================================================
# 2. SOCIAL MEDIA
# ============================================================
class SocialMedia(models.Model):
    """Viungo vya social media."""

    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter / X'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('other', 'Other'),
    ]

    ICON_CHOICES = [
        ('fab fa-facebook-f', 'Facebook'),
        ('fab fa-instagram', 'Instagram'),
        ('fab fa-twitter', 'Twitter/X'),
        ('fab fa-x-twitter', 'X (Twitter New)'),
        ('fab fa-linkedin-in', 'LinkedIn'),
        ('fab fa-youtube', 'YouTube'),
        ('fab fa-tiktok', 'TikTok'),
        ('fab fa-whatsapp', 'WhatsApp'),
        ('fab fa-telegram', 'Telegram'),
        ('fas fa-globe', 'Other'),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField(help_text="URL kamili ya ukurasa wako wa social media")
    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='fab fa-facebook-f',
        help_text="Font Awesome icon class"
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "🌐 Social Media Links"
        ordering = ['order']

    def __str__(self):
        return f"{self.get_platform_display()} — {self.url}"


# ============================================================
# 3. HERO SECTION (HOME)
# ============================================================
class HeroSection(SingletonModel):
    """Sehemu ya kwanza ya website (Hero/Home section)."""

    badge_icon = models.CharField(
        max_length=50,
        default="fas fa-bolt",
        help_text="Font Awesome icon class ya badge (mfano: fas fa-bolt)"
    )
    badge_text = models.CharField(
        max_length=200,
        default="CRB CLASS V · BRELA INCORPORATED"
    )

    title_line1 = models.CharField(
        max_length=200,
        default="Powering",
        help_text="Sehemu ya kwanza ya kichwa (rangi nyeupe)"
    )
    title_line2 = models.CharField(
        max_length=200,
        default="Tanzania's Future",
        help_text="Sehemu ya pili ya kichwa (gradient color)"
    )

    description = models.TextField(
        default=(
            "M2N Engineering is a premier electrical contracting company based in Kilombero, Morogoro. "
            "We deliver world-class electrical solutions across Tanzania with uncompromising quality, safety, "
            "and professionalism. In addition to our comprehensive electrical services, we also specialize in "
            "civil construction and plumbing works, offering integrated solutions for all your construction "
            "and infrastructure needs. From foundation to finish, our team of certified experts delivers "
            "excellence in every project."
        )
    )

    btn_primary_text = models.CharField(max_length=100, default="Start Project")
    btn_primary_icon = models.CharField(max_length=50, default="fas fa-rocket")
    btn_primary_url = models.CharField(max_length=100, default="#contact")

    btn_secondary_text = models.CharField(max_length=100, default="Explore Services")
    btn_secondary_icon = models.CharField(max_length=50, default="fas fa-eye")
    btn_secondary_url = models.CharField(max_length=100, default="#services")

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "🏠 Hero Section (Home)"

    def __str__(self):
        return f"Hero — {self.title_line1} {self.title_line2}"


class HeroStat(models.Model):
    """Takwimu zinazoonekana kwenye Hero section (mfano: 33kV, 50+, CRB V)."""

    number = models.CharField(max_length=50, help_text="Mfano: 33kV, 50+, CRB V")
    label = models.CharField(max_length=100, help_text="Mfano: High Voltage, Projects, Class Five")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Hero Stat"
        verbose_name_plural = "📊 Hero Stats"
        ordering = ['order']

    def __str__(self):
        return f"{self.number} — {self.label}"


# ============================================================
# 4. ABOUT SECTION
# ============================================================
class AboutSection(SingletonModel):
    """Sehemu ya About Us."""

    subtitle = models.CharField(max_length=100, default="ABOUT US")
    title_line1 = models.CharField(max_length=200, default="Engineering")
    title_line2 = models.CharField(max_length=200, default="Excellence", help_text="Sehemu yenye gradient color")

    paragraph1 = models.TextField(
        default=(
            "Founded in 2022, M2N Engineering has rapidly established itself as a premier electrical "
            "contractor in Tanzania. Based in Kilombero, Morogoro, we combine local expertise with global "
            "standards to deliver exceptional electrical solutions. Beyond electrical work, we have expanded "
            "our capabilities to include civil construction and plumbing works, providing integrated "
            "infrastructure solutions for residential, commercial, and industrial clients across the country."
        )
    )
    paragraph2 = models.TextField(
        default=(
            "Our team of certified engineers and technicians brings decades of combined experience across "
            "residential, commercial, and industrial projects. We don't just complete projects – we create "
            "lasting partnerships built on trust, quality, and innovation."
        )
    )

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "🏢 About Section"

    def __str__(self):
        return "About Section"


class AboutFeature(models.Model):
    """Vipengele vya About section (mfano: CRB Class V, BRELA, n.k.)."""

    icon = models.CharField(max_length=50, default="fas fa-certificate", help_text="Font Awesome icon class")
    text = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "About Feature"
        verbose_name_plural = "✅ About Features"
        ordering = ['order']

    def __str__(self):
        return self.text


class Credential(models.Model):
    """Credentials zinazoonekana kwenye kadi ya About section."""

    icon = models.CharField(max_length=50, default="fas fa-certificate", help_text="Font Awesome icon class")
    title = models.CharField(max_length=100, help_text="Mfano: High Voltage, Experience, Team, Coverage")
    value = models.CharField(max_length=200, help_text="Mfano: 33kV Certified, 4+ Years Excellence")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Credential"
        verbose_name_plural = "🏆 Credentials"
        ordering = ['order']

    def __str__(self):
        return f"{self.title}: {self.value}"


# ============================================================
# 5. SERVICES SECTION
# ============================================================
class ServicesSection(SingletonModel):
    """Header na intro ya Services section."""

    subtitle = models.CharField(max_length=100, default="WHAT WE DO")
    title_line1 = models.CharField(max_length=200, default="Our")
    title_line2 = models.CharField(max_length=200, default="Services", help_text="Sehemu yenye gradient color")

    intro_paragraph = models.TextField(
        default=(
            "M2N Engineering provides comprehensive electrical solutions tailored to meet the diverse needs "
            "of our clients across Tanzania. From residential wiring to high-voltage industrial installations, "
            "our team of certified experts delivers excellence in every project. Each service is backed by our "
            "commitment to quality, safety, and customer satisfaction."
        )
    )
    intro_highlight = models.CharField(
        max_length=200,
        default="We offer 21 specialized electrical services"
    )
    intro_icon = models.CharField(max_length=50, default="fas fa-bolt")

    class Meta:
        verbose_name = "Services Section"
        verbose_name_plural = "⚡ Services Section"

    def __str__(self):
        return "Services Section"


class Service(models.Model):
    """Huduma moja moja za M2N Engineering."""

    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(help_text="URL ya picha ya huduma")
    icon = models.CharField(max_length=50, default="fas fa-bolt", help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    # Choices for contact form dropdown
    in_contact_form = models.BooleanField(
        default=True,
        help_text="Ionyeshwe kwenye dropdown ya contact form?"
    )

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "🔧 Services"
        ordering = ['order']

    def __str__(self):
        return self.name


class ServiceFeature(models.Model):
    """Kipengele kimoja cha huduma (bullet point)."""

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    text = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Service Feature"
        verbose_name_plural = "Service Features"
        ordering = ['order']

    def __str__(self):
        return f"{self.service.name} → {self.text}"


class ServiceTag(models.Model):
    """Tag moja ya huduma."""

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='tags')
    text = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Service Tag"
        verbose_name_plural = "Service Tags"

    def __str__(self):
        return f"{self.service.name} [{self.text}]"


# ============================================================
# 6. PROJECTS SECTION
# ============================================================
class ProjectsSection(SingletonModel):
    """Header ya Projects section."""

    subtitle = models.CharField(max_length=100, default="PORTFOLIO")
    title_line1 = models.CharField(max_length=200, default="Featured")
    title_line2 = models.CharField(max_length=200, default="Projects", help_text="Sehemu yenye gradient color")

    class Meta:
        verbose_name = "Projects Section"
        verbose_name_plural = "🏗️ Projects Section"

    def __str__(self):
        return "Projects Section"


class Project(models.Model):
    """Mradi mmoja mmoja wa M2N Engineering."""

    image_url = models.URLField(help_text="URL ya picha ya mradi")
    category = models.CharField(max_length=100, help_text="Mfano: High Voltage, Power Distribution")
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, help_text="Mfano: Kilombero, Morogoro")
    is_featured = models.BooleanField(
        default=False,
        help_text="Mradi mkubwa unaochukua nafasi mbili (featured card)"
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "📁 Projects"
        ordering = ['order']

    def __str__(self):
        return f"{self.title} — {self.location}"


# ============================================================
# 7. CONTACT SECTION
# ============================================================
class ContactSection(SingletonModel):
    """Mipangilio ya Contact section."""

    subtitle = models.CharField(max_length=100, default="GET IN TOUCH")
    title_line1 = models.CharField(max_length=200, default="Contact")
    title_line2 = models.CharField(max_length=200, default="Us", help_text="Sehemu yenye gradient color")

    # Contact Info Card title
    info_card_title = models.CharField(max_length=100, default="Contact Information")

    # Form Card title
    form_card_title = models.CharField(max_length=100, default="Send Inquiry")

    # WhatsApp message template
    whatsapp_message_header = models.CharField(
        max_length=200,
        default="*NEW PROJECT INQUIRY - M2N ENGINEERING*"
    )

    class Meta:
        verbose_name = "Contact Section"
        verbose_name_plural = "📞 Contact Section"

    def __str__(self):
        return "Contact Section"
