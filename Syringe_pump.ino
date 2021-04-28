
/*Example sketch to control a stepper motor with A4988 stepper motor driver, AccelStepper library and Arduino: continuous rotation. More info: https://www.makerguides.com */
// Include the AccelStepper library:
#include <AccelStepper.h>
/// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver:
// Enable Pin
#define enPin 8         //Shield v3 enable Pin for all steppers
// Stepper 1
#define dirPin_1 5      //Shield v3 x-axis
#define stepPin_1 2     //Shield v3 x-axis
#define motorInterfaceType_1 1
// Stepper 2
#define dirPin_2 6      //Shield v3 y-axis
#define stepPin_2 3     //Shield v3 y-axis
#define motorInterfaceType_2 1
// Stepper 3
#define dirPin_3 7       //Shield v3 z-axis
#define stepPin_3 4      //Shield v3 z-axis
#define motorInterfaceType_3 1
/// Create instances of the AccelStepper class:
AccelStepper stepper_1 = AccelStepper(motorInterfaceType_1, stepPin_1, dirPin_1);
AccelStepper stepper_2 = AccelStepper(motorInterfaceType_2, stepPin_2, dirPin_2);
AccelStepper stepper_3 = AccelStepper(motorInterfaceType_3, stepPin_3, dirPin_3);

/// Define global variables
float steps_per_second_p1 = 0;
float steps_per_second_p2 = 0;
float steps_per_second_p3 = 0;
float total_steps_p1 = 0;
float total_steps_p2 = 0;
float total_steps_p3 = 0;

void setup() {
  //Setup Serial
  Serial.begin(230400);
  //Set pin modes
  pinMode(enPin, OUTPUT);
  digitalWrite(enPin, HIGH); //deactivate drivers (LOW active)
  
  pinMode(dirPin_1, OUTPUT);
  pinMode(dirPin_2, OUTPUT);
  pinMode(dirPin_3, OUTPUT);
  digitalWrite(dirPin_1, LOW); //LOW or HIGH
  digitalWrite(dirPin_2, LOW); //LOW or HIGH
  digitalWrite(dirPin_3, LOW); //LOW or HIGH
  pinMode(stepPin_1, OUTPUT);
  pinMode(stepPin_2, OUTPUT);
  pinMode(stepPin_3, OUTPUT);
  digitalWrite(stepPin_1, LOW);
  digitalWrite(stepPin_2, LOW);
  digitalWrite(stepPin_3, LOW);

  digitalWrite(enPin, LOW); //activate drivers
  
  // Set the maximum speed in steps per second:
  stepper_1.setMaxSpeed(4000);
  stepper_2.setMaxSpeed(4000);
  stepper_3.setMaxSpeed(4000);

  //Set Current Position
  stepper_1.setCurrentPosition(0);
  stepper_2.setCurrentPosition(0);
  stepper_3.setCurrentPosition(0);
}
void loop() {

  if (Serial.available() > 0) {
    // read the incoming byte:
    String command_data = Serial.readStringUntil('\n');

    String steps_per_second_1 = getValue(command_data, '_',0);
    String total_steps_1 = getValue(command_data, '_',1);
    
    String steps_per_second_2 = getValue(command_data, '_',2);
    String total_steps_2 = getValue(command_data, '_',3);
    
    String steps_per_second_3 = getValue(command_data, '_',4);
    String total_steps_3 = getValue(command_data, '_',5);
  
    steps_per_second_p1 = steps_per_second_1.toFloat();
    total_steps_p1 = total_steps_1.toFloat();
    stepper_1.setCurrentPosition(0);

    steps_per_second_p2 = steps_per_second_2.toFloat();
    total_steps_p2 = total_steps_2.toFloat();
    stepper_2.setCurrentPosition(0);

    steps_per_second_p3 = steps_per_second_3.toFloat();
    total_steps_p3 = total_steps_3.toFloat();
    stepper_3.setCurrentPosition(0);
  }
  
  if (stepper_1.currentPosition() != total_steps_p1) {
     stepper_1.setSpeed(steps_per_second_p1);
     stepper_1.runSpeed(); 
     //Serial.println(stepper_1.currentPosition());
  }
  if (stepper_2.currentPosition() != total_steps_p2) {
     stepper_2.setSpeed(steps_per_second_p2);
     stepper_2.runSpeed();      
  }
  if (stepper_3.currentPosition() != total_steps_p3) {
     stepper_3.setSpeed(steps_per_second_p3);
     stepper_3.runSpeed();    
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
