#ifndef STACK_H_
#define STACK_H_

//Pop, Push, isEmpty
//it will simply store everything as a string with a type 

typedef struct element {
    char value[];
    char type[];
}Element;

typedef struct stack{
    int length;
    char self[];
    //struct of element
} Stack;

int push(int x);
int* pop();
bool isEmpty(int arr[], int length);

#endif // !DEBUG
