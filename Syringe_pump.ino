
/*Example sketch to control a stepper motor with A4988 stepper motor driver, AccelStepper library and Arduino: continuous rotation. More info: https://www.makerguides.com */
// Include the AccelStepper library:
#include <AccelStepper.h>

/// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver:
// Stepper pump
#define enPin_pump_1 12
#define ms1Pin_pump_1 11 
#define ms2Pin_pump_1 10    
#define stepPin_pump_1 9   
#define dirPin_pump_1 8     
#define motorInterfaceType_pump_1 1

/// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver:
// Stepper pump
#define enPin_pump_2 7
#define ms1Pin_pump_2 6 
#define ms2Pin_pump_2 5    
#define stepPin_pump_2 19    //Analog 5   
#define dirPin_pump_2 20     //Analog 6     
#define motorInterfaceType_pump_2 1

//spreadPin controls modi between 0=stealthChop and 1=spreadCycle of all connected stepper drivers (TMC220x)
#define spreadPin 2  

/// Create instances of the AccelStepper class:
AccelStepper stepper_1 = AccelStepper(motorInterfaceType_pump_1, stepPin_pump_1, dirPin_pump_1);
AccelStepper stepper_2 = AccelStepper(motorInterfaceType_pump_2, stepPin_pump_2, dirPin_pump_2);

/// Define global variables
float steps_per_second_pump_1 = 0;
float steps_per_second_pump_2 = 0;
float total_steps_pump_1 = 0;
float total_steps_pump_2 = 0;

void setup() {
  //Setup Serial
  Serial.begin(115200);
  
  //Deactivate driver (HIGH deactive)
  pinMode(enPin_pump_1, OUTPUT);
  pinMode(enPin_pump_2, OUTPUT);
  digitalWrite(enPin_pump_1, HIGH); 
  digitalWrite(enPin_pump_2, HIGH);
  
  //Set dirPin to LOW
  pinMode(dirPin_pump_1, OUTPUT);
  pinMode(dirPin_pump_2, OUTPUT);
  digitalWrite(dirPin_pump_1, LOW); 
  digitalWrite(dirPin_pump_2, LOW); 
  
  //Set stepPin to LOW
  pinMode(stepPin_pump_1, OUTPUT);
  pinMode(stepPin_pump_2, OUTPUT);
  digitalWrite(stepPin_pump_1, LOW);
  digitalWrite(stepPin_pump_2, LOW);
  
  //Set modi between 0=stealthChop and 1=spreadCycle of all connected stepper drivers (TMC220x)
  pinMode(spreadPin, OUTPUT);
  digitalWrite(spreadPin, HIGH);
  
  //Set pump stepper to 1/16 microstepping
  pinMode(ms1Pin_pump_1, OUTPUT);
  digitalWrite(ms1Pin_pump_1, HIGH);
  pinMode(ms2Pin_pump_1, OUTPUT);
  digitalWrite(ms2Pin_pump_1, HIGH);
  
  //Set fraction stepper to 1/16 microstepping
  pinMode(ms1Pin_pump_2, OUTPUT);
  digitalWrite(ms1Pin_pump_2, HIGH);
  pinMode(ms2Pin_pump_2, OUTPUT);
  digitalWrite(ms2Pin_pump_2, HIGH);

  //Activate Driver
  digitalWrite(enPin_pump_1, LOW); 
  digitalWrite(enPin_pump_2, LOW); 
  
  //Set the maximum speed in steps per second:
  stepper_1.setMaxSpeed(4000);
  stepper_2.setMaxSpeed(4000);

  //Set Current Position
  stepper_1.setCurrentPosition(0);
  stepper_2.setCurrentPosition(0);
}
void loop() {

  if (Serial.available() > 0) {
    // read the incoming byte:
    String command_data = Serial.readStringUntil('\n');

    String data_steps_per_second_pump_1 = getValue(command_data, '_',0);
    String data_total_steps_pump_1 = getValue(command_data, '_',1);
    
    String data_steps_per_second_pump_2 = getValue(command_data, '_',2);
    String data_total_steps_2 = getValue(command_data, '_',3);
    
  
    steps_per_second_pump_1 = data_steps_per_second_pump_1.toFloat();
    total_steps_pump_1 = data_total_steps_pump_1.toFloat();

    steps_per_second_pump_2 = data_steps_per_second_pump_2.toFloat();
    total_steps_pump_2 = data_total_steps_2.toFloat();

    stepper_1.setCurrentPosition(0);
    stepper_2.setCurrentPosition(0);

    Serial.println("Total steps pump 1: " + String(total_steps_pump_1));
    Serial.println("Speed pump 1: " + String(steps_per_second_pump_1));
    Serial.println("Total steps pump 2: " + String(total_steps_pump_2));
    Serial.println("Speed pump 2: " + String(steps_per_second_pump_2));
  }
  
  if (stepper_1.currentPosition() != total_steps_pump_1) {
     stepper_1.setSpeed(steps_per_second_pump_1);
     stepper_1.runSpeed(); 
     //Serial.println(stepper_1.currentPosition());
  }
  if (stepper_2.currentPosition() != total_steps_pump_2) {
     stepper_2.setSpeed(steps_per_second_pump_2);
     stepper_2.runSpeed();      
  }
}
  
String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
