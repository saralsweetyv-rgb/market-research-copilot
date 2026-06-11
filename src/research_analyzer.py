from industry_data import INDUSTRIES


def analyze_topic(topic):
    topic_lower = topic.lower()

    for keyword, data in INDUSTRIES.items():
        if keyword in topic_lower:
            return data

    return {
        "market_type": "General Market",
        "main_opportunity": "Emerging market opportunities.",
        "main_risk": "Market uncertainty."
    }