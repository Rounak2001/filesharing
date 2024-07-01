# File Management app

Here we upload our own file and share it with other user.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#Features)


## Installation

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Rounak2001/File-Management-App.git
    ```


2. **Set Up a Virtual Environment (Optional but Recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Run Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a Superuser (Optional):**

    ```bash
    python manage.py createsuperuser
    ```

## Usage

Follow these instructions to run the project:

1. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

2. **Access the Admin Panel:**

    - Open a web browser and go to `http://127.0.0.1:8000/admin/`.
    - Log in with the superuser credentials created earlier.

3. **Explore the Application:**

    - Visit `http://127.0.0.1:8000/` to access the application's registeration page.

## Features

- User-friendly website with secure login.
- Effortless file uploads.
- View uploaded files.
- Search functionality for user profiles and file .
- File-downloading capabilities.


