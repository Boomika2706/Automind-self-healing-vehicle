# file name: automind_simulation_mobile.py
import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# Set Streamlit page to wide mode (mobile-friendly)
st.set_page_config(layout="centered")

# -------------------
# Header (Mobile UI)
# -------------------
st.markdown("""
<div style="text-align:center; padding: 5px;">
    <h1 style="color:#ff4b4b;">🧠 AutoMind Simulation</h1>
    <h3 style="color:#cccccc;">Real-Time Sensor Monitoring</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; color:#aaaaaa; font-size:16px;">
This mobile-friendly prototype simulates machine sensor data and detects issues in real-time.
</p>
""", unsafe_allow_html=True)

# Centered start button
start_simulation = st.button("▶️ Start Simulation", use_container_width=True)

# Style for mobile-friendly cards
card_style = """
    background-color:#1E1E1E;
    padding:15px;
    border-radius:12px;
    margin-top:10px;
    border:1px solid #333;
"""

# -------------------
# Simulation
# -------------------
if start_simulation:
    st.success("Simulation Started!")
    
    sensor_placeholder = st.empty()
    issue_placeholder = st.empty()
    graph_placeholder = st.empty()

    temp_values = []
    vib_values = []
    time_steps = []

    for i in range(30):

        # Generate data
        temperature = random.randint(20, 100)
        vibration = random.randint(0, 50)

        temp_values.append(temperature)
        vib_values.append(vibration)
        time_steps.append(i)

        # ------------------------
        # Mobile Sensor Card
        # ------------------------
        sensor_placeholder.markdown(f"""
        <div style="{card_style}">
            <h4 style="color:#4fc3f7;">📟 Live Sensor Readings</h4>
            <p style="color:white; font-size:18px;">
                🌡️ <b>Temperature:</b> {temperature}°C<br>
                🔧 <b>Vibration:</b> {vibration}
            </p>
        </div>
        """, unsafe_allow_html=True)

        # ------------------------
        # Issue Alert (Mobile)
        # ------------------------
        if temperature > 75 or vibration > 30:
            issue_placeholder.markdown(f"""
            <div style="{card_style}; background-color:#3b0000; border:1px solid #ff4d4d;">
                <h4 style="color:#ff4d4d;">⚠️ Issue Detected</h4>
                <p style="color:white; font-size:18px;">Machine requires attention.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            issue_placeholder.markdown(f"""
            <div style="{card_style}; background-color:#003300; border:1px solid #1db954;">
                <h4 style="color:#1db954;">✅ Normal Operation</h4>
                <p style="color:white; font-size:18px;">System running smoothly.</p>
            </div>
            """, unsafe_allow_html=True)

        # ------------------------
        # Live Graph (Mobile)
        # ------------------------
        fig, ax = plt.subplots()
        ax.plot(time_steps, temp_values, label="Temperature (°C)")
        ax.plot(time_steps, vib_values, label="Vibration")
        ax.set_xlabel("Time")
        ax.set_ylabel("Values")
        ax.set_title("Real-Time Sensor Graph")
        ax.legend()

        graph_placeholder.pyplot(fig)

        time.sleep(1)

    st.info("Simulation Completed!")
