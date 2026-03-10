"""
=================================================================
M2N ENGINEERING - DATABASE SEED SCRIPT
=================================================================
Tumia hii script kuhifadhi data yote ya website kwenye database.

JINSI YA KUTUMIA:
    python manage.py shell < seed_database.py

AU:
    python manage.py shell
    >>> exec(open('seed_database.py').read())
=================================================================
"""

from website.models import (
    SiteSettings, SocialMedia,
    HeroSection, HeroStat,
    AboutSection, AboutFeature, Credential,
    ServicesSection, Service, ServiceFeature, ServiceTag,
    ProjectsSection, Project,
    ContactSection,
)

print("=" * 60)
print("M2N ENGINEERING - KUANZA KUPAKIA DATA...")
print("=" * 60)


# ============================================================
# 1. SITE SETTINGS
# ============================================================
print("\n[1/8] Kuunda Site Settings...")

site = SiteSettings.load()
site.company_name = "M2N ENGINEERING"
site.company_tagline = "ELECTRICAL CONTRACTORS · TANZANIA"
site.logo_url = "image/logo.png"
site.phone1 = "+255 629 625 288"
site.phone2 = "+255 695 550 288"
site.whatsapp_number = "255629625288"
site.email = "info@m2nengineering.co.tz"
site.address = "Mkamba Street, Kidatu Ward, Kilombero, Morogoro, Tanzania"
site.working_hours = "Mon-Fri: 8:00 - 17:00 | Sat: 8:00 - 13:00"
site.crb_number = "CRB Class V"
site.brela_number = "BRELA #192412951"
site.tin_number = "TIN: 192-412-951"
site.license_year = "2027"
site.meta_description = (
    "M2N Engineering is a premier electrical contracting company based in Kilombero, Morogoro. "
    "We deliver world-class electrical solutions, civil construction, and plumbing works across Tanzania "
    "with uncompromising quality, safety, and professionalism."
)
site.meta_keywords = (
    "electrical contractors Tanzania, civil construction, plumbing works, Kilombero, Morogoro, "
    "M2N Engineering, electrical installation, solar power, CCTV installation"
)
site.og_image_url = "https://m2nengineeringcoltd.onrender.com/image/logo.png"
site.site_url = "https://m2nengineeringcoltd.onrender.com"
site.save()
print("   ✅ Site Settings zimehifadhiwa.")


# ============================================================
# 2. SOCIAL MEDIA
# ============================================================
print("\n[2/8] Kuunda Social Media Links...")

SocialMedia.objects.all().delete()

social_data = [
    {'platform': 'facebook', 'url': 'https://facebook.com/m2nengineering', 'icon': 'fab fa-facebook-f', 'order': 1},
    {'platform': 'instagram', 'url': 'https://instagram.com/m2nengineering', 'icon': 'fab fa-instagram', 'order': 2},
    {'platform': 'whatsapp', 'url': 'https://wa.me/255629625288', 'icon': 'fab fa-whatsapp', 'order': 3},
    {'platform': 'linkedin', 'url': 'https://linkedin.com/company/m2nengineering', 'icon': 'fab fa-linkedin-in', 'order': 4},
    {'platform': 'youtube', 'url': 'https://youtube.com/@m2nengineering', 'icon': 'fab fa-youtube', 'order': 5},
    {'platform': 'tiktok', 'url': 'https://tiktok.com/@m2nengineering', 'icon': 'fab fa-tiktok', 'order': 6},
]

for data in social_data:
    SocialMedia.objects.create(**data, is_active=True)

print(f"   ✅ Social Media links {len(social_data)} zimehifadhiwa.")


# ============================================================
# 3. HERO SECTION
# ============================================================
print("\n[3/8] Kuunda Hero Section...")

hero = HeroSection.load()
hero.badge_icon = "fas fa-bolt"
hero.badge_text = "CRB CLASS V · BRELA INCORPORATED"
hero.title_line1 = "Powering"
hero.title_line2 = "Tanzania's Future"
hero.description = (
    "M2N Engineering is a premier electrical contracting company based in Kilombero, Morogoro. "
    "We deliver world-class electrical solutions across Tanzania with uncompromising quality, safety, "
    "and professionalism. In addition to our comprehensive electrical services, we also specialize in "
    "civil construction and plumbing works, offering integrated solutions for all your construction "
    "and infrastructure needs. From foundation to finish, our team of certified experts delivers "
    "excellence in every project."
)
hero.btn_primary_text = "Start Project"
hero.btn_primary_icon = "fas fa-rocket"
hero.btn_primary_url = "#contact"
hero.btn_secondary_text = "Explore Services"
hero.btn_secondary_icon = "fas fa-eye"
hero.btn_secondary_url = "#services"
hero.save()

# Hero Stats
HeroStat.objects.all().delete()
stats_data = [
    {'number': '33kV', 'label': 'High Voltage', 'order': 1},
    {'number': '50+', 'label': 'Projects', 'order': 2},
    {'number': 'CRB V', 'label': 'Class Five', 'order': 3},
]
for stat in stats_data:
    HeroStat.objects.create(**stat)

print("   ✅ Hero Section na Stats zimehifadhiwa.")


# ============================================================
# 4. ABOUT SECTION
# ============================================================
print("\n[4/8] Kuunda About Section...")

about = AboutSection.load()
about.subtitle = "ABOUT US"
about.title_line1 = "Engineering"
about.title_line2 = "Excellence"
about.paragraph1 = (
    "Founded in 2022, M2N Engineering has rapidly established itself as a premier electrical contractor "
    "in Tanzania. Based in Kilombero, Morogoro, we combine local expertise with global standards to deliver "
    "exceptional electrical solutions. Beyond electrical work, we have expanded our capabilities to include "
    "civil construction and plumbing works, providing integrated infrastructure solutions for residential, "
    "commercial, and industrial clients across the country."
)
about.paragraph2 = (
    "Our team of certified engineers and technicians brings decades of combined experience across residential, "
    "commercial, and industrial projects. We don't just complete projects – we create lasting partnerships "
    "built on trust, quality, and innovation."
)
about.save()

# About Features
AboutFeature.objects.all().delete()
features_data = [
    {'icon': 'fas fa-certificate', 'text': 'CRB Class V Registered', 'order': 1},
    {'icon': 'fas fa-file-alt', 'text': 'BRELA Incorporated', 'order': 2},
    {'icon': 'fas fa-id-card', 'text': 'TIN: 192-412-951', 'order': 3},
    {'icon': 'fas fa-calendar-check', 'text': 'Licensed Until 2027', 'order': 4},
]
for f in features_data:
    AboutFeature.objects.create(**f)

# Credentials
Credential.objects.all().delete()
credentials_data = [
    {'icon': 'fas fa-tower-cell', 'title': 'High Voltage', 'value': '33kV Certified', 'order': 1},
    {'icon': 'fas fa-hard-hat', 'title': 'Experience', 'value': '4+ Years Excellence', 'order': 2},
    {'icon': 'fas fa-users', 'title': 'Team', 'value': '15+ Professionals', 'order': 3},
    {'icon': 'fas fa-globe', 'title': 'Coverage', 'value': 'Nationwide Tanzania', 'order': 4},
]
for c in credentials_data:
    Credential.objects.create(**c)

print("   ✅ About Section, Features, na Credentials zimehifadhiwa.")


# ============================================================
# 5. SERVICES SECTION
# ============================================================
print("\n[5/8] Kuunda Services Section na Huduma 21...")

svc_section = ServicesSection.load()
svc_section.subtitle = "WHAT WE DO"
svc_section.title_line1 = "Our"
svc_section.title_line2 = "Services"
svc_section.intro_icon = "fas fa-bolt"
svc_section.intro_paragraph = (
    "M2N Engineering provides comprehensive electrical solutions tailored to meet the diverse needs "
    "of our clients across Tanzania. From residential wiring to high-voltage industrial installations, "
    "our team of certified experts delivers excellence in every project. Each service is backed by our "
    "commitment to quality, safety, and customer satisfaction."
)
svc_section.intro_highlight = "We offer 21 specialized electrical services"
svc_section.save()

# Delete existing services
Service.objects.all().delete()

# All 21 services with features and tags
services_data = [
    {
        'name': 'CCTV Camera Installation',
        'description': 'Advanced surveillance systems with HD cameras, night vision, and remote monitoring for complete security of your property.',
        'image_url': 'https://cdn.prod.website-files.com/606184adb7296d59f51c3323/6762a52b3d4ec387e9b536b5_security-camera-installation-101-from-system-design-to-deployment.webp',
        'icon': 'fas fa-shield-alt',
        'order': 1,
        'features': ['HD & 4K Cameras', 'Night Vision & Motion Detection', 'Remote Viewing via App'],
        'tags': ['HD Quality', 'Remote Access', '24/7 Recording'],
    },
    {
        'name': 'Electric Fence Installation',
        'description': 'High-security perimeter protection systems that provide reliable deterrent against intruders with real-time alert capabilities.',
        'image_url': 'https://keensight.co.ke/categories/Electric-Fences-Razor.jpg',
        'icon': 'fas fa-bolt',
        'order': 2,
        'features': ['High Voltage Deterrent', 'Alarm Integration', 'Tamper-Proof Design'],
        'tags': ['Perimeter Security', 'Alarm System', 'Energizer'],
    },
    {
        'name': 'Gate Motor Installation',
        'description': 'Automatic gate systems for residential and commercial properties offering convenience, security, and enhanced property value.',
        'image_url': 'https://www.elettronew.com/blog/wp-content/uploads/2024/10/automatizzare-un-cancello.png',
        'icon': 'fas fa-car',
        'order': 3,
        'features': ['Remote Control Operation', 'Safety Sensors', 'Backup Battery Option'],
        'tags': ['Automatic', 'Remote', 'Safety'],
    },
    {
        'name': 'Troubleshooting',
        'description': 'Expert diagnostic services to quickly identify and resolve electrical faults, minimizing downtime and preventing future issues.',
        'image_url': 'https://www.bestbrooklynelectrician.com/wp-content/uploads/2020/11/Electrical-troubleshooting.png',
        'icon': 'fas fa-tools',
        'order': 4,
        'features': ['Advanced Diagnostics', 'Fault Finding', 'Quick Resolution'],
        'tags': ['Diagnostics', 'Repairs', 'Emergency'],
    },
    {
        'name': 'Electrical Maintenance',
        'description': 'Comprehensive preventive and corrective maintenance programs to keep your electrical systems running efficiently and safely.',
        'image_url': 'https://parkinelectric.com/wp-content/uploads/2025/10/oct-blog-img-2.png',
        'icon': 'fas fa-sync-alt',
        'order': 5,
        'features': ['Preventive Maintenance', 'Corrective Repairs', 'System Optimization'],
        'tags': ['Preventive', 'Corrective', 'Inspection'],
    },
    {
        'name': 'Water Pump Installation',
        'description': 'Professional installation and servicing of water pumping systems for domestic, agricultural, and industrial applications.',
        'image_url': 'https://sunnybliss.com/wp-content/uploads/2024/11/Installation-And-Repairing-of-Water-Pumps-12-nov-2024.png',
        'icon': 'fas fa-water',
        'order': 6,
        'features': ['Submersible Pumps', 'Surface Pumps', 'Pressure Systems'],
        'tags': ['Submersible', 'Surface', 'Industrial'],
    },
    {
        'name': 'Residential Wiring',
        'description': 'Complete electrical wiring solutions for homes and apartments, ensuring safety, compliance, and modern functionality.',
        'image_url': 'https://www.ultratechcement.com/content/ultratechcement/in/en/home/for-homebuilders/home-building-explained-single/descriptive-articles/house-electrical-wiring-types/_jcr_content/root/container/container_2072089177/teaser_copy_copy_cop_2001299576.coreimg.jpeg/1741677677264/conduit-wiring.jpeg',
        'icon': 'fas fa-home',
        'order': 7,
        'features': ['New Construction', 'Rewiring & Upgrades', 'Safety Compliance'],
        'tags': ['New Build', 'Rewiring', 'Safety'],
    },
    {
        'name': 'Industrial Wiring',
        'description': 'Complex industrial electrical systems including control panels, motor control centers, and factory installations.',
        'image_url': 'https://www.tridenttechlabs.com/uae/blogs/wp-content/uploads/2025/07/Industrial-Electrical-Network-Engineering-Design-1024x683.jpg',
        'icon': 'fas fa-industry',
        'order': 8,
        'features': ['3-Phase Systems', 'Control Panels', 'Machinery Wiring'],
        'tags': ['3-Phase', 'Control Panels', 'Automation'],
    },
    {
        'name': 'Architecture',
        'description': 'Professional architectural design services with integrated electrical planning for optimal functionality and aesthetics.',
        'image_url': 'https://www.kogakuin.ac.jp/english/faculty/rtfiq300000007j7-img/2.jpg',
        'icon': 'fas fa-draw-polygon',
        'order': 9,
        'features': ['Building Design', 'Electrical Planning', 'Consultation'],
        'tags': ['Design', 'Planning', 'Consulting'],
    },
    {
        'name': 'HT & LT Pole Construction',
        'description': 'Construction of High Tension and Low Tension power distribution poles for utility companies and private developments.',
        'image_url': 'https://shelectromech.com/images/a10.jpg',
        'icon': 'fas fa-tower-cell',
        'order': 10,
        'features': ['33kV HT Poles', 'Distribution Poles', 'Concrete & Steel'],
        'tags': ['33kV', 'Distribution', 'Utility'],
    },
    {
        'name': 'Transformer Installation',
        'description': 'Expert installation, testing, and commissioning of power transformers for distribution substations and industrial facilities.',
        'image_url': 'https://www.weishoelec.com/zb_users/upload/2025/07/202507021751447281115257.jpeg',
        'icon': 'fas fa-charging-station',
        'order': 11,
        'features': ['Distribution Transformers', 'Power Transformers', 'Testing & Commissioning'],
        'tags': ['Distribution', 'Power', 'Substation'],
    },
    {
        'name': 'Motor Rewinding',
        'description': 'Professional rewinding and refurbishment of electric motors to restore performance and extend service life.',
        'image_url': 'https://dandmelectrical.com.au/wp-content/uploads/2022/01/motor-rewinding-4879.jpg',
        'icon': 'fas fa-redo-alt',
        'order': 12,
        'features': ['AC/DC Motors', 'Industrial Motors', 'Pump Motors'],
        'tags': ['AC/DC', 'Repair', 'Refurbishment'],
    },
    {
        'name': 'Wholesale Electrical Products',
        'description': 'Supply of quality electrical materials, cables, switchgear, and components at competitive wholesale prices.',
        'image_url': 'https://ampsqr.com/assets/uploads/carousel/banner-1.png',
        'icon': 'fas fa-store',
        'order': 13,
        'features': ['Cables & Wires', 'Switchgear', 'Lighting Products'],
        'tags': ['Materials', 'Equipment', 'Wholesale'],
    },
    {
        'name': 'Electrical Contractor',
        'description': 'Full-service electrical contracting for commercial, industrial, and infrastructure projects of any scale.',
        'image_url': 'https://braseelectrical.com/wp-content/uploads/2023/09/electrician-with-electric-cable-2022-12-16-11-44-12-utc-copy.jpg',
        'icon': 'fas fa-hard-hat',
        'order': 14,
        'features': ['Project Management', 'Installation Services', 'Maintenance Contracts'],
        'tags': ['CRB V', 'Licensed', 'Insured'],
    },
    {
        'name': 'Plumbing Works',
        'description': 'Professional plumbing installation and maintenance services for residential and commercial buildings.',
        'image_url': 'https://www.geoken.co.ke/images/services/plumbing-works.jpg',
        'icon': 'fas fa-wrench',
        'order': 15,
        'features': ['Water Supply', 'Drainage Systems', 'Sanitary Ware'],
        'tags': ['Water', 'Drainage', 'Installation'],
    },
    {
        'name': 'Cable Termination',
        'description': 'Professional cable termination and testing for low, medium, and high voltage electrical systems.',
        'image_url': 'https://lirp.cdn-website.com/9add30a7/dms3rep/multi/opt/network-684009_1920-640w.jpg',
        'icon': 'fas fa-cable-car',
        'order': 16,
        'features': ['LV Cable Termination', 'MV/HV Terminations', 'Testing & Certification'],
        'tags': ['LV/MV/HV', 'Testing', 'Certification'],
    },
    {
        'name': 'Oil Station Pump Installation',
        'description': 'Specialized installation of fuel dispensing systems and pumps for petrol stations and fuel depots.',
        'image_url': 'https://i.ytimg.com/vi/qofkjUONTJc/hq720.jpg',
        'icon': 'fas fa-gas-pump',
        'order': 17,
        'features': ['Fuel Dispensers', 'Submersible Pumps', 'Control Systems'],
        'tags': ['Fuel Pumps', 'Dispensers', 'Petrol Stations'],
    },
    {
        'name': 'Solar Power Installation',
        'description': 'Complete solar energy solutions including panels, inverters, batteries, and system design for homes and businesses.',
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlL36ZMlrdLLS0irq-ocB2yluPGU2dFX0F2w&s',
        'icon': 'fas fa-solar-panel',
        'order': 18,
        'features': ['Grid-Tie Systems', 'Off-Grid Solutions', 'Battery Backup'],
        'tags': ['Grid-tie', 'Off-grid', 'Hybrid'],
    },
    {
        'name': 'Backup System Installation',
        'description': 'Uninterruptible power solutions including UPS, generators, and inverter backup systems for critical applications.',
        'image_url': 'https://gadgetronix.net/wp-content/uploads/2023/03/Power-Backup-Systems.jpg',
        'icon': 'fas fa-battery-full',
        'order': 19,
        'features': ['Generator Installation', 'UPS Systems', 'Inverter Backup'],
        'tags': ['Generators', 'UPS', 'Inverters'],
    },
    {
        'name': 'Street Lighting Installation',
        'description': 'LED and solar street lighting solutions for public roads, parking lots, and commercial areas.',
        'image_url': 'https://www.smart-solar-lights.com/Content/upload/2018206102/201806042038543310497.png',
        'icon': 'fas fa-street-view',
        'order': 20,
        'features': ['LED Street Lights', 'Solar Lighting', 'Decorative Lighting'],
        'tags': ['LED', 'Solar', 'Public Lighting'],
    },
    {
        'name': 'Civil Construction',
        'description': 'Civil works related to electrical infrastructure including foundations, trenches, and structural support.',
        'image_url': 'https://media.istockphoto.com/id/838476004/photo/silhouette-of-engineer-and-construction-team-working-safely-work-load-concrete-on-scaffolding.jpg?s=612x612&w=0&k=20&c=jpBmpgsT6PTXZYAIk4aHjNQt7LHkiRe_gq1Il9az9o4=',
        'icon': 'fas fa-building',
        'order': 21,
        'features': ['Foundation Works', 'Trenching', 'Concrete Structures'],
        'tags': ['Foundations', 'Trenching', 'Structures'],
    },
]

for svc_data in services_data:
    features = svc_data.pop('features')
    tags = svc_data.pop('tags')
    service = Service.objects.create(**svc_data, is_active=True, in_contact_form=True)
    for i, feat_text in enumerate(features, 1):
        ServiceFeature.objects.create(service=service, text=feat_text, order=i)
    for tag_text in tags:
        ServiceTag.objects.create(service=service, text=tag_text)

print(f"   ✅ Huduma {len(services_data)} zimehifadhiwa na features zake zote.")


# ============================================================
# 6. PROJECTS SECTION
# ============================================================
print("\n[6/8] Kuunda Projects Section na Miradi...")

proj_section = ProjectsSection.load()
proj_section.subtitle = "PORTFOLIO"
proj_section.title_line1 = "Featured"
proj_section.title_line2 = "Projects"
proj_section.save()

Project.objects.all().delete()

projects_data = [
    {
        'image_url': 'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1200&q=85',
        'category': 'High Voltage',
        'title': '33kV Substation & Recloser',
        'location': 'Kilombero, Morogoro',
        'is_featured': True,
        'order': 1,
    },
    {
        'image_url': 'https://www.gridshop.hu/_upload/images/catalog/1300106536/400x300/1300106536_01.jpg',
        'category': 'Power Distribution',
        'title': 'Transformer Commissioning',
        'location': 'Ifakara, Morogoro',
        'is_featured': False,
        'order': 2,
    },
    {
        'image_url': 'https://media.istockphoto.com/id/173006696/photo/power-line-construction.jpg?s=612x612&w=0&k=20&c=O8g9Aehd-TcOqXZlAEEbQblvcVvhHTdvrD7prxmrK5A=',
        'category': 'Line Construction',
        'title': 'MV Distribution Line',
        'location': 'Morogoro Region',
        'is_featured': False,
        'order': 3,
    },
]

for proj_data in projects_data:
    Project.objects.create(**proj_data, is_active=True)

print(f"   ✅ Miradi {len(projects_data)} imehifadhiwa.")


# ============================================================
# 7. CONTACT SECTION
# ============================================================
print("\n[7/8] Kuunda Contact Section...")

contact = ContactSection.load()
contact.subtitle = "GET IN TOUCH"
contact.title_line1 = "Contact"
contact.title_line2 = "Us"
contact.info_card_title = "Contact Information"
contact.form_card_title = "Send Inquiry"
contact.whatsapp_message_header = "*NEW PROJECT INQUIRY - M2N ENGINEERING*"
contact.save()

print("   ✅ Contact Section imehifadhiwa.")


# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("✅ DATA YOTE IMEHIFADHIWA KWA MAFANIKIO!")
print("=" * 60)
print(f"  • Site Settings:    1")
print(f"  • Social Media:     {SocialMedia.objects.count()}")
print(f"  • Hero Stats:       {HeroStat.objects.count()}")
print(f"  • About Features:   {AboutFeature.objects.count()}")
print(f"  • Credentials:      {Credential.objects.count()}")
print(f"  • Services:         {Service.objects.count()}")
print(f"  • Service Features: {ServiceFeature.objects.count()}")
print(f"  • Service Tags:     {ServiceTag.objects.count()}")
print(f"  • Projects:         {Project.objects.count()}")
print("=" * 60)
print("\n🚀 Sasa unaweza kuendesha: python manage.py runserver")
print("📱 Website: http://127.0.0.1:8000/")
print("🔧 Admin:   http://127.0.0.1:8000/admin/")
print("=" * 60)
