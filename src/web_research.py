import requests


def get_web_research(topic):
    url = f"https://api.duckduckgo.com/?q={topic}&format=json"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        abstract = data.get("Abstract", "")

        if abstract:
            return abstract

        return f"No detailed research found for {topic}."

    except Exception as e:
        return f"Research error: {e}"