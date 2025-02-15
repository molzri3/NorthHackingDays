Here’s the corrected and improved version of your writeup in a clean and professional format:

---

# Bayanat

## **Description**
Time for a warmup and chill! no source code :)
---

## **Flag**
`NDH{nadi_nta?_nchofk_f_l7o9na}`

---

## **Solution**

This is an easy SQL injection challenge. Here's how to solve it step by step:

1. **Identify the Vulnerability**:
   - The application has an input field that is vulnerable to SQL injection.
   - You can test this by entering a single quote (`'`) and observing if the application throws an error or behaves unexpectedly.

2. **Manual Exploitation**:
   - Instead of using automated tools like `sqlmap`, you can exploit the vulnerability manually.
   - The application is vulnerable to **Union-Based SQL Injection**.

3. **Enumerate the Database**:
   - Use a payload to enumerate the database schema. For example:
     ```
     ' UNION SELECT schema_name FROM INFORMATION_SCHEMA.SCHEMATA-- -
     ```
   - This will reveal the database names.

4. **Find the Flag Table**:
   - Once you know the database name, enumerate the tables:
     ```
     ' UNION SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='database_name'-- -
     ```
   - Look for a table named `flag`.

5. **Retrieve the Flag**:
   - The `flag` table contains a column named `flag`. Use the following payload to retrieve the flag:
     ```
     ' UNION SELECT flag FROM flag-- -
     ```

6. **Final Payload**:
   - Submit the payload in the input field:
     ```
     ' UNION SELECT flag FROM flag-- -
     ```
   - The application will return the flag.

---

## **Payload**
The final payload to retrieve the flag is:
```
'union select flag from flag -- -
```
