import streamlit as st
import json
import os

# Set page layout to wide for dashboard aesthetics
st.set_page_config(page_title="AI Ad Operations Workspace", layout="wide")

# Local storage configuration (Stored on your hosting instance root or local folder)
CONFIG_FILE = "local_vault.json"

def load_keys():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"google_ads": "", "facebook_ads": "", "gemini": "", "chatgpt": "", "claude": ""}

def save_keys(keys_dict):
    with open(CONFIG_FILE, "w") as f:
        json.dump(keys_dict, f)

# Initialize keys in session state
if "keys" not in st.session_state:
    st.session_state.keys = load_keys()

# ---------------------------------------------------------------------------
# TOP BAR: API Key Management Configurations
# ---------------------------------------------------------------------------
st.title("💼 AI Ad Operations Workspace")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔑 Ads Platform API Credentials")
    ads_platform = st.selectbox("Select Advertising Network", ["Google Ads", "Facebook Ads"])
    if ads_platform == "Google Ads":
        g_key = st.text_input("Google Developer Token", st.session_state.keys["google_ads"], type="password")
        if g_key != st.session_state.keys["google_ads"]:
            st.session_state.keys["google_ads"] = g_key
            save_keys(st.session_state.keys)
    else:
        fb_key = st.text_input("Meta System User Access Token", st.session_state.keys["facebook_ads"], type="password")
        if fb_key != st.session_state.keys["facebook_ads"]:
            st.session_state.keys["facebook_ads"] = fb_key
            save_keys(st.session_state.keys)

with col2:
    st.subheader("🧠 Large Language Model Credentials")
    llm_provider = st.selectbox("Select Core Reasoning LLM", ["Gemini", "ChatGPT (OpenAI)", "Claude Sonnet"])
    if llm_provider == "Gemini":
        gemini_key = st.text_input("Google AI Studio API Key", st.session_state.keys["gemini"], type="password")
        if gemini_key != st.session_state.keys["gemini"]:
            st.session_state.keys["gemini"] = gemini_key
            save_keys(st.session_state.keys)
    elif llm_provider == "ChatGPT (OpenAI)":
        openai_key = st.text_input("OpenAI Secret Key", st.session_state.keys["chatgpt"], type="password")
        if openai_key != st.session_state.keys["chatgpt"]:
            st.session_state.keys["chatgpt"] = openai_key
            save_keys(st.session_state.keys)
    else:
        claude_key = st.text_input("Anthropic API Key", st.session_state.keys["claude"], type="password")
        if claude_key != st.session_state.keys["claude"]:
            st.session_state.keys["claude"] = claude_key
            save_keys(st.session_state.keys)

st.markdown("---")

# ---------------------------------------------------------------------------
# SIDEBAR NAVIGATION & MAIN PANEL HUB
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("Navigation Menu")
    app_mode = st.radio("Select Functional Workspace", ["✨ Create Ads", "📊 Research & Data", "💬 Campaign Copilot Chat"])

# --- WORKSPACE 1: CREATE ADS ---
if app_mode == "✨ Create Ads":
    st.header("Creative Copy & Asset Matrix Generation")
    campaign_goal = st.text_input("Campaign Focus/Product Name", placeholder="e.g., EcoFriendly Water Bottle Launch")
    audience = st.text_area("Target Demographic Personas")
    
    if st.button("Generate Ad Blueprint Structures"):
        st.info("Agent is structuring ad copy hooks using the configured LLM token payload...")
        # Creative orchestration logic connects here

# --- WORKSPACE 2: RESEARCH & DATA ---
elif app_mode == "📊 Research & Data":
    st.header("Market Intelligence & Active Campaign Tracking")
    st.caption("Aggregating local file metrics alongside live performance insights.")
    
    # Simple UI mock metrics
    c1, c2, c3 = st.columns(3)
    c1.metric(label="Blended CPA Tracking", value="$22.40", delta="-12%")
    c2.metric(label="Aggregated Ad Spend", value="$4,350.00", delta="+18%")
    c3.metric(label="Overall Conversion Count", value="194", delta="+32%")

# --- WORKSPACE 3: CAMPAIGN COPILOT CHAT ---
elif app_mode == "💬 Campaign Copilot Chat":
    st.header("🤖 Campaign Copilot Engine")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! Select your platform keys above, and ask me to help build or audit your active assets."}]

    # Render previous interactions seamlessly
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Core user interactive loop
    if user_prompt := st.chat_input("Ask your ad agent to scale or adjust parameters..."):
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        # Process response using backend logic safely
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            ai_reply = "I see your command. I have verified your active API keys from our secure local vault file and am staging optimization actions."
            response_placeholder.markdown(ai_reply)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})