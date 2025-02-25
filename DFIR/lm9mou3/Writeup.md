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

here I found a place similar to the one in the picture (the buildings,mc donalds..)

![image](https://github.com/user-attachments/assets/60b02964-1cd6-4a04-88c2-d7973d6dab64)

this place is **Guéliz** which is in **Marrakech**

so let's search for **mc donalds** nearby **Guéliz** 

from this picture we can recognize **Maroc telecom** and **Mc donald's**

![WhatsApp Image 2025-02-20 à 00 33 08_1d0d8ea0](https://github.com/user-attachments/assets/47a34365-0327-4bd5-ae1b-747f30bb5f3b)

which are shown here in the map 

![WhatsApp Image 2025-02-20 à 00 10 56_853195f2](https://github.com/user-attachments/assets/f8ef0b12-a678-49b4-a268-e215e4eaf62f)

And we can also recognize here the brown **"Zelij"** and we can identify the exact place from where the photo was taken 

![image](https://github.com/user-attachments/assets/49d9c416-51c4-4b16-8955-1f04420ebfd7)

**Now it's time to identify the mosque**

by searching about the nearby mosques we found these result 

![image](https://github.com/user-attachments/assets/a5337385-c0de-46c0-aa66-795babc0fa18)

and since in the challenge description the mosque is carrying the name of an old moroccan king so it's exactly 
**Hassan II mosque** 

![image](https://github.com/user-attachments/assets/2d33a54d-e963-4d96-913a-d79e81dedc6f)

#### And it's exact address is : 
**JXMR+QR9, Rue el Imam Malik, Marrakech 40000**
----
And finally here we is the flag 
---
***NHD{JXMR+QR9, Rue el Imam Malik, Marrakech 40000}***
---
