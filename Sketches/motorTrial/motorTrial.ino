#include <Servo.h>
Servo ESC;     // create servo object to control the ESC
int potValue;  // value from the analog pin
void setup() {
  // Attach the ESC on pin 9
  ESC.attach(9, 1000, 2000); // (pin, min pulse width, max pulse width in microseconds)

  potValue = 1023; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
  potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
  ESC.write(potValue);    // Send the signal to the ESC

  delay (3000);

  potValue = 0; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
  potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
  ESC.write(potValue);    // Send the signal to the ESC

  delay(3000);
  Serial.begin(9600);

}

void setSpeed(int pot){
  // sets motor to a speed, given a potential value
  int angle = map(pot, 0, 1023, 180, 0);
  ESC.write(angle);
}

void loop() {
  potValue = 10; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
  setSpeed(potValue);
//  delay(1000);
//
////  for (potValue=55; potValue > 0; potValue -= 10){
////    setSpeed(potValue);
////    delay(500);
////  }
//
//  ESC.write(0);
//  delay(1000);
//  potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
//  ESC.write(potValue);    // Send the signal to the ESC
  
//  delay(3000);       // stay at this speed for 3 seconds
//
//  potValue = 0; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
//  potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
//  ESC.write(potValue);    // Send the signal to the ESC

//  delay(3000);      // stay at this speed for 3 seconds
}
