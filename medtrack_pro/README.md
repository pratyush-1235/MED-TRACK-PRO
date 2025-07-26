# medtrack_pro/medtrack_pro/README.md

# MedTrack Pro

MedTrack Pro is a Django-based application designed to help hospitals manage patient appointments and medical records in a paperless and digital format. This project utilizes MySQL as the database, HTML and CSS for the frontend, and Bootstrap for styling.

## Features

- User registration and login for patients, doctors, and admins.
- Appointment booking and management.
- Uploading and storing medical reports and prescriptions.
- User dashboards for patients, doctors, and admins.
- Responsive design using Bootstrap.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd medtrack_pro
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Configure the database settings in `medtrack_pro/settings.py` to connect to your MySQL database.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at `http://127.0.0.1:8000/`.

## Usage

- Navigate to the login page to access your account.
- Patients can book appointments and upload medical reports.
- Doctors can manage their appointments and view patient records.
- Admins can manage doctors and view all appointments.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.