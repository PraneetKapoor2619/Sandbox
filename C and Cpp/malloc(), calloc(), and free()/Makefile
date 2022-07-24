CC = gcc -std=gnu99
CPP = g++ -std=c++11
OBJ = $(wildcard *.o)
ASM = $(wildcard *.s)
OUT = $(wildcard *.out)


# C program using malloc
runMallocC: MallocC.out
	./MallocC.out

MallocC.out: MallocC.o MallocC.s
	$(CC) $< -o $@

MallocC.o: Malloc.c
	$(CC) -c $< -o $@

MallocC.s: Malloc.c
	$(CC) -S $< -o $@


# C++ program using malloc
runMallocCPP: MallocCPP.out
	./MallocCPP.out

MallocCPP.out: MallocCPP.o MallocCPP.s
	$(CPP) $< -o $@

MallocCPP.s: Malloc.cpp
	$(CPP) -S $< -o $@

MallocCPP.o: Malloc.cpp
	$(CPP) -c $< -o $@


# C program to use calloc()
runCallocC: CallocC.out
	./CallocC.out

CallocC.out: CallocC.o CallocC.s
	$(CC) $< -o $@

CallocC.o: Calloc.c
	$(CC) -c $< -o $@

CallocC.s: Calloc.c
	$(CC) -S $< -o $@


# C++ program to use calloc()
runCallocCPP: CallocCPP.out
	./CallocCPP.out

CallocCPP.out: CallocCPP.o CallocCPP.s
	$(CPP) $< -o $@

CallocCPP.o: Calloc.cpp
	$(CPP) -c $< -o $@

CallocCPP.s: Calloc.cpp
	$(CPP) -S $< -o $@


# clean
clean: $(OBJ) $(ASM) $(OUT)
	rm $^