#include "HelperFuncs.h"
#include <stdint.h>
#include "Arduino.h"
#include "SPI.h"

uint32_t startAnalogTimer = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

void loop() {

  // Store start Time
  startAnalogTimer = micros();

    // Declare local variable/Buffer 
    unsigned long sum_sensorValue = 0; 


    uint32_t timeBefore = micros();
    // Build buffer: read sensor value then sum it to the previous sensor value 
    for (unsigned int counter = 1; counter <= numSamples; counter++){
      sum_sensorValue += analogRead(A0);
      // Pause for stability 
      myDelay_us(interSampleDelay);
    }
    uint32_t timeAfter = micros();
    // Pause for stability 
    myDelay_us(interAverageDelay);

    // Send the summed data via Serial
    Serial.print(sum_sensorValue);
    Serial.print(",");
    Serial.print(timeBefore);
    Serial.print(",");
    Serial.println(timeAfter);


    // Optional: Reset startAnalogTimer if you want to keep sending data at regular intervals
    startAnalogTimer = micros();
  // }  
}

