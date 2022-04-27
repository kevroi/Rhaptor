#include <Servo.h>
#include <Arduino_LSM6DS3.h>

Servo ESC_f;    // create servo object to control  front ESC
Servo ESC_s;    // create servo object to control side ESC
Servo brake;    // create servo object for braking
int pot_value;   // value from the analog pin
int pot_low;
int pot_high;
int max_value;
int max_mapped;
int min_value;
int min_mapped;
unsigned long last_time = 0; // time counter for heartbeat
int ang_threshold;
String message;


void setup() {

  // Check IMU
  if (!IMU.begin())
  {
    Serial.println("Failed to initialize IMU!");
  }
  
  // calibrate both ESCs concurrently
  ESC_f.attach(9, 1000, 2000);  // pin 9, PWM of 1000 to 2000 ms
  ESC_s.attach(10, 1000, 2000); // pin 10, PWM of 1000 to 2000 ms
  max_value = 1023;
  max_mapped = int(map(max_value, 0, 1023, 0, 180));
  ESC_f.write(max_mapped);
  ESC_s.write(max_mapped);
  delay(3000);
  min_value = 0;
  min_mapped = int(map(min_value, 0, 1023, 0, 180));
  ESC_f.write(min_mapped);
  ESC_s.write(min_mapped);
  delay(3000);

  // Set parameters for some of the rendering modes
  pot_high = 65;
  pot_low = 51;

  Serial.begin(9600);

}


void setSpeedFront(int pot)
{
  // sets front motor speed to a given potential value
  int angle = map(pot, 0, 1023, 0, 180); // map potential linearly to a servo angle
  ESC_f.write(angle);
}

void setSpeedSide(int pot)
{
  // sets side motor speed to a given potential value
  int angle = map(pot, 0, 1023, 0, 180);
  ESC_s.write(angle);
}


void loop() {
  // put your main code here, to run repeatedly:

  //Print Arduino's heartbeat
  if (millis() > last_time + 2000)
    {
        Serial.println("Arduino is alive!!");
        last_time = millis();
    }

  message = Serial.read();
  if (message == 'A')
    {
      // constant resistive torque
      pot_value = 55;
      setSpeedFront(pot_value);
      setSpeedSide(pot_value);
    }

  if (message = 'R')
    {
      // anti-phase rumble effect
      pot_max = 65;
      pot_min = 51;

      setSpeedFront(pot_high);
      setSpeedSide(pot_low);
      delay(500); // future works can try varying this frequency
      detSpeedFront(pot_low);
      setSpeedSide(pot_high);
    }

  if (message = 'S')
    {
      // in-phase rumble effect
      pot_max = 65;
      pot_min = 51;

      setSpeedFront(pot_high);
      setSpeedSide(pot_high);
      delay(500)
      setSpeedFront(pot_low);
      setSpeedSide(pot_low);
    }

  if (message = 'T')
  {
    // tension effect
    if (IMU.gyroscopeAvailable())
    {
      ang_threshold = 2;
      IMU.readAcceleration(x, y, z);
    
      while ((abs(x)>ang_threshold) || (abs(y)>ang_threshold) || (abs(z)>ang_threshold))
      {
        setSpeedFront(pot_high);
        delay(500);
      }
    }
    else()
    {
      Serial.println("IMU unavailable for tension mapping");
    }

  if (message == 'I')
    {
      // constant resistive torque
      pot_value = 0;
      setSpeedFront(pot_value);
      setSpeedSide(pot_value);
      brake.write(180);
      delay(1000);
      brake.write(0);
    }
  }
  

    
  

}
