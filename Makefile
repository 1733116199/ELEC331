prog2_part1: prog2_part1.c
	gcc -o prog2_part1 -Wno-implicit-int -Wno-implicit-function-declaration -Wno-return-type -g prog2_part1.c

run_prog2_part1:
	printf "10\n0.1\n0.3\n100.0\n2\n" | ./prog2_part1 > prog2_part1.log

clean:
	rm -rf prog2*