## BEHAVE
this challenge is not hard at all

the player should analyse the behavior of thir server ant its output facing the user input

1. the output is the HEX that means that is should fersty convert the putput from HEX to bytes 

2. each time the output changes even for the same input , the player then should expect a count variable that increments each time.

3. the hint says XOR then the player should use it should play with 

4. the server accepts all alphanumerical values wich indicates that the server processes the input as ascii code.

## solution

the player should xor its input phrase with the expected count variable that (their ascii values) then xor the result with the the output phrase (after recovering it from HEX).

## the flag :
NHD{behavioral_analysis_:_good_job}


