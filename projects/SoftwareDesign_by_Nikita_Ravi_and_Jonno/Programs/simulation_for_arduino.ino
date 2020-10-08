#include "Wire.h" // imports the wire library for talking over I2C

float tempC; // Variable for holding temp in C

float pressure; //Variable for holding pressure reading

int i = 0;

unsigned long mstime;

void setup() {
    Serial.begin(9600);
}

void loop() {
    if (i <= 100) {
        tempC = i; // Read Temperature

        pressure = 10 * sqrt(i); //Read Pressure

        mstime = millis();

        Serial.print(mstime);

        Serial.print(",");

        Serial.print(tempC);

        Serial.print(",");

        Serial.println(pressure);

        delay(100);



        i += 1;
    }
    else {

        i = 1;
        delay(100);
    }
}