objects = main.o addition.o division.o multiplication.o subtraction.o

calculator: $(objects)
	gcc -o calculator $(objects)

main.o: main.c operations.h
	gcc -c $< -o $@

addition.o: addition.c operations.h
	gcc -c $< -o $@

subtraction.o: subtraction.c operations.h
	gcc -c $< -o $@

multiplication.o: multiplication.c operations.h
	gcc -c $< -o $@

division.o: division.c operations.h
	gcc -c $< -o $@

clean:
	rm -f calculator $(objects)
