import csv
import logging
from datetime import datetime

# Configure logging for the system
logging.basicConfig(
    filename="attendance_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# File name for attendance CSV
ATTENDANCE_FILE = "attendance_records.csv"

# Function to initialize the attendance file
def initialize_file():
    """
    Ensures the attendance file is created with a header if it doesn't exist.
    """
    try:
        with open(ATTENDANCE_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Employee ID", "Name", "Status"])
        logging.info(f"{ATTENDANCE_FILE} created successfully.")
    except FileExistsError:
        logging.info(f"{ATTENDANCE_FILE} already exists.")

# Function to log attendance
def log_attendance(employee_id, name, status):
    """
    Logs an employee's attendance in the CSV file.
    """
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(ATTENDANCE_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, employee_id, name, status])
        logging.info(f"Attendance logged for Employee {employee_id} ({name}): {status}")
        print(f"Attendance logged for Employee {employee_id} ({name}): {status}")
    except Exception as e:
        logging.error(f"Failed to log attendance for Employee {employee_id} ({name}): {e}")
        print("An error occurred while logging attendance. Please try again.")

# Function to view attendance logs
def view_attendance():
    """
    Reads and displays the attendance records from the CSV file.
    """
    try:
        with open(ATTENDANCE_FILE, 'r') as file:
            reader = csv.reader(file)
            attendance_data = list(reader)

        if len(attendance_data) <= 1:  # Only header exists
            logging.info("No attendance records found.")
            print("No attendance records found.")
        else:
            logging.info("Displaying all attendance records:")
            print("\n--- Attendance Records ---")
            for row in attendance_data:
                print(", ".join(row))
                logging.info(", ".join(row))

    except FileNotFoundError:
        logging.warning("No attendance records file found. Please log attendance first.")
        print("No attendance records file found. Please log attendance first.")
    except Exception as e:
        logging.error(f"Error reading attendance logs: {e}")
        print("An error occurred while viewing attendance logs. Please try again.")

# Main function for user interaction
def main():
    """
    Main function to handle user input for attendance management.
    """
    initialize_file()

    logging.info("Attendance Management System Started.")
    while True:
        print("\n--- Main Menu ---")
        print("1. Log Attendance")
        print("2. View Attendance Logs")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1/2/3): ").strip())

            if choice == 1:
                try:
                    # Take user input for attendance
                    employee_id = input("Enter your Employee ID: ").strip()
                    name = input("Enter your Name: ").strip()
                    status = input("Enter your Attendance Status (Present/Absent): ").strip().capitalize()

                    # Validate status
                    if status not in ["Present", "Absent"]:
                        raise ValueError("Invalid status. Please enter 'Present' or 'Absent'.")

                    # Log attendance
                    log_attendance(employee_id, name, status)

                except ValueError as ve:
                    logging.warning(f"Invalid input: {ve}")
                    print(f"Invalid input: {ve}")
                except Exception as e:
                    logging.error(f"Error during input: {e}")
                    print("An error occurred. Please try again.")

            elif choice == 2:
                view_attendance()

            elif choice == 3:
                logging.info("Exiting the Attendance Management System. Goodbye!")
                print("Exiting the Attendance Management System. Goodbye!")
                break

            else:
                logging.warning("Invalid menu choice entered. Please enter 1, 2, or 3.")
                print("Invalid choice. Please enter 1, 2, or 3.")

        except ValueError:
            logging.warning("Invalid menu choice entered.")
            print("Invalid choice. Please enter a number (1/2/3).")
        except Exception as e:
            logging.error(f"Unexpected error in the main loop: {e}")
            print("An unexpected error occurred. Please try again.")
            
if __name__ == "__main__":
    main()