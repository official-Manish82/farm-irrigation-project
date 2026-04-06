// implementation  of all stack operations.
#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int stack[MAX];
int top = -1;

// Function to push an element onto the stack
void push(int x) {
    if (top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = x;
    printf("%d pushed to stack\n", x);
}

// Function to pop an element from the stack
int pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    int x = stack[top--];
    printf("%d popped from stack\n", x);
    return x;
}

// Function to return the top element without popping
int peek() {
    if (top == -1) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack[top];
}

// Function to check if stack is empty
int isEmpty() {
    return top == -1;
}

// Function to check if stack is full
int isFull() {
    return top == MAX - 1;
}

// Function to display the stack
void display() {
    if (top == -1) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack elements: ");
    for (int i = 0; i <= top; i++) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}

int main() {
    push(10);
    push(20);
    push(30);
    display();
    printf("Top element: %d\n", peek());
    pop();
    display();
    printf("Is stack empty? %s\n", isEmpty() ? "Yes" : "No");
    printf("Is stack full? %s\n", isFull() ? "Yes" : "No");
    return 0;
}