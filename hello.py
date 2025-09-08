#include <stdio.h>
#include <string.h>

int main() {
    char name[100];
    
    printf("Hello! What's your name? ");

    scanf("%s", name);
      
    printf("Have a good day, %s!\n", name);
    
    
    return 0;
}
