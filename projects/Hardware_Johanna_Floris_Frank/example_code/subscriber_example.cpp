// 02/10/2020 17:30
// author: Kira
// code example for subscriber

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define error    00000000 // reserve empty byte as error message
#define command1 00000001 // command do nothing
#define command2 00000010 // echo message
#define command3 00000011 // read temperature

unsigned char listen(){
	// this function listens to the i2C channel to see if the master sends a command
	// think about proper message handling https://www.arduino.cc/en/Reference/WireRead
	unsigned char master_command;
	
	// when it receives a command it returns the command to give to interpretCommand()
	return master_command
}

void interpretCommand(unsigned char command){
	// this function interprets the command and decides what function to call afterwards
	// a good way to do this effectively is to use switch-case statements https://www.w3schools.com/cpp/cpp_switch.asp
	switch(command){
		case command1:
		// do nothing
		break;
		case command2:
		// echo message
		break;
		case command3:
		// call read temperature and transmit
		break;
		default:
		// in case the command is not understood
		// transmit error byte
	}
}

void readTemperature(){
	// this function reads the temperature from BME and makes it ready to transmit to master
	// think about properly changing the float from BME to a message your master understands
}

void sendMessage(unsigned char reply){
	// this function sends the bytes back to the master
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
