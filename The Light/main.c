#include <stdlib.h>
#include <stdio.h>

int main(){
    short *ptr,sum;
    int i,lines=0;
    char ch;
    FILE *file;
    file = fopen("input.txt", "r");
    while(!feof(file)){
        ch = fgetc(file);
        if(ch == '\n'){
            lines++;
        }
    }
    ptr=(short*) calloc(2*lines,sizeof(short));
}