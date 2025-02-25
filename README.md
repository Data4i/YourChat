# YourChat

* `pip install -r requirements.py`

* `streamlit run app.py`

To get a **Groq API key**, follow these steps:  

### **Step 1: Sign Up or Log In**  
1. Go to the [Groq Platform](https://console.groq.com/).  
2. If you don’t have an account, sign up using your email or GitHub/Google account.  
3. If you already have an account, log in.

### **Step 2: Access API Keys**  
1. Once logged in, go to the **API Keys** section.  
   - You can find this in the dashboard or under **Account Settings**.  
2. Click **Create API Key**.  
3. Name your key (optional) and set permissions if required.

### **Step 3: Copy and Store Your API Key**  
1. After generating the key, **copy it immediately** because you won’t be able to view it again.  
2. create a `.streamlit` folder and then a `secrets.toml` file inside.
3. `GROQ_API_KEY = "api-key"` inside your `secrets.toml`
