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

> TO BE CONTINUE!
>
