import os
from dotenv import load_dotenv
from groq import Groq
from src.research_data import get_research_context
from src.web_research import get_web_research

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_market_analysis(topic):
    research_context = get_research_context(topic)
    web_research = get_web_research(topic)

    prompt = f"""
You are a market research analyst.

Internal Research:
{research_context}

Web Research:
{web_research}

Generate a professional market research report.

Include:

1. Executive Summary
2. Market Overview
3. Key Market Trends
4. Competitor Landscape
5. Opportunities
6. Risks
7. Strategic Recommendations
8. Conclusion

Format the response in Markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content