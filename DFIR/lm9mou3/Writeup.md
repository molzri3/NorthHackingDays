# lme9mou3 - Write-Up
## **Overview📄**

---

In this challenge, we receive a mysterious file that refuses to reveal its contents. The file is linked to a well-known Moroccan artist often mocked on social media. Our goal is to recover the file and identify the artist and the name of the song, leading us to a specific geolocation based on an Instagram post from January 20.

---

## **recovering the file**

The given file is named corrupted.gif. However, upon inspecting its contents, it does not resemble a valid GIF file.

even if we try to use **exiftool** or **file** it doesn't give us a useful information about the file type 

![image](https://github.com/user-attachments/assets/c2745aba-b979-4e31-a84a-b7710cd95875)

**So let's analyze the file header using a hex editor**
```bash
hexeditor Corrupted.gif 
```

![image](https://github.com/user-attachments/assets/b07e7b79-c3ac-4d44-ba7f-49a60bc00c92)

