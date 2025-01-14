
# Active Passcards Tracker

This Django application is designed to manage and track access passes for individuals. It provides functionality to monitor active passes, analyze visits, and display information about pass usage.

---

## Features

- **Active Pass Tracking:** Displays a list of individuals with active passes.
- **Visit Details:** Shows detailed information about visits for each pass.
- **Unclosed Visits:** Provides a summary of visits where the individual has not yet left.

---

## Prerequisites

- Python 3.6 or later
- PostgreSQL database
- Required Python packages specified in `requirements.txt`

---

## Installation and Setup

### 1. Clone the Repository
Download or clone the repository to your local machine:
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Create a Virtual Environment
(Optional) It is recommended to use a virtual environment to avoid package conflicts:
```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies
Install all required dependencies specified in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Ensure your PostgreSQL server is running and create a database with the following settings (or modify `settings.py` with your database credentials):
- **Host:** `checkpoint.devman.org`
- **Port:** `5434`
- **Database Name:** `checkpoint`
- **User:** `guard`
- **Password:** `osim5`

Update the `SECRET_KEY` in `settings.py`:
```python
SECRET_KEY = 'your_secret_key_here'
```

### 5. Apply Migrations
Apply the database migrations to set up the required tables:
```bash
python manage.py migrate
```

### 6. Run the Server
Start the Django development server:
```bash
python manage.py runserver 0.0.0.0:8000
```

---

## Usage

- Access the application in your browser at `http://localhost:8000/`.
- Navigate through the following views:
  - **Active Passcards View:** `/` - Displays active passcards.
  - **Storage Information View:** `/storage_information` - Shows unclosed visits.
  - **Passcard Info View:** `/passcard_info/<uuid:passcode>` - Displays detailed information about visits for a specific pass.

---

## Directory Structure

- `main.py`: Entry point for running the application.
- `requirements.txt`: Contains all Python package dependencies.
- `project/settings.py`: Configuration file for the Django project.
- `project/urls.py`: URL routing for the application.
- `datacenter/models.py`: Defines database models for passcards and visits.
- `datacenter/views/`: Contains views to handle different functionalities.

---

## Example Usage

### Access Active Passcards
Visit the root URL to view a list of individuals with active passes.

### View Storage Information
Navigate to `/storage_information` to see details of unclosed visits.

### Check Passcard Information
Use `/passcard_info/<uuid:passcode>` to analyze visit details for a specific pass.

---

## Notes

- This application is for demonstration purposes and should not be used in production without proper security measures.
- Replace the default credentials and `SECRET_KEY` with secure values for your setup.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or fixes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.