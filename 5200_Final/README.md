# PWW Database Viewer

A Streamlit application for viewing and managing PWW database data.

## Features
- View database records
- Search functionality
- Export data to CSV
- Real-time data updates

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pww-database-viewer.git
cd pww-database-viewer
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Configure your database settings in `app.py`:
```python
host="localhost"
user="root"
password="dev"
database="PWW_DATABASE"
```

4. Run the application:
```bash
streamlit run app.py
```

## Requirements
- Python 3.7+
- MySQL
- XAMPP (for local development)

## Configuration
Make sure your XAMPP MySQL service is running and the PWW_DATABASE is properly configured.
