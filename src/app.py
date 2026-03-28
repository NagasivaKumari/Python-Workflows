import streamlit as st
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import plotly.graph_objects as go

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Health Risk AI", layout="wide")

# ------------------ UI ------------------
st.markdown(
    """
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.title {
    font-size: 45px;
    text-align: center;
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { color: white; }
    to { color: cyan; }
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.stButton>button {
    background: linear-gradient(45deg, #00c6ff, #0072ff);
    color: white;
    height: 50px;
    width: 100%;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="title">❤️ Health Risk Prediction System</div>', unsafe_allow_html=True
)

# ------------------ LOAD DATASET ------------------
DATASET_PATH = os.path.join(os.path.dirname(__file__), "Dataset.csv")
df = pd.read_csv(DATASET_PATH, encoding="latin1")
df["Chronic Disease History"] = df["Chronic Disease History"].fillna("None")

# ------------------ PREPROCESS ------------------
X = df.drop("Health Risk Level", axis=1)
y = df["Health Risk Level"]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_encoded = pd.get_dummies(
    X, columns=["Gender", "Smoking Status", "Chronic Disease History"]
)
feature_columns = X_encoded.columns

# ------------------ TRAIN TEST ------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y_encoded, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ------------------ MODELS ------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(max_depth=5),
    "Random Forest": RandomForestClassifier(n_estimators=100),
}

trained_models = {}
accuracies = {}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    trained_models[name] = model
    y_pred = model.predict(X_test_scaled)
    accuracies[name] = accuracy_score(y_test, y_pred)

# ------------------ INPUT UI (NO LIMITS) ------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.text_input("Age 👤")
    bmi = st.text_input("BMI ⚖")
    gender = st.selectbox("Gender ⚧", ["Male", "Female", "Other"])
    smoking = st.selectbox("Smoking 🚬", ["Never", "Former", "Current"])

with col2:
    alcohol = st.text_input("Alcohol 🍺")
    activity = st.text_input("Physical Activity 🏃")
    sleep = st.text_input("Sleep 😴")
    disease = st.selectbox(
        "Disease 🏥", ["None", "Diabetes", "Heart Disease", "Hypertension"]
    )
    stress = st.text_input("Stress 😵")

st.markdown("</div>", unsafe_allow_html=True)


# ------------------ EXPLANATION ------------------
def explain_risk(user_data):

    reasons = []

    if user_data["Age"] > 60:
        reasons.append("Age above 60 increases risk")

    if user_data["BMI"] > 30:
        reasons.append("High BMI (Obesity)")

    if user_data["Smoking Status"] == "Current":
        reasons.append("Smoking increases disease risk")

    if user_data["Alcohol Consumption (per week)"] > 12:
        reasons.append("High alcohol consumption")

    if user_data["Physical Activity (hours/week)"] < 2:
        reasons.append("Low physical activity")

    if user_data["Sleep Duration (hours/day)"] < 6:
        reasons.append("Poor sleep")

    if user_data["Stress Level (1-10)"] >= 8:
        reasons.append("High stress")

    if user_data["Chronic Disease History"] != "None":
        reasons.append("Existing chronic disease")

    return reasons


# ------------------ GAUGE ------------------
def show_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Health Risk Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "steps": [
                    {"range": [0, 33], "color": "#00ff88"},
                    {"range": [33, 66], "color": "#ffaa00"},
                    {"range": [66, 100], "color": "#ff2e2e"},
                ],
            },
        )
    )
    fig.update_layout(paper_bgcolor="black", font={"color": "white"})
    st.plotly_chart(fig, use_container_width=True)


# ------------------ PREDICT ------------------
if st.button("🚀 Analyze Health Risk"):

    try:
        user_data = {
            "Age": float(age),
            "Gender": gender,
            "BMI": float(bmi),
            "Smoking Status": smoking,
            "Alcohol Consumption (per week)": float(alcohol),
            "Physical Activity (hours/week)": float(activity),
            "Sleep Duration (hours/day)": float(sleep),
            "Chronic Disease History": disease,
            "Stress Level (1-10)": float(stress),
        }

        input_df = pd.DataFrame([user_data])
        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)
        input_scaled = scaler.transform(input_encoded)

        # MODEL OUTPUT
        st.markdown("### 🤖 Model Predictions")
        for name, model in trained_models.items():
            pred = model.predict(input_scaled)
            label = label_encoder.inverse_transform(pred)[0]
            prob = max(model.predict_proba(input_scaled)[0]) * 100
            st.write(f"{name} → {label} ({round(prob, 2)}%)")

        # FINAL RESULT
        rf_model = trained_models["Random Forest"]
        score = max(rf_model.predict_proba(input_scaled)[0]) * 100

        st.markdown("### 🎯 Final Result")

        if score < 33:
            st.success(f"🟢 LOW RISK ({round(score, 2)}%)")
        elif score < 66:
            st.warning(f"🟡 MODERATE RISK ({round(score, 2)}%)")
        else:
            st.error(f"🔴 HIGH RISK ({round(score, 2)}%)")

        show_gauge(score)

        # EXPLANATION
        st.markdown("### 🧠 Explanation")
        reasons = explain_risk(user_data)

        if len(reasons) == 0:
            st.info("✔ Healthy profile. No major risks.")
        else:
            for r in reasons:
                st.write("✔", r)

    except Exception:
        st.error("⚠ Please enter valid numeric values!")

# ------------------ ACCURACY ------------------
st.markdown("## 📊 Model Accuracy")
for name, acc in accuracies.items():
    st.write(f"{name}: {round(acc * 100, 2)}%")
