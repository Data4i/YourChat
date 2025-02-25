# **YourChat 🤖**  

YourChat is an AI-powered chatbot built with **Streamlit**, **LangChain**, and **Groq API**. It allows users to interact with various AI personas, including a **Friendly Mentor**, **Survival Expert**, and **History Professor**. Users can also create custom AI characters.  

## **Features**  
✅ Chat with different AI personalities  
✅ Supports both **text** and **voice input** (speech-to-text using Whisper)  
✅ Memory persistence for ongoing conversations  
✅ Streamlit-based UI for easy interaction  

---

## **Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/yourchat.git
cd yourchat
```

### **2️⃣ Install Dependencies**  
Ensure you have **Python 3.8+** installed. Then, install the required dependencies using:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Groq API Key**  
To use the **Groq AI model**, you need an API key:  

1️⃣ Sign up or log in at [Groq Platform](https://console.groq.com/)  
2️⃣ Navigate to **API Keys** in your dashboard  
3️⃣ Click **Create API Key** and copy the generated key  
4️⃣ Store it securely in your project:  
   - Create a `.streamlit` directory inside the project folder:  
     ```bash
     mkdir .streamlit
     ```
   - Inside `.streamlit`, create a `secrets.toml` file:  
     ```bash
     touch .streamlit/secrets.toml
     ```
   - Add your API key inside `secrets.toml`:  
     ```toml
     GROQ_API_KEY = "your-api-key-here"
     ```

---

## **Running the App**  

Once installation and setup are complete, run the chatbot with:  
```bash
streamlit run app.py
```

Then, open the displayed **local URL** in your browser to start chatting! 🎉  

---

## **Usage**  

### **1️⃣ Select a Character**  
- Choose a chatbot personality from the **sidebar**.  
- You can also create a **custom AI persona** by entering a name.  

### **2️⃣ Choose Input Mode**  
- **Text Input**: Type your message and hit Enter.  
- **Voice Input**: Record your voice, and the AI will transcribe and respond.  

### **3️⃣ Chat with AI**  
- The AI will generate responses based on the selected character's personality.  
- Messages are **persisted** during the session.  

---

## **Project Structure**  

```
yourchat/
│── app.py               # Main Streamlit app
│── requirements.txt      # Required dependencies
│── .streamlit/
│   ├── secrets.toml      # API key storage
│── README.md             # Project documentation
```

---

## **Troubleshooting**  

### **1️⃣ API Key Not Found?**  
- Ensure `secrets.toml` is correctly placed inside `.streamlit/`  
- Double-check that your **Groq API Key** is valid  

### **2️⃣ Dependency Issues?**  
- Try updating pip before installing dependencies:  
  ```bash
  pip install --upgrade pip
  ```  
- If issues persist, create a virtual environment:  
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

### **3️⃣ Streamlit Errors?**  
- Ensure **Streamlit** is properly installed:  
  ```bash
  pip install streamlit
  ```

---

## **Contributing**  

🚀 Want to improve **YourChat**? Feel free to contribute!  

1. Fork the repository  
2. Create a new feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to your branch (`git push origin feature-name`)  
5. Open a **pull request**  

---

## **License**  
📝 This project is licensed under the **MIT License** – feel free to modify and distribute.  

---

🎉 **Enjoy chatting with YourChat!** 🚀