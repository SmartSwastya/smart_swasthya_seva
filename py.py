import os
import json

# Function to scan project structure and collect file data
def scan_project_structure(root_dir):
    project_structure = {}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip __pycache__ directories
        if '__pycache__' in dirnames:
            dirnames.remove('__pycache__')

        # Collect data about files
        project_structure[dirpath] = filenames

    return project_structure

# Function to check for missing files (e.g., urls.py, views.py)
def check_dependencies(project_structure):
    missing_files = []
    
    for dirpath, files in project_structure.items():
        if 'urls.py' not in files:
            missing_files.append(f"Missing 'urls.py' in {dirpath}")
        if 'views.py' not in files:
            missing_files.append(f"Missing 'views.py' in {dirpath}")
    
    return missing_files

# Function to auto-repair missing files
def auto_repair_missing_files(missing_files):
    for file in missing_files:
        # Extract the correct file name and path
        file_path = file.split(" in ")[-1].strip().replace("'", "")
        
        # Check if the file exists and create it if missing
        try:
            if file_path.endswith('.py') or file_path.endswith('.html'):  # You can extend it to other file types
                # If the file does not exist, create a new one
                if not os.path.exists(file_path):
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directories if not exist
                    with open(file_path, 'w') as f:
                        f.write(f"# Auto-generated missing file: {os.path.basename(file_path)}\n")
                    print(f"Created missing file: {file_path}")
        except Exception as e:
            print(f"Error creating {file_path}: {str(e)}")

# Function to generate project report
def generate_report(project_structure, missing_files):
    report = {
        "project_structure": project_structure,
        "missing_files": missing_files
    }

    report_path = "D:\smartswasthyawebsite\smart_swasthya_seva/project_report.json"
    with open(report_path, 'w') as report_file:
        json.dump(report, report_file, indent=4)

    print(f"Report generated successfully at {report_path}")

# Main function
def main():
    root_dir = "D:\smartswasthyawebsite\smart_swasthya_seva"
    
    print("Scanning project structure...")
    project_structure = scan_project_structure(root_dir)

    print("Checking dependencies...")
    missing_files = check_dependencies(project_structure)

    if missing_files:
        print(f"Found {len(missing_files)} missing files. Attempting to auto-repair...")
        auto_repair_missing_files(missing_files)
    else:
        print("No missing files detected.")

    generate_report(project_structure, missing_files)

if __name__ == "__main__":
    main()
