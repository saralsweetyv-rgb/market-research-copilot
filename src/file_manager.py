from pathlib import Path


def save_report(topic, report_content):
    file_name = topic.lower().replace(" ", "_")
    report_file = Path(f"reports/{file_name}.md")

    final_content = f"# Market Research Copilot Report\n\n{report_content}"

    report_file.write_text(final_content, encoding="utf-8")

    return report_file