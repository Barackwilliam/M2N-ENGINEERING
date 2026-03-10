# M2N Engineering — Django Website

## 🚀 Local Development

```bash
# 1. Activate virtual environment
python -m venv venv
venv\scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create static folder
mkdir static

# 4. Run migrations (SQLite locally)
python manage.py makemigrations
python manage.py migrate

# 5. Seed database
python manage.py shell < seed_database.py

# 6. Create admin user
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

---

## ☁️ Deployment kwenye Render + Supabase

### Step 1: Push Code kwenye GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/m2n-engineering.git
git push -u origin main
```

### Step 2: Tengeneza Web Service kwenye Render
1. Nenda https://render.com → **New** → **Web Service**
2. Connect GitHub repo yako
3. Weka mipangilio hii:
   - **Runtime:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn m2n_engineering.wsgi --log-file -`

### Step 3: Weka Environment Variables kwenye Render
Nenda **Environment** tab, ongeza variables hizi:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | (generate random key — angalia chini) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app.onrender.com` |
| `DATABASE_URL` | `postgresql://postgres:[PASSWORD]@db.hbwbifvbzvkeishhxvtd.supabase.co:5432/postgres` |

### Jinsi ya Generate SECRET_KEY:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 4: Seed Database (baada ya deploy)
Kwenye Render → **Shell** tab:
```bash
python manage.py shell < seed_database.py
python manage.py createsuperuser
```

---

## 🌐 URLs
- **Website:** https://your-app.onrender.com/
- **Admin:** https://your-app.onrender.com/admin/

---

## 📁 Files za Deployment
| File | Kazi |
|------|------|
| `Procfile` | Inaambia Render kutumia gunicorn |
| `build.sh` | Inafanya collectstatic + migrate kiotomatiki |
| `requirements.txt` | Python packages zote |
| `.env.example` | Mfano wa environment variables |
| `.gitignore` | Files zisizoingia kwenye Git |
