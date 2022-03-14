all: prog2_part1 prog2_part2

prog2_part1: prog2_part1.c
	gcc -o prog2_part1 -Wno-implicit-int -Wno-implicit-function-declaration -Wno-return-type -g prog2_part1.c

prog2_part2: prog2_part2.c
	gcc -o prog2_part2 -Wno-implicit-int -Wno-implicit-function-declaration -Wno-return-type -g prog2_part2.c

run_prog2_part1:
	printf "11\n0.1\n0.3\n1000\n2\n" | ./prog2_part1 > prog2_part1.log

run_prog2_part2:
	printf "40\n0.2\n0.2\n10\n2\n" | ./prog2_part2 > prog2_part2.log

clean:
	rm -rf prog2_part1 prog2_part1