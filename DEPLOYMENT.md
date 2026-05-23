# Deployment Guide - Restaurant AI App

## Quick Summary
| Platform | Cost | Difficulty | Best For |
|----------|------|-----------|----------|
| **Streamlit Cloud** | Free (with limits) | ⭐ Easiest | Quick deployment |
| **Render** | Free tier available | ⭐⭐ Easy | Production-ready |
| **Railway** | Pay-as-you-go | ⭐⭐ Easy | Small projects |
| **AWS/Azure/GCP** | Variable | ⭐⭐⭐ Complex | Enterprise |
| **Docker + Any Cloud** | Variable | ⭐⭐⭐ Complex | Full control |

---

## 1. STREAMLIT CLOUD (Recommended - Easiest)

### Steps:
1. **Push code to GitHub**
   - Create a GitHub repo for your project
   - Push your code: `app.py`, `requirements.txt`

2. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Click "Sign up" → "Sign in with GitHub"

3. **Deploy**
   - Click "New app"
   - Select repo, branch, and file (`app.py`)
   - Click "Deploy"

4. **Add Secrets**
   - In Streamlit Cloud dashboard → Settings → Secrets
   - Add your GROQ API key (get one at https://console.groq.com):
     ```
     GROQ_API_KEY = "your-actual-groq-api-key-here"
     ```

### Pros:
- ✅ Free tier available
- ✅ Automatic deploys on git push
- ✅ Built for Streamlit
- ✅ Custom domain support

### Cons:
- ❌ Community tier has sleep after 7 days
- ❌ Limited to Streamlit apps

---

## 2. RENDER (Great Alternative)

### Steps:
1. **Push to GitHub** (same as above)

2. **Create Render Account**
   - Visit: https://render.com
   - Sign up with GitHub

3. **Create New Web Service**
   - Select your GitHub repo
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.port=10000 --server.address=0.0.0.0`

4. **Add Environment Variables**
   - Add `GROQ_API_KEY` in Render dashboard

### Pros:
- ✅ Free tier available
- ✅ Auto-deploys from GitHub
- ✅ Better performance than Streamlit Cloud free tier
- ✅ Custom domains

### Cons:
- ❌ Free tier has limited resources
- ❌ Slightly more complex setup

---

## 3. RAILWAY

### Steps:
1. **Push to GitHub**

2. **Railway Setup**
   - Visit: https://railway.app
   - Click "New Project" → "Deploy from GitHub"
   - Select your repo

3. **Configure**
   - Add `GROQ_API_KEY` environment variable
   - Railway auto-detects Streamlit

### Pros:
- ✅ Easy setup
- ✅ Pay-as-you-go (cheap)
- ✅ Good performance

### Cons:
- ❌ Not free (but $5-10/month typical)

---

## 4. AWS / AZURE / GOOGLE CLOUD

### Best for: Production-grade, high traffic

**EC2 / App Service / Compute Engine Setup:**
1. Create VM instance
2. SSH into machine
3. Install Python & dependencies
4. Run with process manager (PM2, Supervisor, Systemd)
5. Use Nginx as reverse proxy

**More Complex** - requires DevOps knowledge

---

## 5. DOCKER + ANY CLOUD

### Dockerfile Example:
```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

### Deploy to:
- Docker Hub → Render / Railway
- AWS ECS / ECR
- Google Cloud Run
- Azure Container Instances

---

## BEFORE DEPLOYMENT

### 1. Update `requirements.txt`
Make sure it has the exact versions you're using:
```
streamlit==1.28.1
langchain==0.0.354
langchain-community==0.0.20
langchain-groq==0.0.1
```

### 2. Security Checklist
- ✅ Never commit API keys to GitHub
- ✅ Use environment variables for secrets
- ✅ Streamlit Cloud Secrets feature is safe

### 3. Test Locally First
```powershell
# Set API key
$env:GROQ_API_KEY="your-key"

# Run exactly as deployed
streamlit run app.py
```

---

## MY RECOMMENDATION

**For your restaurant app:**

🏆 **START WITH: Streamlit Cloud**
- Easiest setup (5 minutes)
- Perfect for Streamlit apps
- Free tier works great for testing
- GitHub integration is seamless

**THEN UPGRADE TO: Render**
- If you need better uptime
- Don't want sleep timeouts
- Still simple to use

---

## QUICK START (Streamlit Cloud)

1. **Create GitHub repo**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/restaurant-app.git
   git push -u origin main
   ```

2. **Go to**: https://streamlit.io/cloud

3. **Click "New app"** and select your repo

4. **Add GROQ_API_KEY** in Secrets

5. **Done!** Your app is live 🚀

---

## Questions?

- **For Streamlit Cloud help**: https://docs.streamlit.io/streamlit-cloud
- **For Render help**: https://docs.render.com
- **General deployment**: Ask me for specific platform help
