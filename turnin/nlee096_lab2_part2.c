/*	Author: Nathan Lee nlee096@ucr.edu
 *  Partner(s) Name: none
 *	Lab Section: 022
 *	Assignment: Lab #2  Exercise #2
 *	Exercise Description: parking space sensor
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
	DDRA = 0x00; PORTA = 0xFF; 
	DDRC = 0xFF; PORTC = 0x00;
	
	unsigned char tmpA = 0x00;
	//unsigned char tmpB = 0x00;
	
	unsigned char cntavail;
    unsigned char i;

    while(1){
		tmpA = PINA & 0x0F;
		cntavail = 4;
		for(i = 0; i < 4; i++){
			if((tmpA & (0x01 << i)) != 0){
				cntavail = cntavail - 1;
			}
		}
		PORTC = cntavail;
    }
    return 1;
}
