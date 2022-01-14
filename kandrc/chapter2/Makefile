SOURCE = main

run: a.out
	./a.out

a.out: $(SOURCE).o
	gcc $(SOURCE).o
	
obj.o: $(SOURCE)
	gcc -c $(SOURCE).c
	
debug: $(SOURCE)
	gcc -g -Wall $(SOURCE).c
	gdb a.out