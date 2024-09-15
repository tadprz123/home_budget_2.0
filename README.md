# Budget App

## Overview
The Budget App is a simple web application designed to help users manage their budget. It allows users to track their income and expenses, providing a clear overview of their financial situation.

## Project Structure

budget_app/ │ ├── app/ │ ├── static/ │ │ └── style.css │ ├── templates/ │ │ └── index.html │ ├── init.py │ ├── models.py │ ├── routes.py │ └── utils.py │ ├── data/ │ └── budget.csv │ ├── venv/ │ ├── .gitignore ├── config.py ├── requirements.txt └── run.py


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/tadprz123/home_budget_2.0
    ```
2. Navigate to the project directory:
    ```bash
    cd budget_app
    ```
3. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:
    ```bash
    python run.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000`.

## Project Files
- **app/**: Contains the main application code.
  - **static/**: Contains static files like CSS.
  - **templates/**: Contains HTML templates.
  - **__init__.py**: Initializes the application.
  - **models.py**: Defines the data models.
  - **routes.py**: Defines the application routes.
  - **utils.py**: Contains utility functions.
- **data/**: Contains the budget data in CSV format.
- **venv/**: Virtual environment directory.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **config.py**: Configuration file for the application.
- **requirements.txt**: Lists the dependencies required by the application.
- **run.py**: Entry point to run the application.

## Contributing
Feel free to fork this project, make improvements, and submit pull requests. Any contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
