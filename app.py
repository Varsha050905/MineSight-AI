import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MineSight AI",
    page_icon="⛏️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 20px;
        color: #666;
        margin-top: 0px;
    }

    .risk-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #fff3cd;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown('<div class="main-title">⛏️ MineSight AI</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Predict. Prevent. Produce. | AI + Space Technology for Smarter Mining</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🧠 MineSight AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Command Center",
        "🗺️ Reserve Intelligence",
        "📈 Production Intelligence",
        "⚠️ Risk Intelligence",
        "💡 Action Intelligence"
    ]
)

# --------------------------------------------------
# SAMPLE DATA
# --------------------------------------------------
np.random.seed(42)

months = pd.date_range("2025-01-01", periods=12, freq="ME")

production = [
    820, 850, 870, 860,
    900, 920, 890, 910,
    880, 850, 820, 790
]

target = [900] * 12

# ==================================================
# PAGE 1 — COMMAND CENTER
# ==================================================

if page == "🏠 Command Center":

    st.header("🧠 Mining Intelligence Command Center")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🗺️ Mining Zones", "12")
    col2.metric("🟢 High Potential Zones", "4")
    col3.metric("📈 Production Efficiency", "82%", "-4%")
    col4.metric("🚨 Active Risks", "2", "+1")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🗺️ Reserve Intelligence")

        st.success("🟢 HIGH POTENTIAL ZONE IDENTIFIED")

        st.write("**Top Exploration Zone:** Zone A")
        st.write("**AI Potential Score:** 87%")
        st.write("**Confidence Level:** High")

        st.caption(
            "Based on geological indicators and satellite-derived surface patterns."
        )

    with col2:

        st.subheader("⚠️ Production Intelligence")

        st.error("🔴 HIGH SHORTFALL RISK")

        st.write("**Shortfall Probability:** 78%")
        st.write("**Predicted Production:** 790 tonnes")
        st.write("**Target Production:** 900 tonnes")

        st.caption(
            "Risk detected before the production target is affected."
        )

    st.divider()

    st.subheader("🔄 Closed-Loop Mining Intelligence")

    st.markdown(
        "📊 **DATA** → 🧠 **PREDICT** → ⚠️ **DETECT RISK** → "
        "💡 **RECOMMEND ACTION** → 👷 **EXPERT FEEDBACK** → 🔄 **IMPROVE**"
    )

# ==================================================
# PAGE 2 — RESERVE INTELLIGENCE
# ==================================================

elif page == "🗺️ Reserve Intelligence":

    st.header("🗺️ Reserve Intelligence")

    st.write(
        "AI prioritizes exploration zones using geological and "
        "satellite-derived indicators."
    )

    zones = pd.DataFrame({
        "Zone": ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"],
        "Geological Score": [88, 75, 62, 45, 38],
        "Satellite Indicator": [84, 70, 60, 48, 35],
        "AI Potential Score": [87, 73, 61, 46, 36],
        "Potential": ["🟢 HIGH", "🟢 HIGH", "🟡 MEDIUM",
                      "🟡 MEDIUM", "🔴 LOW"]
    })

    st.dataframe(zones, use_container_width=True)

    st.divider()

    selected_zone = st.selectbox(
        "Select Exploration Zone",
        zones["Zone"]
    )

    zone_data = zones[zones["Zone"] == selected_zone].iloc[0]

    st.subheader(f"AI Analysis — {selected_zone}")

    st.metric(
        "AI Potential Score",
        f"{zone_data['AI Potential Score']}%"
    )

    if zone_data["AI Potential Score"] >= 70:

        st.success(
            "🟢 HIGH POTENTIAL — Recommended for priority exploration."
        )

    elif zone_data["AI Potential Score"] >= 45:

        st.warning(
            "🟡 MEDIUM POTENTIAL — Additional geological validation recommended."
        )

    else:

        st.error(
            "🔴 LOW POTENTIAL — Lower exploration priority."
        )

    st.info(
        "⚠️ Scientific Note: Satellite observations do not directly "
        "detect underground manganese. They provide surface and "
        "environmental indicators combined with geological evidence."
    )

# ==================================================
# PAGE 3 — PRODUCTION INTELLIGENCE
# ==================================================

elif page == "📈 Production Intelligence":

    st.header("📈 Production Intelligence")

    st.write(
        "Historical production data combined with predictive analysis "
        "to identify possible shortfalls."
    )

    forecast_months = pd.date_range(
        "2026-01-01",
        periods=6,
        freq="ME"
    )

    forecast = [780, 770, 790, 810, 840, 870]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=months,
        y=production,
        mode="lines+markers",
        name="Historical Production"
    ))

    fig.add_trace(go.Scatter(
        x=forecast_months,
        y=forecast,
        mode="lines+markers",
        name="AI Forecast"
    ))

    fig.add_trace(go.Scatter(
        x=list(months) + list(forecast_months),
        y=[900] * 18,
        mode="lines",
        name="Production Target",
        line=dict(dash="dash")
    ))

    fig.update_layout(
        title="Production Forecast vs Target",
        xaxis_title="Time",
        yaxis_title="Production (Tonnes)",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Target Production", "900 tonnes")
    col2.metric("Predicted Production", "780 tonnes")
    col3.metric("Shortfall Risk", "HIGH")

    st.error(
        "🚨 EARLY WARNING: Production is predicted to remain below target."
    )

# ==================================================
# PAGE 4 — RISK INTELLIGENCE
# ==================================================

elif page == "⚠️ Risk Intelligence":

    st.header("⚠️ AI Production Risk Intelligence")

    st.write(
        "Adjust the operational conditions and let MineSight AI "
        "evaluate the production risk."
    )

    col1, col2 = st.columns(2)

    with col1:

        equipment = st.slider(
            "🚜 Equipment Availability (%)",
            0, 100, 65
        )

        rainfall = st.slider(
            "🌧️ Rainfall Risk (%)",
            0, 100, 70
        )

    with col2:

        production_efficiency = st.slider(
            "📈 Production Efficiency (%)",
            0, 100, 75
        )

        blasting_delay = st.slider(
            "💥 Blasting Delay Risk (%)",
            0, 100, 40
        )

    if st.button("🧠 Analyze Mining Risk"):

        risk_score = (
            (100 - equipment) * 0.30 +
            rainfall * 0.25 +
            (100 - production_efficiency) * 0.30 +
            blasting_delay * 0.15
        )

        st.divider()

        st.subheader("🤖 AI Risk Analysis")

        st.metric("Risk Score", f"{risk_score:.1f}%")

        if risk_score >= 60:

            st.error("🔴 CRITICAL RISK")

        elif risk_score >= 35:

            st.warning("🟡 MEDIUM RISK")

        else:

            st.success("🟢 LOW RISK")

        st.subheader("🔍 Key Risk Factors")

        factors = []

        if equipment < 70:
            factors.append("🚜 Reduced equipment availability")

        if rainfall > 60:
            factors.append("🌧️ High weather disruption probability")

        if production_efficiency < 80:
            factors.append("📉 Production efficiency below expected level")

        if blasting_delay > 50:
            factors.append("💥 Significant blasting delay risk")

        if factors:
            for factor in factors:
                st.write("•", factor)

        else:
            st.write("No major operational risk factors detected.")

# ==================================================
# PAGE 5 — ACTION INTELLIGENCE
# ==================================================

elif page == "💡 Action Intelligence":

    st.header("💡 AI Action Intelligence")

    st.write(
        "MineSight AI converts detected risks into recommended "
        "corrective actions."
    )

    st.error("🚨 CURRENT STATUS: HIGH PRODUCTION SHORTFALL RISK")

    st.subheader("🤖 Recommended Actions")

    actions = [
        (
            "🚜 Equipment Strategy",
            "Deploy backup equipment and schedule preventive maintenance."
        ),
        (
            "🌧️ Weather Strategy",
            "Adjust excavation schedules based on weather risk."
        ),
        (
            "📅 Production Strategy",
            "Prioritize high-efficiency mining zones and optimize scheduling."
        )
    ]

    for title, description in actions:

        with st.expander(title):
            st.write(description)

    st.divider()

    st.subheader("👷 Human-in-the-Loop Validation")

    decision = st.radio(
        "Mining Expert Decision",
        [
            "Approve AI Recommendation",
            "Modify Recommendation",
            "Reject Recommendation"
        ]
    )

    if st.button("Submit Expert Feedback"):

        st.success(
            f"Expert feedback recorded: {decision}"
        )

        st.info(
            "🔄 Feedback can be used to continuously improve future AI recommendations."
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "MineSight AI © 2026 | From Reactive Mining → Predictive Mining → Intelligent Mining"
)