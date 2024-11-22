# filehandling

File Handling is a mechanism for creating, reading, updating and deleting files. It is crucial feature for managing data storage and retrieval, enabling applications to persist data between program executions. File Handling is crucial for managing, processing, and storing data in business applications. 

# key operations in file handling

1. Opening a file : Files can be opened using the built-in open() function.

   # file = open('filename.txt','mode')
   mode can be read(r), write(w), append(a) and create(x).

2. Reading a file : Use read(), readline(), or readlines() to fetch file content.

   # with open('data.txt','r') as file:
   # content = file.read()
   # print(content)

3. Writing to a file : Use write() or writelines() to write data.

   # with open('data.txt','w') as file:
   # file.write("Hello, World!")

4. Appending to a file : Opens the file in append mode to add data without overwriting existing content.

   # with open('data.txt','a') as file:
   # file.write("Hello again")

5. Closing a file : Ensures all resources tied to the file are released.

   # file = open('filename.txt','r')
   # print(file.read())
   # file.close()

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

# code snippet example(Employee Performance Report)

A company maintains employee performance data in a text file(performance.txt) that contains detials such as empid, name and monthly performance score. The company needs to extract and validate the performance data, identify top performers and calculate the average performance score, and save the report in a file(report.txt), including top performers and the average score.


def generate_performance_report(input_file, output_file):
    """
    Reads employee performance data from the input file, analyzes it to find top performers 
    and average scores, and writes a detailed report to the output file.
    """
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        total_score = 0
        count = 0
        top_performers = []
        performance_data = []

        for line in lines:
            data = line.strip().split(',')
            if len(data) != 3:  # Expecting format: EmployeeID,Name,Score
                continue

            emp_id, name, score = data
            try:
                score = float(score)
                total_score += score
                count += 1
                performance_data.append((emp_id, name, score))
                if score >= 90:  # Top performer threshold
                    top_performers.append(f"{emp_id},{name},{score:.2f}")
            except ValueError:
                print(f"Invalid score format in line: {line}")

        average_score = total_score / count if count > 0 else 0

        with open(output_file, 'w') as outfile:
            outfile.write("Employee Performance Report\n")
            outfile.write("----------------------------\n")
            outfile.write("Top Performers:\n")
            outfile.write("\n".join(top_performers) if top_performers else "No top performers.\n")
            outfile.write(f"\n\nAverage Performance Score: {average_score:.2f}\n")

        print(f"Performance report generated successfully in '{output_file}'.")
        print(f"Average Score: {average_score:.2f}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    input_file = "performance.txt"  
    output_file = "report.txt"     
    generate_performance_report(input_file, output_file)


