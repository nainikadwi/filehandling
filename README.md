# filehandling

File Handling is a mechanism for creating, reading, updating and deleting files. It is crucial feature for managing data storage and retrieval, enabling applications to persist data between program executions. File Handling is crucial for managing, processing, and storing data in business applications. 

# key operations in file handling

1. Opening a file : Files can be opened using the built-in open() function.

   file = open('filename.txt','mode')

   mode can be read(r), write(w), append(a) and create(x).

3. Reading a file : Use read(), readline(), or readlines() to fetch file content.

   with open('data.txt','r') as file:

   content = file.read()

   print(content)

5. Writing to a file : Use write() or writelines() to write data.

   with open('data.txt','w') as file:

   file.write("Hello, World!")

7. Appending to a file : Opens the file in append mode to add data without overwriting existing content.

   with open('data.txt','a') as file:

   file.write("Hello again")

9. Closing a file : Ensures all resources tied to the file are released.

   file = open('filename.txt','r')

   print(file.read())

   file.close()

# advantages of file handling

1. Files allow data to be saved and retrieved across multiple program executions, ensuring long-term storage.
2. Automation processes like maintaining logs, generating reports, and tracking operations.
3. Handles different types of data(txt,csv,json etc.).
4. Files can be accessed easily and modified using standard operations like reading, writing, appending or deleting.
5. Files can be transferred between systems and applications , enabling seamless data exchange.
6. Files can be used for creating backups and retrieving critical data in case of system failure.
7. Facilitates the storage and organization of large datasets, allowing sorting, searching and processing as required.

# disadvantages of file handling

1. File systems may lack encryption or access control, making them vulnerable to unauthorzied access or data breaches.
2. Files are less efficient for large-scale operations compared to databases when dealing with relational or hierarchial data.
3. Simultaneous access by multiple users or programs can lead to data corruption or overwriting.
4. Manual file handling can result in duplicate or inconsistent data across files.
5. File systems lack built-in recovery features, making it harder to retrieve data lost due to accident deletion or corruption.
6. Accessing and processing large files can be slower than querying data from a database.
7. Files require regular maintenance for updates, archiving, and deletion which can be labor-intensive.

# code description

This Python code implements a menu-driven attendance management system that allows real-time logging and viewing of employee attendance. It uses CSV files to store attendance data and logging to record all application activities, errors, and user interactions for traceability and debugging.

The key features include:
	1.	Logging Attendance: Employees can log their attendance with details such as Employee ID, Name, and Status (e.g., Present/Absent).
	2.	Viewing Attendance: Users can view all recorded attendance records, which are displayed in the console and logged to a log file.
	3.	Exception Handling: Specific error handling for scenarios like file-related issues and invalid input.
	4.	Log File for Audit: All actions and errors are recorded in attendance_system.log for tracking and debugging.

# code objective

The objective of this code is to provide a simple, user-friendly, and reliable attendance management application that can:
	•	Serve real-world company needs for maintaining attendance records in a structured manner.
	•	Use logging to maintain a permanent audit trail of user interactions and system errors.
	•	Utilize exception handling to ensure robustness and user guidance in error scenarios.

This approach ensures the system is efficient, traceable, and ready for real-life business use cases.
