#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int minutes();
int control();
int operation();

int main(int argc, char **argv)
{
        while (1) {
                control();
        }
        return 0;
}

int minutes()
{
        time_t now = time(NULL);
        struct tm *tm_struct = localtime(&now);
        int min = tm_struct->tm_min;
        return min;
}

int control()
{
        static int TARGET_SET_FLAG;
        static int target;
        int interval = 1;

        if (TARGET_SET_FLAG == 0) {
                target = minutes() + interval;
                printf("Target set -> %d\n\n", target);
                TARGET_SET_FLAG = 1;               
        }

        else if ((TARGET_SET_FLAG == 1) && (minutes() == target)) {
                operation();
                TARGET_SET_FLAG = 0;
        }

        return 0;
}

int operation()
{
        printf("Doing some operation\n");
        return 0;
}