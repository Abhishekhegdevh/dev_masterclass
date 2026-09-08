import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="MicroDegree | Project Unlock",
    page_icon="🚀",
    layout="centered"  # Keeps the form neatly centered like in the tutorial
)

# --------------------------------------------------
# CUSTOM CSS (Clean, light aesthetic matching tutorial)
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* Center header titles */
    .title-text {
        text-align: center;
        font-size: 26px;
        font-weight: 700;
        color: #1E40AF;
        margin-bottom: 4px;
    }
    .subtitle-text {
        text-align: center;
        font-size: 15px;
        color: #4B5563;
        margin-bottom: 25px;
    }

    /* Container Card styling */
    div[data-testid="stForm"] {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    /* Success message styling */
    .success-box {
        background-color: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 8px;
        padding: 14px 18px;
        margin-top: 20px;
        color: #166534;
        font-size: 14.5px;
    }

    /* Unlocked project box */
    .unlocked-container {
        border: 2px solid #2563EB;
        border-radius: 10px;
        padding: 18px 22px;
        margin-top: 15px;
        background-color: #FFFFFF;
    }
    .unlocked-title {
        color: #1D4ED8;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .unlocked-item {
        color: #1F2937;
        font-size: 14.5px;
        margin: 6px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown('<div class="title-text">Welcome to MicroDegree 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Register below to unlock exciting projects & tutorials!</div>', unsafe_allow_html=True)

# --------------------------------------------------
# FORM
# --------------------------------------------------
with st.form(key="registration_form"):
    st.markdown("### 📝 Enter Your Details")

    name = st.text_input("Full Name", placeholder="e.g. Manoj")
    email = st.text_input("Email Address", placeholder="e.g. manoj@gmail.com")
    phone = st.text_input("Phone Number", placeholder="e.g. 123456")
    topic = st.text_input("What are you excited to learn?", placeholder="e.g. devops, python, testing")

    submitted = st.form_submit_button("Register Now 🎉")

# --------------------------------------------------
# POST-SUBMIT RESULT (Matching 2nd Image)
# --------------------------------------------------
if submitted:
    if not name or not email or not phone:
        st.error("Please fill in all required fields!")
    else:
        # Green Welcome Banner
        st.markdown(
            f"""
            <div class="success-box">
                <div>☕ <b>Welcome {name}!</b> You're now registered with <b>{email}</b>.</div>
                <div style="margin-top: 5px;">📣 <i>Fantastic! You just unlocked amazing projects!</i></div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Unlocked Projects Box
        st.markdown(
            f"""
            <div class="unlocked-container">
                <div class="unlocked-title">🔥 You Unlocked:</div>
                <div class="unlocked-item">🚀 <b>Python Full-Stack</b> Micro Projects</div>
                <div class="unlocked-item">📌 <b>Kubernetes Architecture & Deployment</b></div>
                <div class="unlocked-item">🤖 <b>AI & ML Hands-On</b> Mini Projects</div>
                <div class="unlocked-item">🎯 Topic Specific Track: <b>{topic.upper() if topic else 'GENERAL TECH'}</b></div>
            </div>
            """,
            unsafe_allow_html=True
        )