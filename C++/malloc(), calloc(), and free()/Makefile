run: main.out
	./main.out

main.out: main.o main.s
	g++ $< -o $@

main.o: main.cpp
	g++ -c -std=c++11 -O0 -Wall $<

main.s: main.cpp
	g++ -S -std=c++11 -O0 -Wall $<