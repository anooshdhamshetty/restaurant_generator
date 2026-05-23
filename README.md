# 🍽️ Restaurant AI - Menu Generator

> An AI-powered Streamlit app that generates creative restaurant names and menus using LangChain and Groq's lightning-fast LLM.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://restaurantgenerator-aefrdd.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/anooshdhamshetty/restaurant_generator)

### 🔗 [Try It Live Now →](https://restaurantgenerator-aefrdd.streamlit.app/)

---

## ✨ Features

- 🏪 **Restaurant Name Generator** - Get creative restaurant names based on cuisine type
- 📋 **Smart Menu Suggestions** - Auto-generate contextual menus for your restaurant
- ⚡ **Lightning Fast** - Powered by Groq's fast LLM inference
- 🎨 **Simple UI** - Clean, intuitive Streamlit interface

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **LLM Framework** | LangChain |
| **AI Engine** | Groq API |
| **Language** | Python 3.13 |

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anooshdhamshetty/restaurant_generator.git
cd restaurant_generator
```

### 2️⃣ Create Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4️⃣ Get Groq API Key
- Go to [Groq Console](https://console.groq.com)
- Sign up (free!)
- Create an API key
- Set environment variable:

```powershell
$env:GROQ_API_KEY='your-api-key-here'
```

### 5️⃣ Run the Application
```powershell
streamlit run app.py
```

🌐 App opens at: `http://localhost:8501`

---

## 🚀 Deployment

### **Streamlit Cloud** (Recommended ⭐)

1. Push code to GitHub ✅ (Done!)
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New app"** → Select your repo
4. Add `GROQ_API_KEY` in **Secrets**
5. Done! 🎉

**🌐 Live App:** https://restaurantgenerator-aefrdd.streamlit.app/

### Other Platforms

| Platform | Effort | Cost |
|----------|--------|------|
| **Render** | ⭐⭐ Easy | Free+ |
| **Railway** | ⭐⭐ Easy | $5-10/mo |
| **AWS/Azure** | ⭐⭐⭐ Complex | Variable |

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 🔧 Configuration

### Environment Variables

| Variable | Required | Notes |
|----------|----------|-------|
| `GROQ_API_KEY` | ✅ Yes | Get from [Groq Console](https://console.groq.com) |

### Optional Settings

```powershell
# Disable usage telemetry (optional)
$env:STREAMLIT_LOGGER_LEVEL='error'
```

---

## 📁 Project Structure

```
restaurant_generator/
├── 📄 app.py                 # Main Streamlit application
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # This file
├── 📄 SETUP.md              # Local setup guide
├── 📄 DEPLOYMENT.md         # Deployment guide
└── 📄 .gitignore            # Git ignore rules
```

---

## 🐛 Troubleshooting

### Issue: `GROQ_API_KEY not found`
**Solution:** Make sure to set environment variable before running:
```powershell
$env:GROQ_API_KEY='your-actual-key'
streamlit run app.py
```

### Issue: `Port 8501 already in use`
**Solution:** Use different port:
```powershell
streamlit run app.py --server.port 8502
```

### Issue: NumPy warnings on Windows (Python 3.13)
**Solution:** These are harmless warnings. Your app will work fine!

### Issue: Slow first load
**Solution:** LangChain and Groq setup takes ~5-10 seconds on first run. Subsequent runs are faster.

---

## 📚 Documentation

- [Streamlit Docs](https://docs.streamlit.io)
- [LangChain Documentation](https://python.langchain.com)
- [Groq API Reference](https://console.groq.com/docs)

---

## 💡 How It Works

1. **User Input** → Selects cuisine type
2. **Name Generation** → LangChain + Groq creates restaurant name
3. **Menu Creation** → Generates menu for the created restaurant
4. **Display** → Shows results in Streamlit UI

---

## 📄 License

MIT License - Feel free to use this project!

---

## 👤 Author

**Anoosh Dhamshetty**

- GitHub: [@anooshdhamshetty](https://github.com/anooshdhamshetty)
- Email: anooshdhamshetty@gmail.com

---

## 🙏 Support

Found this helpful? Please give it a ⭐ on GitHub!

Have questions? Open an issue or check the docs above.

---

<div align="center">

**Made with ❤️ using Streamlit, LangChain & Groq**

</div>
