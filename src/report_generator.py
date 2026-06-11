from research_analyzer import analyze_topic


def create_report_content(topic):
    analysis = analyze_topic(topic)

    return f"""
# Market Research Report

Topic: {topic}

## Executive Summary
This report focuses on {topic}, which belongs to the {analysis['market_type']} sector.

## Market Overview
The {analysis['market_type']} market is currently being evaluated.

## Competitor Analysis
Key competitors in the {topic} market will be identified.

## Opportunities
{analysis['main_opportunity']}

## Risks
{analysis['main_risk']}
"""