from pathlib import Path


def get_user_topic():
    return input("Enter a research topic: ")


def create_report_content(topic):
    return f"""
# Market Research Report

Topic: {topic}

## Executive Summary
This report focuses on {topic}.

## Market Overview
An overview of the {topic} market will be analyzed.

## Competitor Analysis
Key competitors in the {topic} market will be identified.

## Opportunities
Potential opportunities within {topic} will be explored.

## Risks
Potential risks and challenges related to {topic} will be assessed.
"""


def save_report(topic, report_content):
    file_name = topic.lower().replace(" ", "_")
    report_file = Path(f"reports/{file_name}.md")

    report_file.write_text(report_content, encoding="utf-8")

    return report_file


def main():
    print("\n=== Market Research Copilot ===\n")

    topic = get_user_topic()

    report_content = create_report_content(topic)

    report_file = save_report(topic, report_content)

    print("\nReport created successfully!")
    print(f"Saved to: {report_file}")


if __name__ == "__main__":
    main()