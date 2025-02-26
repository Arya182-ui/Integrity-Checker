from monitor import start_monitoring
from visualization import plot_changes
from report_generator import generate_pdf_report

if __name__ == "__main__":
    path = input("Enter directory to monitor: ")
    start_monitoring(path)

    # Visualization and report generation
    plot_changes()
    generate_pdf_report()
