#include <stdint.h>


extern unsigned long session_val;
extern unsigned long desiredInterval_s;
extern unsigned long desiredInterval_ms;
extern unsigned long desiredInterval_us;

/* Fast Board */
extern unsigned int interSampleDelay; 
extern unsigned int interAverageDelay; 
extern unsigned int numSamples; 


void myDelay_us(unsigned long us);