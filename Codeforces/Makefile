path := 50A/
path := $(path)main.cpp
$(info path=$(path))

all: main.exe
	./main.exe

main.exe: main.o
	g++ main.o -o main.exe

main.o: $(path)
	g++ -c $(path)
