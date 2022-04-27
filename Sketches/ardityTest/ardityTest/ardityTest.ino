String data;      // signal from Unity

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    data = Serial.read();
    
    if(data == "A"){
      Serial.println('A');
    }
    else {
      Serial.println(data);
    }
}
