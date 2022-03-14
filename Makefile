prog2: prog2.c
	gcc -o prog2 -Wno-implicit-int -Wno-implicit-function-declaration -g prog2.c

run_prog2:
	printf "10\n0.2\n0.2\n100.0\n3\n" | ./prog2

clean:
	rm -rf prog2