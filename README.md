https://mealbot.streamlit.app

# 👨‍🍳 Mealbot: Your AI Culinary Tutor & Meal Planner

Mealbot is an intelligent culinary assistant powered by Google Gemini AI that provides personalized cooking guidance, nutritional advice, and custom meal planning based on your dietary preferences and protein needs.

## 🌟 Features

### 🍳 Culinary Q&A
- **Cooking Techniques**: Get expert guidance on various cooking methods
- **Ingredient Substitutions**: Find alternatives for dietary restrictions or missing ingredients  
- **Recipe Customization**: Modify recipes to suit your taste and dietary needs
- **Food Science**: Understand the science behind cooking processes

### 🥗 Personalized Meal Planning
- **Protein Calculation**: Automatically calculates daily protein needs based on age, weight, height, gender, and activity level
- **Dietary Preferences**: Supports Omnivore, Vegetarian, Vegan, Pescatarian, Keto, Paleo, Mediterranean
- **Comprehensive Meal Plans**: Complete daily meal prep with protein breakdown, preparation instructions, shopping lists, and storage tips

## 📋 Prerequisites

- Python 3.11+ (Python 3.13+ recommended)
- Google Gemini API key
- Virtual environment (recommended)

## 🚀 Installation

### 1. Setup Environment
```bash
python3.13 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install streamlit google-generativeai python-dotenv
```

### 2. Configure API Key
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

**Getting a Gemini API Key:** Visit [Google AI Studio](https://makersuite.google.com/app/apikey), sign in, create a new API key.

## 📁 Project Structure

```
chef-maestro/
├── app.py              # Streamlit web application
├── chef.py             # Core Gemini AI integration
├── .env                # Environment variables
└── README.md          # Documentation
```

## 📝 Required Files

### chef.py
You need to create a `chef.py` file with the Gemini AI integration. This file should include:
- Environment variable loading
- Gemini API configuration
- Model initialization
- `ask_chef(prompt)` function that returns AI responses

## 🏃‍♂️ Running the Application

```bash
python -m streamlit run app.py
```

The application opens at `http://localhost:8501`

## 🎯 Usage Guide

### Culinary Q&A Tab
Ask cooking questions and get expert advice. Examples: "How do I make a perfect soufflé?", "What's the science behind caramelization?"

### Personalized Meal Prep Tab
1. Fill out your profile (age, weight, height, gender, activity level, dietary preference)
2. Click "Generate My Meal Prep Plan"
3. View calculated protein needs and comprehensive meal plan

## ⚙️ Configuration

### Protein Calculation
- **Sedentary**: 0.8g per kg body weight
- **Lightly Active**: 1.0g per kg
- **Moderately Active**: 1.2g per kg
- **Very Active**: 1.4g per kg
- **Extremely Active**: 1.6g per kg
- **Age 65+**: Additional 0.2g per kg

### Supported Diets
Omnivore, Vegetarian, Vegan, Pescatarian, Keto, Paleo, Mediterranean

## 🛠️ Troubleshooting

### Common Issues

**ModuleNotFoundError**: Ensure virtual environment is activated and packages are installed
**API Key Error**: Check `.env` file exists and API key is correct
**Wrong Python Version**: Use `python -m streamlit run app.py`
**Virtual Environment Issues**: Recreate environment with correct Python version

## 🔐 Security Notes

- Never commit your `.env` file to version control
- Keep your Gemini API key private
- Add `.env` to your `.gitignore` file

## 🚀 Deployment

### Streamlit Cloud
1. Upload code to GitHub (without `.env` file)
2. Connect to [Streamlit Cloud](https://share.streamlit.io/)
3. Add `GEMINI_API_KEY` in secrets management
4. Deploy

### Local Network Access
```bash
streamlit run app.py --server.address 0.0.0.0
```

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Google Gemini AI** for intelligent responses
- **Streamlit** for the web framework
- **Nutrition Science Community** for protein guidelines

---

**Built with ❤️ for home cooks and nutrition enthusiasts!**
