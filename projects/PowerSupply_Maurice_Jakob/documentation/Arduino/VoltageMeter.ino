/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

}

// the loop routine runs over and over again forever:
void loop() {
  double R1 = 19.9; // resistance of resistor in voltage divider in kOhms
  double R2 = 4.7;
  double factor = (R1+R2)/R2; //ratio to go from measured voltage to actual voltage of battery
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  double voltage = factor * sensorValue * 3.3 /1024;//latter factor is to turn a digital value into a voltage
  // print out the value you read:
  Serial.println(voltage);
  delay(1);        // delay in between reads for stability
}
