#include <TimeLib.h>


void epoch_to_utc();
void string_time();

struct time_data {
	long int epoch, displacement;
	int day, month, year, hour, minute, second;
	bool ampm;
	String time_string;
};
struct time_data td1;


void setup()
{
	//td1.epoch is set here
	td1.epoch = 1646139874;

	//India is +5:30 ahead of GMT. 
	//+5:30 = 19800;
	td1.displacement = +19800;	
	td1.epoch += td1.displacement;

	Serial.begin(115200);
	Serial.println("Starting computations now...");
}


/*
* get the epoch time
* pass it to a function which manipulates variables in a structure storing DD:MM:YYYY, hh:mm:ss
*/
void loop()
{
	static double init = millis();
	if ((millis() - init) / 1000.0 >= 1) {
		++td1.epoch;
		init = millis();
	}
	epoch_to_utc();
	string_time();
	Serial.println(td1.time_string);
}


void epoch_to_utc()
{
	td1.day = day(td1.epoch);
	td1.month = month(td1.epoch);
	td1.year = year(td1.epoch);
	td1.hour = hour(td1.epoch);
	if (td1.hour > 12)
		td1.hour -= 12;
	td1.minute = minute(td1.epoch);
	td1.second = second(td1.epoch);
	td1.ampm = isAM(td1.epoch);
}


void string_time()
{
	td1.time_string = "";
	if (td1.day < 10)
		td1.time_string += "0";
	td1.time_string += String(td1.day) + "/";

	if (td1.month < 10)
		td1.time_string += "0";
	td1.time_string += String(td1.month) + "/";
	td1.time_string += String(td1.year) + ", ";
	
	if (td1.hour < 10)
		td1.time_string += "0";
	td1.time_string += String(td1.hour) + ":";
	
	if (td1.minute < 10)
		td1.time_string += "0";
	td1.time_string += String(td1.minute) + ":";

	if (td1.second < 10)
		td1.time_string += "0";
	td1.time_string += String(td1.second) + " ";

	if (td1.ampm == 1)
		td1.time_string += "AM";
	else
		td1.time_string += "PM";
}
