# Walkthrough :

### **Step 1: Checking the Audio File for Hidden Data**

You’re given an audio file called **`blaugrana.wav`**, but there’s something unusual about it. Instead of just listening, let’s start by checking if there’s any hidden information inside the file’s metadata.

Run this command:

```bash
exiftool blaugrana.wav
```

This will display all the metadata stored in the file.

![image](https://github.com/user-attachments/assets/6e590025-83e7-42aa-a4bc-b54e2f9af75c)


📌 **What you’re looking for:**

- A **comment** field that contains a link to a Telegram bot `t.me/N2T_bot`

Once you find the link, open Telegram and start a conversation with the bot.

---

### **Step 2: Exploring the Telegram Bot**

The bot will respond with a welcome message. Now, type:

```
/help
```

This will show you a list of available commands.

![image](https://github.com/user-attachments/assets/64242fa7-53da-4266-a494-550dea003b12)


One of the most important commands is:

```
/get_flag
```

However, when you try using it, you’ll see that it doesn’t work right away. The bot has security restrictions in place.

To get a clue, type:

```
/hint
```

![image](https://github.com/user-attachments/assets/0eeb0180-5d97-4201-8ffa-7f15fb9c47a7)

📌 **What the hint tells you:**

- It mentions **modular arithmetic** and asks you to sum the ASCII values of letters in a word.
- It also refers to a very well-known number in Morocco (**spoiler: it’s 212, the country code**).

At this point, you still don’t have everything you need. Let’s go back to the original `blaugrana.wav` file and dig deeper.

### **Step 3: Extracting a Hidden Audio File**

The `blaugrana.wav` file actually contains another **hidden** audio file inside it. You need a tool to find the embedded files within the original audio( steghide,binwalk..)

After crack just the password of zip file it’s very easy to crack there’s various tools to do tha

💡 **Hint:** Try common words. The password is **"password"** (yes, it’s that simple).

Now you have a new file: **`hidden_audio.wav`**.

---

### **Step 4: Decoding the Morse Code**

If you listen to `hidden_audio.wav`, you’ll hear a series of beeps and pauses. This is **Morse code**.

Instead of decoding it manually, you can use an **online Morse code decoder**:

- Upload the file to https://morsecode.world/international/decoder/audio-decoder.html
- The output will be:
    
    ```
    VISCABARC
    ```
    

📌 **Important:** Remember this word—**"VISCABARCA"**—you will need it soon.

---

### **Step 5: Solving the Modular Arithmetic Puzzle**

The hint from the bot talked about summing the **ASCII values** of a word and using **modular arithmetic** with **212**.

Let’s calculate it:

Open Python and run this:

```python
sum(ord(c) for c in "VISCABARCA") % 212
```

This will give you a **specific number** (let’s call it `X`).

---

### **Step 6: Bypassing the Bot’s Security**

Now that you have the number `X`, go back to the bot and type:

```
/get_flag X
```

If you calculated it correctly, the bot will respond:

```
✅ Payload = bypass_success
```

![image](https://github.com/user-attachments/assets/e99be094-3c0d-4de1-9950-8e7740ed4146)

NOW you have the payload but as you already notice there’s some restrictions on the logic used by the bot to handle inputs of /get-flag so I will give u the opportunity to guess how to do it ( it’s very easy now you should just type the payload in other format) 

I’m just kidding there’s the final step :

![image](https://github.com/user-attachments/assets/1ee480b9-e53a-4af0-8665-ee3f5baa07d7)

That’s all see you next time…. For those who ask what is this payload ask Mr GPT IM VERY LAZY TO DO IT!!
