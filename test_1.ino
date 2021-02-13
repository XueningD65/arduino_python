int switchstate = 0;
int val = 0;
String data;

void setup() {
  // put your setup code here, to run once:
  pinMode(6, INPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  switchstate = digitalRead(6);

  while (Serial.available())
  {
      data = Serial.readString();
      val= data.toInt();
   }
   
  Serial.println("Hello world from Arduino!"); // write a string
  // put your main code here, to run repeatedly:
  Serial.println(val);

  if(switchstate == LOW && val == LOW)
  {
    digitalWrite(4, LOW);
    digitalWrite(2, LOW);
    delay(500);
    digitalWrite(2, HIGH);
    delay(500);
  }
  else if(switchstate == LOW)
  {
    digitalWrite(2, LOW);
    digitalWrite(4, HIGH);
    delay(500);
    digitalWrite(2, HIGH);
    digitalWrite(4, LOW);
    delay(500);
  }
  else
  {
    digitalWrite(2, LOW);
    digitalWrite(4, LOW);
    delay(500);
    digitalWrite(4, HIGH);
    delay(500);
  }
}
