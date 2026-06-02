from pathlib import Path


def save_report(topic, report_content):
    file_name = topic.lower().replace(" ", "_")
    report_file = Path(f"reports/{file_name}.md")

    report_file.write_text(report_content, encoding="utf-8")

    return report_file