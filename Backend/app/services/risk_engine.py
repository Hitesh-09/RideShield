def calculate_risk(city, rainfall, temp, aqi):

    risk_score = 0

    # 🌧 Rain risk
    if rainfall > 5:
        risk_score += 2
    elif rainfall > 2:
        risk_score += 1

    # 🌡 Heat risk
    if temp > 40:
        risk_score += 2
    elif temp > 35:
        risk_score += 1

    # 🌫 AQI risk
    if aqi >= 4:
        risk_score += 2
    elif aqi >= 3:
        risk_score += 1

    # Final decision
    if risk_score >= 4:
        return {"risk": "high", "premium": 50}
    elif risk_score >= 2:
        return {"risk": "medium", "premium": 30}
    else:
        return {"risk": "low", "premium": 20}
