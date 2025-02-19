char * flag = "REDACTED";
String curr, first, second;
int a1 = 2, a2 = 3, a3 = 4, a4 = 5;  
int y1 = 6, y2 = 7, y3 = 8, y4 = 9;  
int i;

String get_out(String bits) {
    String output;
    digitalWrite(out1, ((bits[0] == '1') ? HIGH : LOW));
    digitalWrite(out2, ((bits[1] == '1') ? HIGH : LOW));
    digitalWrite(out3, ((bits[2] == '1') ? HIGH : LOW));
    digitalWrite(out4, ((bits[3] == '1') ? HIGH : LOW));
    delay(500);  
    output += String(digitalRead(a1));
    output += String(digitalRead(a2));
    output += String(digitalRead(a3));
    output += String(digitalRead(a4));
    return output;
}

String transform(int n) {
  String r;
  while (n != 0) {
    r = (n % 2 == 0 ? "0" : "1") + r;
    n /= 2;
  }
  while ((int)r.length() < 8) {
    r = "0" + r;
  }
  return r;
}

void setup() {  
  i = 0;
  pinMode(y1, OUTPUT);
  pinMode(y2, OUTPUT);
  pinMode(y3, OUTPUT);
  pinMode(y4, OUTPUT);
  pinMode(a1, INPUT);
  pinMode(a2, INPUT);
  pinMode(a3, INPUT);
  pinMode(a4, INPUT);
  Serial.begin(8000);
}

void loop() {
  if (i < strlen(flag)) {
    curr = transform(flag[i]);  
    first = curr.substring(0, 4); 
    second = curr.substring(4, 8);  
    Serial.print(get_out(first));
    Serial.println(get_out(second));
    delay(3000);
    i++;
  }
}
