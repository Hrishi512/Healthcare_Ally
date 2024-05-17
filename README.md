# Healthcare Ally
A Machine Learning project designed to assist doctors in determining the necessity of treatment for patients based on their blood analysis results.

# Project Setup and Execution

## Step 1: Clone the Repository or Download the ZIP

Clone the repository or download the ZIP file from the following Git link:
`<link>`

## Step 2: Folder Structure

Ensure your project has the following folder structure:

![Folder Structure](static/folder_structure.png)

## Step 3: Open and Run the Notebook

1. Open the `sourcecode.ipynb` file.
2. Run each cell in the Jupyter Notebook or VScode.

## Step 4: Trained Model Creation

After executing `sourcecode.ipynb`, the `model.joblib` file will be created inside the `models` folder, which is the trained model for this project.

## Step 5: Running the Flask App

### Using VS Code

1. Open the project in VS Code.
2. Locate `app.py`, which contains the Flask code for designing the user interface and uses HTML for webpage design.
3. Before running the `app.y` ensure `model.joblib` is present in the models directory and is updated.
4. Run `app.py` in VS Code.
5. The terminal at the bottom of the VS Code screen will show a local connection for the webpage.
6. Hold `Ctrl` + `click` to open the webpage in your default browser or you can copy and paste it your desired browser.
7. You can now see the user interface for entering the requested data. After inputting the data, click "Submit" to predict the output using the pre-trained model `model.joblib`.
8. Once you finish. `Ctrl` + `C` on the terminal to stop the application `app.py`.

![VScode terminal](static/vs_code.png)

### Using Command Prompt or PowerShell

1. Open the Command Prompt or PowerShell from the project folder.
2. Before running the `app.py` ensure `model.joblib` is present in the models directory and is updated.
3. Run the following command:
   ```sh
   python app.py
4. After running the command, a local connection link for the webpage will be displayed. Click on the link to open the webpage in your default browser or copy and paste it your desired browser. Input your data, and the output will be predicted using the pre-trained model.
5. Once done `Ctrl` + `C` on the terminal to stop the application `app.py`.

![Command prompt terminal](static/cmd.png)

## Sample data for testing

### Male sample data
| HAEMATOCRIT | HAEMOGLOBINS | ERYTHROCYTE | LEUCOCYTE | THROMBOCYTE | MCH  | MCHC | MCV  | AGE | SEX |
|--------------|--------------|-------------|-----------|-------------|------|------|------|-----|-----|
| 50.5         | 17.2         | 6.37        | 17.6      | 303         | 27   | 34.1 | 79.3 | 27  | M   |
| 43.6         | 14.2         | 5.03        | 11.1      | 252         | 28.2 | 32.6 | 86.7 | 43  | M   |


### Female sample data
| HAEMATOCRIT | HAEMOGLOBINS | ERYTHROCYTE | LEUCOCYTE | THROMBOCYTE | MCH  | MCHC | MCV  | AGE | SEX |
|--------------|--------------|-------------|-----------|-------------|------|------|------|-----|-----|
| 38.3         | 12.6         | 4.22        | 5.1       | 244         | 29.9 | 32.9 | 90.8 | 80  | F   |
| 37.7         | 12.8         | 4.21        | 5.1       | 213         | 30.4 | 34   | 89.5 | 28  | F   |
