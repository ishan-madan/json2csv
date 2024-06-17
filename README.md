 # $\textsf{\color{skyblue} JSON 2 CSV}$

## $\textsf{\color{lightgreen} Description}$
JSON 2 CSV is a python program that simplifies the conversion of JSON files to the CSV format. It leverages the powerful `pandas` library for data manipulation and the `os` and `json` libraries for file handling and JSON parsing, respectively.

## $\textsf{\color{lightgreen} Key Features}$

### 1. Effortless Conversion
- Convert your JSON data to CSV format with a single script, streamlining your data processing workflow.

### 2. Library Agnostic JSON Support:
- Handles various JSON structures, making it adaptable to diverse data formats.

### 3. Cross-Platform Compatibility:
- Designed using standard Python libraries, ensuring compatibility across different operating systems.
  
## $\textsf{\color{lightgreen} Languages and Libraries Used}$
- Python
- Pandas
- os
- json

# $\textsf{\color{skyblue} JSON 2 CSV Program Walkthrough}$

## $\textsf{\color{lightgreen} Cloning the Repository}$

1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to clone the repository.
   - Run the following command:
     ```
     git clone <repository_url>
     ```
     Replace `<repository_url>` with the actual URL of the GitHub repository.

## $\textsf{\color{lightgreen} Setting Up the Environment}$

2. **Environment Setup:**
   - Ensure you have Python installed on your system. You can check by running:
     ```
     python --version
     ```
   - If you dont have it installed, head to [python.org](python.org) to install. Alternatively, if you have homebrew installed, type
     ```
     brew install python
     ```
     into the command window.
   - Next, open a virtual environment and install pandas by using the following commands.
     <br/>
       - MacOS:
         ```
         python -m venv ~/myenv
         myenv\Scripts\activate.bat
         pip install pandas  
         ```
       - Windows:
         ```
         python -m venv myenv
         source ~/myenv/bin/activate
         pip install pandas  
         ```
       - Linux:
         ```
         python -m venv myenv
         source ~/myenv/bin/activate
         pip install pandas  
         ```
   - Finally, navigate to the folder where the script has been cloned
     ```
      cd ~/path/to/cloned/repo/
     ```

## $\textsf{\color{lightgreen} Program Walkthrough}$

3. **Program Walkthrough:**
   - **Step 1: Opening the Program**
     - Open the project folder and navigate to the `json_to_csv.py` file.
    <p align="center">
   <img src="ReadMe%20Images/step1.png" height="60%" width="60%" alt="Opening the Program"/>
   </p>

   - **Step 2: File Path Information**
     - Input the path to the parent filder, name of the `json` file, and the desired name of the `csv` file.
   <p align="center">
   <img src="ReadMe%20Images/step2.png" height="60%" width="60%" alt="Filling in File Path Information"/>
   </p>

   - **Step 3: Run the Program**
     - In the command window where you set up the environment, run
       ```
       python json_to_csv.py
       ```
   <p align="center">
   <img src="ReadMe%20Images/step3.png" height="40%" width="40%" display="inline-block" alt="Running the program"/>
   </p>

   - **Step 4: Convert**
     - The program will convert your `json` file and save it as a `csv` file to that same folder!
   <p align="center">
   <img src="ReadMe%20Images/step4.png" height="60%" width="60%" alt="Convert JSON to CSV"/>
   </p>



