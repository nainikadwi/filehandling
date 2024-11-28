import csv
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler for log file
file_handler = logging.FileHandler("attendance_system.log")
file_handler.setLevel(logging.INFO)

# Console handler for console output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Log message format
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Constant for the CSV file name
ATTENDANCE_FILE = "attendance_records.csv"


def initialize_file():
    """
    Initialize the attendance file.

    Checks if the attendance CSV file exists. If not, it creates
    the file and writes the header row.

    Returns:
        None
    """
    try:
        with open(ATTENDANCE_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Employee ID", "Name", "Status"])
        logging.info(f"{ATTENDANCE_FILE} created successfully.")
    except FileExistsError as e:
        logging.info(f"{ATTENDANCE_FILE} already exists. Error: {e}")


def write_to_csv(data: list):
    """
    Write data to the attendance CSV file.

    Args:
        data (list): A list of data to write to the CSV file, where each element
                     corresponds to a row (e.g., [Timestamp, Employee ID, Name, Status]).

    Returns:
        None
    """
    try:
        with open(ATTENDANCE_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        logging.info(f"Attendance logged successfully: {data}")
    except IOError as e:
        logging.error(f"Error writing to file: {e}")


def read_from_csv() -> list:
    """
    Read all data from the attendance CSV file.

    Returns:
        list: A list of rows read from the CSV file, where each row is a list of strings.
    """
    try:
        with open(ATTENDANCE_FILE, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError as e:
        logging.error(f"File not found error: {e}")
        return []


def log_attendance(employee_id: str, name: str, status: str):
    """
    Log attendance details for an employee.

    Args:
        employee_id (str): The ID of the employee.
        name (str): The name of the employee.
        status (str): The attendance status (e.g., Present, Absent).

    Returns:
        None
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = [timestamp, employee_id, name, status]
    write_to_csv(data)


def view_attendance():
    """
    Display all attendance records from the CSV file in the log.

    Returns:
        None
    """
    attendance_data = read_from_csv()

    if len(attendance_data) <= 1:
        logging.info("No attendance records found.")
    else:
        logging.info("Displaying all attendance records:")
        for row in attendance_data:
            logging.info(", ".join(row))


# Main application logic
def main():
    """
    Main function for the attendance system application.

    Provides a menu-driven interface for logging attendance and viewing attendance records.

    Returns:
        None
    """
    initialize_file()
    while True:
        try:
            logging.info("\n--- Attendance System ---\n1. Log Attendance\n2. View Attendance\n3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Employee Name: ")
                status = input("Enter Status (Present/Absent): ")
                log_attendance(employee_id, name, status)
            elif choice == 2:
                view_attendance()
            elif choice == 3:
                logging.info("Application exited by the user.")
                break
            else:
                logging.warning("Invalid choice entered.")
        except ValueError as ve:
            logging.error(f"Invalid input! Please enter a number. Error: {ve}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")


# Run the application
if __name__ == "__main__":
    main()
