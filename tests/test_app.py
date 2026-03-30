import sys
import os
import importlib.util

# Dynamically import explain_risk from app.py
spec = importlib.util.spec_from_file_location(
    "app", os.path.join(os.path.dirname(__file__), "../src/app.py")
)
app = importlib.util.module_from_spec(spec)
sys.modules["app"] = app
spec.loader.exec_module(app)


def test_explain_risk():
    user_data = {
        "Age": 65,
        "BMI": 32,
        "Smoking Status": "Current",
        "Alcohol Consumption (per week)": 15,
        "Physical Activity (hours/week)": 1,
        "Sleep Duration (hours/day)": 5,
        "Stress Level (1-10)": 9,
        "Chronic Disease History": "Diabetes",
    }
    reasons = app.explain_risk(user_data)
    assert "Age above 60 increases risk" in reasons
    assert "High BMI (Obesity)" in reasons
    assert "Smoking increases risk" in reasons
    assert "High alcohol consumption" in reasons
    assert "Low physical activity" in reasons
    assert "Poor sleep" in reasons
    assert "High stress" in reasons
    assert "Existing chronic disease" in reasons
