int incomingByte = 0;
int led = 13;
int motor = 12;
int sensor_pin = A1;
#include <dht.h>        // Include library
#define outPin 8        // Defines pin number to which the sensor is connected

dht DHT;   


void setup() {
Serial.begin(9600);
pinMode(led, OUTPUT);
pinMode(motor, OUTPUT);
}

void loop() {
  while (Serial.available() > 0) {  
    incomingByte = Serial.read();
    // String incomingStr = Serial.readString();

      while (incomingByte == "HIGH") {
        motor_high();
      }

      while (incomingByte == "LOW") { 
      motor_low();
    }

  }


  int readData = DHT.read11(outPin);

	float t = DHT.temperature;        // Read temperature
	float h = DHT.humidity;  // Read humidity      

	// Serial.print(t);   // Temperature in celsius
	// Serial.print((t*9.0)/5.0+32.0);        // Convert celsius to fahrenheit

    float moisture_percentage;
    int sensor_analog;
    sensor_analog = analogRead(sensor_pin);
    moisture_percentage = ( 100 - ( (sensor_analog/1023.00) * 100 ) );


    Serial.print(t);
    Serial.print(",");
    Serial.print(h);
    Serial.print(",");
    Serial.print(moisture_percentage);
    delay(500);

    }

    void motor_high() {
    digitalWrite(led, HIGH);
    }

    void motor_low() {
    digitalWrite(led, HIGH);
    }
