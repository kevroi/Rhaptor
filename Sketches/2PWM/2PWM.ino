#include <Servo.h>
Servo ESC_front;     // create servo object to control the ESC
Servo ESC_side;
int potValue;  // value from the analog pin
void setup() {
  // Attach the ESC on pin 9
  ESC_front.attach(9, 1000, 2000); // (pin, min pulse width, max pulse width in microseconds)
  ESC_side.attach(10, 1000, 2000);

  potValue = 1023; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
  potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
  ESC_front.write(potValue);    // Send the signal to the ESC
  ESC_side.write(potValue);

  delay (3000);

  potValue = 0; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
  potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
  ESC_front.write(potValue);    // Send the signal to the ESC
  ESC_side.write(potValue);

  delay(3000);
  Serial.begin(9600);

}

void setSpeed_front(int pot){
  // sets motor to a speed, given a potential value
  int angle = map(pot, 0, 1023, 180, 0);
  ESC_front.write(angle);
}

void setSpeed_side(int pot){
  // sets motor to a speed, given a potential value
  int angle = map(pot, 0, 1023, 180, 0);
  ESC_side.write(angle);
  delay(500);
  ESC_side.write(0);
}

void loop() {
  potValue = 60; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
  setSpeed_front(potValue);
  setSpeed_side(potValue);
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
