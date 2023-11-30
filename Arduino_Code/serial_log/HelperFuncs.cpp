#include "HelperFuncs.h"
#include "Arduino.h"

unsigned long session_val = 1;              // default trial is 1
unsigned long desiredInterval_s = 1;        // 1 min = 60 s  
unsigned long desiredInterval_ms = 1000;    // 1 s   = 1_000 ms 
unsigned long desiredInterval_us = 1000000;

unsigned int interSampleDelay = 50; 
unsigned int interAverageDelay = 1500; 
unsigned int numSamples = 20;


void myDelay_us(unsigned long us)                      // us: duration (use instaed of block func delay())
{   
    unsigned long start_us = micros();                 // start: timestamp
    for (;;) {                                         // for (;;) infinite for loop 
        unsigned long now_us = micros();               // now: timestamp
        unsigned long elapsed_us = now_us - start_us;  // elapsed: duration
        if (elapsed_us >= us)                          // comparing durations: OK
            return;
    }
}