#include <Servo.h>
Servo myservo;


void setup() {
Serial.begin(9600);
pinMode(13,OUTPUT);
myservo.attach(9);
}

int c;
void loop() {
  
  if(Serial.available()>0){
    c = Serial.read();
    myservo.write(c);
  }
  
}  
