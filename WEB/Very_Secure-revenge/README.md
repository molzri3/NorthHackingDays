## Very_Secure-revenge

### Flag:
`NHD{be_cautious_when_using_weak_jwt_secrets}`

### Description

Very_Secure was mid. I bet you can solve this one :)

### Solution

1. Inspect the cookies to find the user and its JWT.
2. Crack the JWT using the `rockyou` wordlist to obtain the password: `angeline`.
3. Create your cookies as an admin and get the flag in the home page.
