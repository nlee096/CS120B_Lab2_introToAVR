/*	Author: lab
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #  Exercise #
 *	Exercise Description: [optional - include for your own benefit]
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
	DDRB = 0x00; PORTB = 0xFF;
	DDRC = 0x00; PORTC = 0xFF;
	DDRD = 0xFF; PORTD = 0x00;

	//unsigned short us_temp_cnt = 0x00;
	unsigned char us_temp_cnt = 0x00;
	unsigned char uc_temp_out = 0x00;
	//unsigned char uc_temp_convert = 0x00;
	
    while(1){

    //PD0 = 1 if sum weight >140
    	us_temp_cnt = PINA + PINB + PINC;
		if(us_temp_cnt > 0x8C){
			uc_temp_out = 0x01;
		}
		else{
			uc_temp_out = 0x00;
		}
	
	//D = sum weight
	/*
		if(us_temp_cnt > 0x3F){
			while (us_temp_cnt > 0x3F){
				us_temp_cnt = us_temp_cnt >> 1;
			}
		}
		us_temp_cnt = us_temp_cnt << 2;
		uc_temp_convert = (char)us_temp_cnt;
		uc_temp_out = uc_temp_out | uc_temp_convert;
	*/
	//if we assume all weight sums can be represented in 8 bit
		us_temp_cnt = us_temp_cnt >> 2;
		us_temp_cnt = us_temp_cnt & 0xFC;
		uc_temp_out = uc_temp_out | us_temp_cnt;


	//PD1 = 1 if |A-C| > 80
		if(PINA > PINC){
			us_temp_cnt = PINA - PINC;
		}
		else if(PINA < PINC){
			us_temp_cnt = PINC - PINA;
		}
		else{
			us_temp_cnt = 0x00;
		}

		if(us_temp_cnt > 80){
			uc_temp_out = uc_temp_out | 0x02;
		}

		PORTD = uc_temp_out;

    }
    return 1;
}
