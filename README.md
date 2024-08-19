---

# POLIBOX

POLIBOX is a comprehensive platform designed to assist students of Universities of Technology. This project, built using Django, provides various resources and tools to facilitate the academic journey of students. The backend is almost ready, needing more security and some small improvements. The frontend should be redesigned, but I am not really into it.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Materials**: Find all educational aids and materials in one place.
- **Email Generator**: Check how to start an email to a specific lecturer and copy the template.
- **Calendar**: Stay updated with important dates such as colloquia, exams, and ceremonies.
- **Progress Tracker**: Monitor your academic progress.
- **Information**: Access contact information and the portal's regulations.

Check Wiki section to see what does it look like!

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/m-sadkowski/Polibox.git
    cd Polibox
    cd myproject
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

4. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`.

- **Materials**: Navigate to the `Materials` section to find study aids.
- **Email Generator**: Use the `Generator` to create email templates.
- **Calendar**: Check the `Calendar` for important academic dates.
- **Progress Tracker**: View your progress in the `Progress` section.
- **Information**: Visit the `Information` page for contact details and regulations.
- **Admin**: Login as administrator via http://127.0.0.1:8000/admin/ to add events to calendar or manage materials.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

Please ensure your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the BSD-2 License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any queries, suggestions, or feedback, please contact:

- **Michał Sadkowski**: [msadkowski000@gmail.com](mailto:msadkowski000@gmail.com)
- **GitHub**: [github.com/m-sadkowski](https://github.com/m-sadkowski)

---

Thank you for using POLIBOX! We hope it makes your academic journey easier and more efficient.

---
