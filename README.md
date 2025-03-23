# SendMail

## Project Description
SendMail is a Python package for sending emails using SMTP. This project allows you to send emails using your Gmail account.

## Installation
You can install this package in two ways:

1. **Using Git Clone:**
   First, clone the repository or download the files, then use the following command to install:

   ```sh
   pip install .
   ```

2. **Directly from GitHub:**
   You can install the package directly from GitHub using pip:

   ```sh
   pip install git+https://github.com/heydari-dev/SendEmail.git
   ```

## Usage
After installation, you can use the `send_email` function to send an email. The following example demonstrates how to send an email:

```python
from sendemail import send_email

subject = "Hello"
body = "This is a test email."
your_email = "your_email@gmail.com"
your_password = "your_password"
email_receiver = "receiver@example.com"

send_email(subject, body, your_email, your_password, email_receiver)
```

## Requirements
- A Gmail account
- Enabling Less Secure Apps access in Gmail
- Python 3+

## License
This project is licensed under the MIT License.

