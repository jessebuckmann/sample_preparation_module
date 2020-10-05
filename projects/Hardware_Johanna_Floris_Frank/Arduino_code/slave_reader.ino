#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme;

void setup() {
  Wire.begin(8);                // join i2c bus with address #8
  Wire.onRequest(requestEvent); // register event
}

void loop() {
  delay(500);
}

// function that executes whenever data is requested by master
// this function is registered as an event, see setup()

void requestEvent() {
  Wire.write("hello"); // respond with message of 6 bytes
  // as expected by master
}
