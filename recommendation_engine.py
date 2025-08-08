def get_recommendations(heart_data, diab_data, history):
    recs = []

    if heart_data["chol"] > 240:
        recs.append("Reduce intake of fatty foods.")
    if heart_data["trestbps"] > 140:
        recs.append("Monitor your blood pressure regularly.")
    if diab_data["Glucose"] > 130:
        recs.append("Control sugar intake.")
    if diab_data["BMI"] > 30:
        recs.append("Adopt a regular workout plan.")
    if "smoke" in history.lower():
        recs.append("Consider quitting smoking.")

    recs.append("Get regular health check-ups every 6 months.")
    return recs

