#include <Servo.h>
Servo ESC;     // create servo object to control the ESC
int potValue;  // value from the analog pin
unsigned long last_time = 0;

void setup()
{
      // Attach the ESC on pin 9
    ESC.attach(9,1000,2000); // (pin, min pulse width, max pulse width in microseconds) 
    
    potValue = 1023; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
    potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
    ESC.write(potValue);    // Send the signal to the ESC
    
    delay (3000);
    
    potValue = 0; //analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
    potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
    ESC.write(potValue);    // Send the signal to the ESC
    
    delay(3000);

    potValue = 65;
    Serial.begin(9600);
}

void setSpeed(int pot)
{
    // sets motor to a speed, given a potential value
    int angle = map(pot, 0, 1023, 0, 180);
    ESC.write(angle);
}

void loop()
{
    // Print a heartbeat
    if (millis() > last_time + 2000)
    {
        Serial.println("Arduino is alive!!");
        last_time = millis();
    }

    Serial.print(Serial.read());

//    // Read character sent and perform required action
//    if (Serial.read() == 'H')
//    {
//        setSpeed(potValue);
//        delay(5000);
//        setSpeed(0);
//        // Serial.println("Received an A");
//    }
}
