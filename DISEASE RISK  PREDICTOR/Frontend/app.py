import streamlit as st
import requests

st.set_page_config(page_title="AI Medical Assistant", layout="centered")
st.write("🔥 NEW VERSION LOADED")
# ---------- CUSTOM STYLE ----------

st.markdown("""
<style>
.card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}
.title {
    font-size: 22px;
    font-weight: bold;
}
.value {
    font-size: 28px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🩺 Health Metrics Dashboard")

# ---------- INPUT SECTION ----------
st.markdown("""
<style>
.top-card {
    background: linear-gradient(135deg, #00c853, #64dd17);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}
.big-value {
    font-size: 40px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


st.subheader("Enter Patient Details")


pregnancies = st.slider("Pregnancies", 0, 15, 1)
glucose = st.slider("Glucose", 50, 200, 100)
bp = st.slider("Blood Pressure", 40, 150, 80)
bmi = st.slider("BMI", 10.0, 50.0, 22.0)
age = st.slider("Age", 1, 100, 25)
st.markdown(f"""
<div class="top-card">
    <div>Health Overview</div>
    <div class="big-value">{glucose}</div>
    <div>Glucose Level</div>
</div>
""", unsafe_allow_html=True)

# ---------- CARD VIEW ----------
st.markdown("## 🧠 AI Analysis")
st.subheader("📊 Health Metrics")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="title">Glucose</div>
        <div class="value">{glucose}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="title">Blood Pressure</div>
        <div class="value">{bp}</div>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="title">BMI</div>
        <div class="value">{bmi}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
        <div class="title">Age</div>
        <div class="value">{age}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- PREDICT ----------
with st.spinner("🔍 Analyzing patient data..."):

    data = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": bp,
        "bmi": bmi,
        "age": age
    }
    

    try:
        res = requests.post("http://127.0.0.1:5000/predict", json=data)
        result = res.json()

        st.subheader("🧾 Result")

        if "error" in result:
            st.error(result["error"])
        else:
            if "High" in result["risk"]:
                st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #ff4b2b, #ff416c);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 22px;">
        ⚠️ HIGH RISK DETECTED<br>
        Consult a doctor immediately
    </div>
    """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #00c853, #64dd17);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 22px;">
        ✅ LOW RISK<br>
        Patient condition looks stable
    </div>
    """, unsafe_allow_html=True)
    except:
        st.error("Backend not running")
        

import matplotlib.pyplot as plt

st.subheader("📈 Glucose Trend")

values = [glucose-10, glucose-5, glucose, glucose+2, glucose-3]

fig, ax = plt.subplots()
ax.plot(values, marker='o')
ax.set_title("Trend")
ax.set_xlabel("Time")
ax.set_ylabel("Glucose")

st.pyplot(fig)

# ---------- FOOTER ----------
st.caption("⚠️ For assistance only. Not a medical diagnosis.")