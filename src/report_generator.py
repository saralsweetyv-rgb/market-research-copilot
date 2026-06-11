from research_analyzer import analyze_topic


def create_report_content(topic):
    analysis = analyze_topic(topic)

    return f"""
# Market Research Report

## Topic
{topic}

## Executive Summary
This report focuses on {topic}, which belongs to the {analysis['market_type']} sector.

## Market Overview
The {analysis['market_type']} market is currently being evaluated for growth opportunities and challenges.

## Industry Trends
Key trends are shaping the future of the {analysis['market_type']} industry.

## Competitor Analysis
Leading competitors and market participants should be analyzed for strategic insights.

## Opportunities
{analysis['main_opportunity']}

## Risks
{analysis['main_risk']}

## Strategic Recommendations
Organizations should monitor market developments, evaluate emerging opportunities, and proactively manage identified risks.

## Conclusion
The {analysis['market_type']} sector presents both opportunities and challenges that require ongoing analysis.
"""