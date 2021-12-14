/*	Author: Nathan Lee nlee096@ucr.edu
 *  Partner(s) Name: none
 *	Lab Section: 022
 *	Assignment: Lab #2  Exercise #1
 *	Exercise Description: Garage open at night
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
	DDRB = 0xFF; PORTB = 0x00;
	unsigned char tmpB = 0x00;
	unsigned char tmpA = 0x00;
    while(1){
		tmpA = PINA;
		if ((tmpA & 0x03) == 0x01) {
			tmpB = 0x01; 
		} else {
			tmpB = 0x00;
		}	
	PORTB = tmpB;
    }
    return 1;
}
