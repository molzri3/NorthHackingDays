# lme9mou3 - Write-Up
## **Overview📄**

---

In this challenge, we receive a mysterious file that refuses to reveal its contents. The file is linked to a well-known Moroccan artist often mocked on social media. Our goal is to recover the file and identify the artist and the name of the song, leading us to a specific geolocation based on an Instagram post from January 20.

---

## **Recovering the file🧐**

The given file is named corrupted.gif. However, upon inspecting its contents, it does not resemble a valid GIF file.

even if we try to use **exiftool** or **file** it doesn't give us a useful information about the file type 

![image](https://github.com/user-attachments/assets/c2745aba-b979-4e31-a84a-b7710cd95875)

**So let's analyze the file header using a hex editor**
```bash
hexeditor Corrupted.gif 
```

![image](https://github.com/user-attachments/assets/b07e7b79-c3ac-4d44-ba7f-49a60bc00c92)

by checking this website **https://en.wikipedia.org/wiki/List_of_file_signatures** that provides a list of file signatures
we can see that our file header looks like a wav file header but it's a little bit modified

![image](https://github.com/user-attachments/assets/caf2994a-bd09-4dda-92e6-5bff52e0f4a7)

let's try to correct the hex values and save the file in a solution.wav

![image](https://github.com/user-attachments/assets/077e3b3a-b326-49f1-b4bb-07b012ad66b2)

---

## **OSINT Investigation (Finding the Instagram Post)🕵️**

I think it's easy to recognize the song but in case you didn't recognize it you can use this website 
**https://aha-music.com/**

![image](https://github.com/user-attachments/assets/9e21af13-ff0b-4b9b-861d-3e8ea35a9930)

So as you see here this song belongs to **Sy Mehdi😂**

you can easily find his instagram page 

![image](https://github.com/user-attachments/assets/aaf94fae-1f1c-4ebf-b8a8-e9ab95fb9eb7)

**by scroling down we can find this post that was posted in 20 january**

![image](https://github.com/user-attachments/assets/6650947a-f61f-4a9e-ba90-399715bee519)

**let's take a screenshoot and do a reverse image search with google image**

![image](https://github.com/user-attachments/assets/7ef72f0e-cbe7-4758-86b6-64b5d85c3d46)

here I found a place similar to the one in the picture 

![image](https://github.com/user-attachments/assets/60b02964-1cd6-4a04-88c2-d7973d6dab64)

