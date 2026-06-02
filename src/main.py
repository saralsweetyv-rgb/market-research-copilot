from report_generator import create_report_content
from file_manager import save_report

def get_user_topic():
    return input("Enter a research topic: ")


def main():
    print("\n=== Market Research Copilot ===\n")

    topic = get_user_topic()

    report_content = create_report_content(topic)

    report_file = save_report(topic, report_content)

    print("\nReport created successfully!")
    print(f"Saved to: {report_file}")


if __name__ == "__main__":
    main()