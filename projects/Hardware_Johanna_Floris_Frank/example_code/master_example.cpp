// 02/10/2020 17:30
// author: Kira
// code example for master

#include <Wire.h>

#define error    00000000 // reserve empty byte as error message
#define command1 00000001 // command do nothing
#define command2 00000010 // echo message
#define command3 00000011 // read temperature

void sendCommand(unsigned char command){ // unsigned char is exactly 1 byte large (like your commands)
	// this function sends a command to a subscriber
	// think about proper message handling https://www.arduino.cc/en/Reference/WireWrite
}

void listen(){
	// this function listens to the subscriber and saves/writes-to-file the received message
	// think about how long you want each message to be so that you can listen the correct number of bytes
}

void setup(){
	Serial.begin();
	Wire.begin();
	Wire.SetClock();
}

void loop(){
	sendCommand();
	listen();
}