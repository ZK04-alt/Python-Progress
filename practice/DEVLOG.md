## Week 1 (Jan 1 – Jan 7)

### What I worked on
- Wrote multiple beginner-level Python programs:
  - Calculator
  - Number checker
  - Menu selection program
- Intentionally avoided using functions (except `main`) and loops to focus on
  understanding core flow and syntax.

### What I learned
- Refreshed Python syntax for:
  - Input and output handling
  - `if–elif–else` logic
  - `match–case` statements


### Problems I faced
- Incorrect results when user input was not converted properly to integers
- Logical mistakes in condition ordering that caused unexpected outputs
- Minor syntax errors while using `match–case`

### How I solved them
- Explicitly converted inputs using `int()` and tested with multiple values
- Reordered conditions to ensure correct logic flow


### Improvements to make next week
- Start using functions to reduce repetition
- Introduce loops for better structure
- Focus on writing cleaner, more readable code
- Maintain consistency and avoid developing bad habits early



## Week 2 (Jan 7 – Jan 14)

### What I worked on
- Wrote multiple beginner-level Python program:
  - Calculator with functions
  - ATM simulator
  - number guessing game
  - password validator/checker


### What I learned
- Using the random library to generate a random integer for the guessing game.
- Syntax, usage and application of both for and while loops.
- The use funtions to make code more modular and readable.
- Input validation using try and except blocks and various error types such as ValueError
- There is no need to use == to check if a variable has true or false value just use if variable: or if not variable
- Use of many built-in functions such as; split(), isalpha(), isnumeric()



### Problems I faced
- Setting up loop corectly to display number of attempts left and loop 10 times in number guessing game
- the correct answer when input in number guessing game was also always being flagged wrong, found through printing random num generated and inputing it.
- at first struggled to make code for password checker readable and understandable as there were too many if elif statements

### How I solved them
- was initializing count at start of attempt counter function so it would always display 9 attempts left, learned how to make
  and use global variables as count variable was assigned value of 10 at the start of program not in funtion
- Realized was equaiting the guess received in str to rand gen in int so was always getting flagged wrong
- re wrote program while giving each feature and requirement of program to one function


### Improvements to make next week
- keep learning more and ensuring code is readable.
- make codes more modualar on first try, or code with the intention of making program modular.
