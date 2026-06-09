#include <Servo.h>

Servo putar;

const int ms = A5;     
const int buzzer = 6;

int mouster;            

void setup()
{
  pinMode(ms, INPUT);
  pinMode(buzzer, OUTPUT);
  putar.attach(5);        
}

void loop()
{
  mouster = analogRead(ms);
  
  if (mouster < 200) {
    putar.write(90);   
    digitalWrite(buzzer, HIGH);
  } 
  else {
    putar.write(0);            
    digitalWrite(buzzer, LOW);
  }
  
  delay(100); // Small delay to stabilize sensor readings
}
