def analyze_topic(topic):
    topic_lower = topic.lower()

    if "healthcare" in topic_lower:
        return {
            "market_type": "Healthcare Technology",
            "main_opportunity": "Improving patient care through automation and AI.",
            "main_risk": "Data privacy and regulatory compliance."
        }

    elif "electric vehicle" in topic_lower:
        return {
            "market_type": "Electric Mobility",
            "main_opportunity": "Growing adoption of sustainable transportation.",
            "main_risk": "Battery supply chain challenges."
        }

    else:
        return {
            "market_type": "General Market",
            "main_opportunity": "Emerging market opportunities.",
            "main_risk": "Market uncertainty."
        }