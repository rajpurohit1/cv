import streamlit as st

# ✅ Remove all layout padding and margins
st.markdown("""
    <style>
        div.block-container {
            padding: 0rem !important;
            margin: 0rem !important;
        }

        section[data-testid="stMain"] {
            padding: 0rem !important;
        }

        [data-testid="stSidebarHeader"] {
            height: 2rem;
        }

        .stAppHeader {
            background-color: rgba(255, 255, 255, 0.0);
            visibility: visible;
        }

        body {
            background-color: #f0f2f6;
            font-family: 'Segoe UI', sans-serif;
        }

        .section {
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .title {
            color: #2c3e50;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
        }

        .header {
            color: #34495e;
            font-size: 28px;
            margin-bottom: 10px;
        }

        .content {
            font-size: 18px;
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Title
st.markdown('<div class="title">About Ishwar Singh Rajpurohit</div>', unsafe_allow_html=True)

# ✅ Introduction
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header">A to Z About Me</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Welcome to my personal profile page. Here you will find everything about me from A to Z, including my professional background, technical skills, current projects, career goals, and personal aspirations.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ Personal Details
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header">Personal Details</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content">
<ul>
<li><strong>Name:</strong> Ishwar Singh Rajpurohit</li>
<li><strong>Job Title:</strong> Global Support Specialist</li>
<li><strong>Manager:</strong> Natalia Murias</li>
<li><strong>Skip Manager:</strong> Michal Madej</li>
<li><strong>Office Location:</strong> Vadodara</li>
</ul>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ Technical Skills
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header">Technical Skills</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content">
<ul>
<li>Programming Languages: Python, SQL</li>
<li>Machine Learning: Random Forest, Decision Trees, TfidfVectorizer</li>
<li>Tools: Power BI, Streamlit, Outlook, Power Automate</li>
<li>Web Development: Streamlit</li>
<li>Data Science: Feature Engineering, Model Deployment</li>
</ul>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ Current Projects
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header">Current Projects</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content">
<ul>
<li><strong>Toolbox App Enhancements:</strong> Automating client onboarding and secure password handling</li>
<li><strong>Logging System:</strong> Outlook + Power Automate + SharePoint Excel for centralized access logs</li>
<li><strong>ML in Power BI:</strong> Predictive modeling for NielsenIQ applications</li>
<li><strong>Classification System:</strong> Using decision trees to classify daily-use items into modules/submodules</li>
</ul>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ Career Goals
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header">Career Goals</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content">
<ul>
<li>Become a top-tier data scientist with deep understanding of the full data lifecycle</li>
<li>Master core mathematical foundations: Linear Algebra, Probability, Statistics, Calculus</li>
<li>Build AI models trained on Indian general knowledge</li>
<li>Deliver impactful insights using machine learning</li>
</ul>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ Personal Aspirations A to Z
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="header">Personal Aspirations (A to Z)</div>', unsafe_allow_html=True)
aspirations = {
    "A": "Aspire to be a lifelong learner",
    "B": "Believe in continuous improvement",
    "C": "Care deeply about technology and its impact",
    "D": "Dream big and work hard",
    "E": "Embrace challenges with a positive mindset",
    "F": "Foster innovation and creativity",
    "G": "Grow professionally and personally",
    "H": "Help others succeed",
    "I": "Inspire through actions",
    "J": "Join communities and contribute",
    "K": "Keep learning new skills",
    "L": "Lead by example",
    "M": "Make a difference",
    "N": "Never give up",
    "O": "Open to feedback and improvement",
    "P": "Pursue excellence",
    "Q": "Question the status quo",
    "R": "Respect diversity and inclusion",
    "S": "Strive for balance in life",
    "T": "Take initiative",
    "U": "Understand others' perspectives",
    "V": "Value collaboration",
    "W": "Work with integrity",
    "X": "eXcel in all endeavors",
    "Y": "Yearn for knowledge",
    "Z": "Zealously chase dreams"
}
aspiration_html = "<div class='content'><ul>"
for letter, aspiration in aspirations.items():
    aspiration_html += f"<li><strong>{letter}:</strong> {aspiration}</li>"
aspiration_html += "</ul></div>"
st.markdown(aspiration_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
