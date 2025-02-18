# Fireside Secrets - Write-Up
## **Overview**
---

The challenge involves multiple layers of skills and techniques:

1-Decrypting Firefox passwords stored in a user profile.

2-Finding a hidden directory containing a password-protected flag.zip file.

3-Extracting the flag using the decrypted password.

---

## **Exploring the VHDX File**
first we need to unzip the **Profiles.zip** which contains the vhdx file.
but you can see that a password is required 

![image](https://github.com/user-attachments/assets/22dc09b4-b736-4ec4-9e7a-bbac0056a256)

To proceed, we need to crack the ZIP file password using **fcrackzip** or **john**.
```bash

fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt profiles.zip
found file 'firefox_profiles.vhdx', (size cp/uc 60867448/239075328, flags 9, chk 4c42)


PASSWORD FOUND!!!!: pw == operationcwal


```

### Now let's unzip the file using the password found 

```bash

unzip profiles.zip
Archive:  profiles.zip
[profiles.zip] firefox_profiles.vhdx password: 
  inflating: firefox_profiles.vhdx  


```
### Now we need to mount the disk to our machine and explore its content

```bash
sudo modprobe nbd
sudo qemu-nbd --connect=/dev/nbd0 firefox_profiles.vhdx
sudo mount /dev/nbd0p1 /mnt/vhdx

cd /mnt/vhdx
ls -la 
total 52
drwxrwxrwx 1 root root 49152 Feb 12 08:40  .
drwxr-xr-x 8 root root  4096 Feb  9 13:41  ..
drwxrwxrwx 1 root root     0 Jul 14  2024 '$RECYCLE.BIN'
drwxrwxrwx 1 root root     0 Jul 14  2024  Aaron.Jones
drwxrwxrwx 1 root root     0 Jul 14  2024  Abigail.Wallace
drwxrwxrwx 1 root root     0 Jul 14  2024  Aimee.Elliott
drwxrwxrwx 1 root root     0 Jul 14  2024  Aimee.Knight
drwxrwxrwx 1 root root     0 Jul 14  2024  Alan.Fox
drwxrwxrwx 1 root root     0 Jul 14  2024  Amy.Woods
drwxrwxrwx 1 root root     0 Jul 14  2024  Andrea.Davies
drwxrwxrwx 1 root root     0 Jul 14  2024  Anne.Mitchell
drwxrwxrwx 1 root root     0 Jul 14  2024  Annette.King
drwxrwxrwx 1 root root     0 Jul 14  2024  Anthony.Heath
drwxrwxrwx 1 root root     0 Jul 14  2024  Anthony.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Anthony.Thompson
drwxrwxrwx 1 root root     0 Jul 14  2024  Arthur.Kirk
drwxrwxrwx 1 root root     0 Jul 14  2024 "Ashley.O'Neill"
drwxrwxrwx 1 root root     0 Jul 14  2024  Barry.Cox
drwxrwxrwx 1 root root     0 Jul 14  2024  Barry.Foster
drwxrwxrwx 1 root root     0 Jul 14  2024  Ben.Brown
drwxrwxrwx 1 root root     0 Jul 14  2024  Benjamin.Walker
drwxrwxrwx 1 root root     0 Jul 14  2024  Bernard.Davey
drwxrwxrwx 1 root root     0 Jul 14  2024  Bernard.Turner
drwxrwxrwx 1 root root     0 Jul 14  2024  Bernard.Walters
drwxrwxrwx 1 root root     0 Jul 14  2024  Beverley.Connolly
drwxrwxrwx 1 root root     0 Jul 14  2024  Brett.Roberts
drwxrwxrwx 1 root root     0 Jul 14  2024  Bruce.Hewitt
drwxrwxrwx 1 root root     0 Jul 14  2024  Callum.Brookes
drwxrwxrwx 1 root root     0 Jul 14  2024  Cameron.White
drwxrwxrwx 1 root root     0 Jul 14  2024  Caroline.Barker
drwxrwxrwx 1 root root     0 Jul 14  2024  Caroline.Hunter
drwxrwxrwx 1 root root     0 Jul 14  2024  Caroline.Thornton
drwxrwxrwx 1 root root     0 Jul 14  2024  Caroline.Wilson
drwxrwxrwx 1 root root     0 Jul 14  2024  Carolyn.Hughes
drwxrwxrwx 1 root root     0 Jul 14  2024  Carolyn.Hunt
drwxrwxrwx 1 root root     0 Jul 14  2024  Charles.Sullivan
drwxrwxrwx 1 root root     0 Jul 14  2024  Cheryl.Evans
drwxrwxrwx 1 root root     0 Jul 14  2024  Cheryl.Roberts
drwxrwxrwx 1 root root     0 Jul 14  2024  Chloe.Scott
drwxrwxrwx 1 root root     0 Jul 14  2024  Christopher.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Claire.Lewis
drwxrwxrwx 1 root root     0 Jul 14  2024  Clare.Preston
drwxrwxrwx 1 root root     0 Jul 14  2024  Colin.Faulkner
drwxrwxrwx 1 root root     0 Jul 14  2024  Connor.Cook
drwxrwxrwx 1 root root     0 Jul 14  2024  Damien.Hartley
drwxrwxrwx 1 root root     0 Jul 14  2024  Daniel.Clark
drwxrwxrwx 1 root root     0 Jul 14  2024  Daniel.Gibson
drwxrwxrwx 1 root root     0 Jul 14  2024  Danny.Roberts
drwxrwxrwx 1 root root     0 Jul 14  2024  Dawn.Clarke
drwxrwxrwx 1 root root     0 Jul 14  2024  Denis.Davies
drwxrwxrwx 1 root root     0 Jul 14  2024  Denise.Begum
drwxrwxrwx 1 root root     0 Jul 14  2024  Denis.Wood
drwxrwxrwx 1 root root     0 Jul 14  2024  Derek.Giles
drwxrwxrwx 1 root root     0 Jul 14  2024  Diana.James
drwxrwxrwx 1 root root     0 Jul 14  2024  Diane.Carroll
drwxrwxrwx 1 root root     0 Jul 14  2024  Dominic.Heath
drwxrwxrwx 1 root root     0 Jul 14  2024  Dorothy.Walsh
drwxrwxrwx 1 root root     0 Jul 14  2024  Eileen.Andrews
drwxrwxrwx 1 root root     0 Jul 14  2024  Elliott.Carr
drwxrwxrwx 1 root root     0 Jul 14  2024  Elliott.Kay
drwxrwxrwx 1 root root     0 Jul 14  2024  Elliott.Nicholls
drwxrwxrwx 1 root root     0 Jul 14  2024  Emma.Clark
drwxrwxrwx 1 root root     0 Jul 14  2024  Fiona.Marshall
drwxrwxrwx 1 root root     0 Jul 14  2024  Francesca.Ahmed
drwxrwxrwx 1 root root     0 Jul 14  2024  Frances.Freeman
drwxrwxrwx 1 root root     0 Jul 14  2024  Frederick.Jackson
drwxrwxrwx 1 root root     0 Jul 14  2024  Gail.Cox
drwxrwxrwx 1 root root     0 Jul 14  2024  Gail.Joyce
drwxrwxrwx 1 root root     0 Jul 14  2024  Gareth.Hussain
drwxrwxrwx 1 root root     0 Jul 14  2024  Gareth.Newton
drwxrwxrwx 1 root root     0 Jul 14  2024  Gavin.Dixon
drwxrwxrwx 1 root root     0 Jul 14  2024  Georgina.Burns
drwxrwxrwx 1 root root     0 Jul 14  2024  Gerald.Foster
drwxrwxrwx 1 root root     0 Jul 14  2024  Gerald.Murphy
drwxrwxrwx 1 root root     0 Jul 14  2024  Gerard.Thomas
drwxrwxrwx 1 root root     0 Jul 14  2024  Gillian.Roberts
drwxrwxrwx 1 root root     0 Jul 14  2024  Glen.Marshall
drwxrwxrwx 1 root root     0 Jul 14  2024  Glenn.Rogers
drwxrwxrwx 1 root root     0 Jul 14  2024  Grace.Dunn
drwxrwxrwx 1 root root     0 Jul 14  2024  Heather.Little
drwxrwxrwx 1 root root     0 Jul 14  2024  Henry.Adams
drwxrwxrwx 1 root root     0 Jul 14  2024  Henry.Jordan
drwxrwxrwx 1 root root     0 Feb 12 09:23  .hidden
drwxrwxrwx 1 root root     0 Jul 14  2024  Hollie.Harrison
drwxrwxrwx 1 root root     0 Jul 14  2024  Hollie.Hunt
drwxrwxrwx 1 root root     0 Jul 14  2024  Hollie.White
drwxrwxrwx 1 root root     0 Jul 14  2024  Iain.Graham
drwxrwxrwx 1 root root     0 Jul 14  2024  Ian.Connor
drwxrwxrwx 1 root root     0 Feb 12 07:18  Jack.Sparrow
drwxrwxrwx 1 root root     0 Jul 14  2024 "Jacob.O'Donnell"
drwxrwxrwx 1 root root     0 Jul 14  2024  Jacqueline.Morley
drwxrwxrwx 1 root root     0 Jul 14  2024  Jade.Perry
drwxrwxrwx 1 root root     0 Jul 14  2024  Jade.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Jake.Kaur
drwxrwxrwx 1 root root     0 Jul 14  2024  James.Cook
drwxrwxrwx 1 root root     0 Jul 14  2024  James.Marshall
drwxrwxrwx 1 root root     0 Jul 14  2024  Jamie.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Jane.Taylor
drwxrwxrwx 1 root root     0 Jul 14  2024  Janice.Stokes
drwxrwxrwx 1 root root     0 Jul 14  2024  Jasmine.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Jasmine.Yates
drwxrwxrwx 1 root root     0 Jul 14  2024  Jemma.Bartlett
drwxrwxrwx 1 root root     0 Jul 14  2024  Jemma.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Jeremy.Austin
drwxrwxrwx 1 root root     0 Jul 14  2024  Joe.Brooks
drwxrwxrwx 1 root root     0 Jul 14  2024  Joe.Nicholls
drwxrwxrwx 1 root root     0 Jul 14  2024  Jonathan.Richardson
drwxrwxrwx 1 root root     0 Jul 14  2024  Jordan.Moore
drwxrwxrwx 1 root root     0 Jul 14  2024  Joseph.Carroll
drwxrwxrwx 1 root root     0 Jul 14  2024  Josephine.Evans
drwxrwxrwx 1 root root     0 Jul 14  2024  Josephine.Walker
drwxrwxrwx 1 root root     0 Jul 14  2024  Josh.Wilson
drwxrwxrwx 1 root root     0 Jul 14  2024  Joyce.Johnson
drwxrwxrwx 1 root root     0 Jul 14  2024  Judith.Harris
drwxrwxrwx 1 root root     0 Jul 14  2024  Judith.Hawkins
drwxrwxrwx 1 root root     0 Jul 14  2024  Julie.Rees
drwxrwxrwx 1 root root     0 Jul 14  2024  June.Murphy
drwxrwxrwx 1 root root     0 Jul 14  2024  Karen.Moore
drwxrwxrwx 1 root root     0 Jul 14  2024  Karl.Thomas
drwxrwxrwx 1 root root     0 Jul 14  2024  Katherine.Osborne
drwxrwxrwx 1 root root     0 Jul 14  2024  Katherine.Williams
drwxrwxrwx 1 root root     0 Jul 14  2024  Kathleen.Taylor
drwxrwxrwx 1 root root     0 Jul 14  2024  Kathleen.Walker
drwxrwxrwx 1 root root     0 Jul 14  2024  Katy.Jones
drwxrwxrwx 1 root root     0 Jul 14  2024  Keith.Howell
drwxrwxrwx 1 root root     0 Jul 14  2024  Keith.Jackson
drwxrwxrwx 1 root root     0 Jul 14  2024  Keith.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Kieran.Parker
drwxrwxrwx 1 root root     0 Jul 14  2024  Kim.Lee
drwxrwxrwx 1 root root     0 Jul 14  2024  Kim.Thomas
drwxrwxrwx 1 root root     0 Jul 14  2024  Kyle.Parker
drwxrwxrwx 1 root root     0 Jul 14  2024  Laura.Robinson
drwxrwxrwx 1 root root     0 Jul 14  2024  Laura.Yates
drwxrwxrwx 1 root root     0 Jul 14  2024  Lauren.Young
drwxrwxrwx 1 root root     0 Jul 14  2024  Lawrence.Stewart
drwxrwxrwx 1 root root     0 Jul 14  2024  Leanne.McCarthy
drwxrwxrwx 1 root root     0 Jul 14  2024  Leigh.Watson
drwxrwxrwx 1 root root     0 Jul 14  2024  Leslie.Ingram
drwxrwxrwx 1 root root     0 Jul 14  2024  Leslie.Willis
drwxrwxrwx 1 root root     0 Jul 14  2024  Liam.Peters
drwxrwxrwx 1 root root     0 Jul 14  2024  Linda.Lee
drwxrwxrwx 1 root root     0 Jul 14  2024  Lucy.Morgan
drwxrwxrwx 1 root root     0 Jul 14  2024  Lucy.Richardson
drwxrwxrwx 1 root root     0 Jul 14  2024  Lynne.Gibson
drwxrwxrwx 1 root root     0 Jul 14  2024  Lynne.Hayward
drwxrwxrwx 1 root root     0 Jul 14  2024  Malcolm.Palmer
drwxrwxrwx 1 root root     0 Jul 14  2024  Marc.Mitchell
drwxrwxrwx 1 root root     0 Jul 14  2024  Marcus.Taylor
drwxrwxrwx 1 root root     0 Jul 14  2024  Margaret.Patel
drwxrwxrwx 1 root root     0 Jul 14  2024  Marian.Baldwin
drwxrwxrwx 1 root root     0 Jul 14  2024  Marian.Bell
drwxrwxrwx 1 root root     0 Jul 14  2024  Marian.Campbell
drwxrwxrwx 1 root root     0 Jul 14  2024  Maria.Parkinson
drwxrwxrwx 1 root root     0 Jul 14  2024  Marilyn.Sanderson
drwxrwxrwx 1 root root     0 Jul 14  2024  Marion.Evans
drwxrwxrwx 1 root root     0 Jul 14  2024  Martin.Dawson
drwxrwxrwx 1 root root     0 Jul 14  2024  Martin.James
drwxrwxrwx 1 root root     0 Jul 14  2024  Martin.Kirk
drwxrwxrwx 1 root root     0 Jul 14  2024  Martin.Marsden
drwxrwxrwx 1 root root     0 Jul 14  2024  Martin.Simpson
drwxrwxrwx 1 root root     0 Jul 14  2024  Mary.Andrews
drwxrwxrwx 1 root root     0 Jul 14  2024  Mary.Hunter
drwxrwxrwx 1 root root     0 Jul 14  2024  Mary.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Matthew.Craig
drwxrwxrwx 1 root root     0 Jul 14  2024  Maurice.Davies
drwxrwxrwx 1 root root     0 Jul 14  2024  Megan.Howard
drwxrwxrwx 1 root root     0 Jul 14  2024  Michelle.Butler
drwxrwxrwx 1 root root     0 Jul 14  2024  Michelle.Jordan
drwxrwxrwx 1 root root     0 Jul 14  2024  Michelle.Young
drwxrwxrwx 1 root root     0 Jul 14  2024  Mohamed.Wright
drwxrwxrwx 1 root root     0 Jul 14  2024  Mohammed.Ward
drwxrwxrwx 1 root root     0 Jul 14  2024  Molly.Wilson
drwxrwxrwx 1 root root     0 Jul 14  2024  Naomi.Harris
drwxrwxrwx 1 root root     0 Jul 14  2024  Natalie.Norris
drwxrwxrwx 1 root root     0 Jul 14  2024  Nicola.Winter
drwxrwxrwx 1 root root     0 Jul 14  2024  Nicole.Harrison
drwxrwxrwx 1 root root     0 Jul 14  2024  Nicole.Lloyd
drwxrwxrwx 1 root root     0 Jul 14  2024  Nigel.Sutton
drwxrwxrwx 1 root root     0 Jul 14  2024  Owen.Black
drwxrwxrwx 1 root root     0 Jul 14  2024  Patricia.Johnson
drwxrwxrwx 1 root root     0 Jul 14  2024  Patrick.Ford
drwxrwxrwx 1 root root     0 Jul 14  2024  Peter.Nash
drwxrwxrwx 1 root root     0 Jul 14  2024  Philip.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Rafik.Boubker
drwxrwxrwx 1 root root     0 Jul 14  2024  Richard.Hutchinson
drwxrwxrwx 1 root root     0 Jul 14  2024  Richard.Lewis
drwxrwxrwx 1 root root     0 Jul 14  2024  Richard.Riley
drwxrwxrwx 1 root root     0 Jul 14  2024  Robert.Lewis
drwxrwxrwx 1 root root     0 Jul 14  2024  Robin.Hargreaves
drwxrwxrwx 1 root root     0 Jul 14  2024  Robin.Scott
drwxrwxrwx 1 root root     0 Jul 14  2024  Robin.Smith
drwxrwxrwx 1 root root     0 Jul 14  2024  Ross.Scott
drwxrwxrwx 1 root root     0 Jul 14  2024  Russell.Hurst
drwxrwxrwx 1 root root     0 Jul 14  2024  Russell.Miller
drwxrwxrwx 1 root root     0 Jul 14  2024  Russell.Mistry
drwxrwxrwx 1 root root     0 Jul 14  2024  Sally.Clayton
drwxrwxrwx 1 root root     0 Jul 14  2024  Sarah.Bradley
drwxrwxrwx 1 root root     0 Jul 14  2024  Sheila.Sharp
drwxrwxrwx 1 root root     0 Jul 14  2024  Sian.Kemp
drwxrwxrwx 1 root root     0 Jul 14  2024  Simon.Morris
drwxrwxrwx 1 root root     0 Jul 14  2024  Sophie.Powell
drwxrwxrwx 1 root root     0 Jul 14  2024  Sophie.Webster
drwxrwxrwx 1 root root     0 Jul 14  2024  Stacey.Barrett
drwxrwxrwx 1 root root     0 Jul 14  2024  Stacey.Pratt
drwxrwxrwx 1 root root     0 Jul 14  2024  Steven.Bowen
drwxrwxrwx 1 root root     0 Jul 14  2024  Stewart.Armstrong
drwxrwxrwx 1 root root     0 Jul 14  2024 'System Volume Information'
drwxrwxrwx 1 root root     0 Jul 14  2024  Tina.Dawson
drwxrwxrwx 1 root root     0 Jul 14  2024  Toby.Knight
drwxrwxrwx 1 root root     0 Jul 14  2024  Tony.Graham
drwxrwxrwx 1 root root     0 Jul 14  2024  Victor.Jenkins
drwxrwxrwx 1 root root     0 Jul 14  2024  Vincent.Roberts
drwxrwxrwx 1 root root     0 Jul 14  2024  Wendy.French
drwxrwxrwx 1 root root     0 Jul 14  2024  William.McLean
drwxrwxrwx 1 root root     0 Jul 14  2024  Yvonne.Morris
drwxrwxrwx 1 root root     0 Jul 14  2024  Zoe.Adams



```
here you can notice a hidden directory named **.hidden**

![image](https://github.com/user-attachments/assets/46f4f5c9-1330-4e19-ba0f-2c68eed41440)

As you see here this directory contains the flag.zip but it's protected with the password of the user that we should find its credentials

## **Decrypting user profile credentials**

Now if you check the directories you'll notice that all of them are empty except **Rafik.Boubker** directory

![image](https://github.com/user-attachments/assets/eb865df6-2e04-4de4-b2fd-099c0a2f914c)

#### Now we should decrypt Mozilla protected passwords 
by searching a little you can find this amazing tool https://github.com/lclevy/firepwd.git
**clone the repo**
then run the script
```bash
python firepwd.py -d /mnt/vhdx/Rafik.Boubker/profiles 

globalSalt: b'd7c4533f35d54acefc1c4f1845403d6112ad281b'
 SEQUENCE {
   SEQUENCE {
     OBJECTIDENTIFIER 1.2.840.113549.1.5.13 pkcs5 pbes2
     SEQUENCE {
       SEQUENCE {
         OBJECTIDENTIFIER 1.2.840.113549.1.5.12 pkcs5 PBKDF2
         SEQUENCE {
           OCTETSTRING b'21bde4508688d2fddd9af5f46f4417174fd3c680afff1f33109d4afed6efa316'
           INTEGER b'01'
           INTEGER b'20'
           SEQUENCE {
             OBJECTIDENTIFIER 1.2.840.113549.2.9 hmacWithSHA256
           }
         }
       }
       SEQUENCE {
         OBJECTIDENTIFIER 2.16.840.1.101.3.4.1.42 aes256-CBC
         OCTETSTRING b'4af4135413a3dcbfbe8be5a261bc'
       }
     }
   }
   OCTETSTRING b'b81bb26a18afa9c907e0fbbbe168b701'
 }
clearText b'70617373776f72642d636865636b0202'
password check? True
 SEQUENCE {
   SEQUENCE {
     OBJECTIDENTIFIER 1.2.840.113549.1.5.13 pkcs5 pbes2
     SEQUENCE {
       SEQUENCE {
         OBJECTIDENTIFIER 1.2.840.113549.1.5.12 pkcs5 PBKDF2
         SEQUENCE {
           OCTETSTRING b'862db7261298b6ae35a5b75c6e037022037a853fb1309aaa0c007d13c90b8435'
           INTEGER b'01'
           INTEGER b'20'
           SEQUENCE {
             OBJECTIDENTIFIER 1.2.840.113549.2.9 hmacWithSHA256
           }
         }
       }
       SEQUENCE {
         OBJECTIDENTIFIER 2.16.840.1.101.3.4.1.42 aes256-CBC
         OCTETSTRING b'f4b20c4e677efa934aaf67957499'
       }
     }
   }
   OCTETSTRING b'1993fca7a9e176ca887917105d21af967f65018715856ac24730af0e45b76a78'
 }
clearText b'a1190d07ce38916ee51a6123615b2502493819d0fd8fd6510808080808080808'
decrypting login/password pairs
 http://git.ifrit.vl:b'jack.smith@ifrit.vl',b'JigokuNoKaen10'

```
And as you see we successfully decrypted the login/password pairs 
***http://git.ifrit.vl:b'jack.smith@ifrit.vl',b'JigokuNoKaen10'***
so this password : **JigokuNoKaen10** will be used to unzip the **flag.zip** file

```bash
┌──(root㉿kali)-[/mnt/vhdx/.hidden]
└─# unzip flag.zip        
Archive:  flag.zip
[flag.zip] flag.txt password: 
 extracting: flag.txt                
                                                                                                       
┌──(root㉿kali)-[/mnt/vhdx/.hidden]
└─# cat flag.txt   
NHD{R2fiK_B0uBk3r_PasSw0rd_L3aK3d}

```
----
And here we goo here is the flag : **NHD{R2fiK_B0uBk3r_PasSw0rd_L3aK3d}**
----
