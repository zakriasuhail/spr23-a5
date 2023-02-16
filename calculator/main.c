#include <stdio.h>
#include <stdlib.h>
#include "operations.h"

int main(){
    printf("Welcome to the world's most advanced calculator!\n");
    printf("After years of research and development, we are proud to welcome you to our new and improve calculator.\n");
    
    // Prompt user to select a choice.
    printf("First, choose an operation. Choose one of the following options:\n");
    printf("+ for addition\n");
    printf("* for multiplication\n");
    printf("/ for division\n");
    printf("- for subtraction\n");

    char choice; 
    scanf ("%c", &choice);

    // Prompt user to enter numbers. 
    int a;
    int b;
    printf("Now you will need to enter two numbers: a and b.\n");
    printf("Please enter a value for a: \n");
    scanf("%d", &a);

    printf("Please enter a value for b: \n");
    scanf("%d", &b);

    // Evaluate operation based on user's choice.
    int result; 
    switch (choice){
      case '+':
        result = add(a, b);
      case '-':
        result = subtract(a, b);
      case '*':
        result = multiply(a, b);
      case '/':
        result = divide(a, b);
    }

    printf("The result of your operation is %d\n", result); 

    return 0;
  
}
