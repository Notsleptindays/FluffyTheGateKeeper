//Pin for the LED
int ledPin = 13;
//Input pin for the PIR sensor (Motion sensor)
int sensorPIR = 2; 
//No motion detected
int statePIR = LOW;
//Variable for reading pin status
int value = 0; 

void setup() {
    //Initialize LED as output
    pinMode(ledPin, OUTPUT);
    //Initialize PIR sensor as input 
    pinMode(sensorPIR, INPUT); 
    //Initialize serial
    Serial.begin(9600);
}

void loop(){
    //Read sensor value
    value = digitalRead(sensorPIR);
    //Check input is high
    if (value == HIGH){  
      //Turn the LED on
      digitalWrite(ledPin, HIGH);
      if (statePIR == LOW){
        Serial.println("Motion detected!");
        statePIR = HIGH;
      } 
    }
    else{
      //Turn LED off
      digitalWrite(ledPin, LOW); 
      if (statePIR == HIGH){
        statePIR = LOW;
      } 
   }
   delay(1000);
}
