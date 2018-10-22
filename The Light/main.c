#include <stdlib.h>
#include <stdio.h>

int roomcheck(short time,short *ptr,short length){
    for(int i=0;i<=length;i+=2){
        if(ptr[i]<time+0.5&&time+0.5<ptr[i+1]){
            return 1;
        }
    }
    return 0;
}

int main(){
    short *ptr,sum,i,streak=0,f=0,j,max=-1,min=25,maxstreak=-1;
    int lines=1;
    char ch;
    FILE *file;
    file = fopen("input.txt","r");
    while(!feof(file)){
        ch = fgetc(file);
        if(ch == '\n'){
            lines++;
        }
    }
    rewind(file);
    ptr=(short*)malloc(2*lines*sizeof(short));
    for(i=0;i<2*lines;i+=2){
        fscanf(file,"%hi %hi",&ptr[i],&ptr[i+1]);
        if(ptr[i+1]>max) max=ptr[i+1];
        if(ptr[i]<min) min=ptr[i];
        
    }
    for(i=min;i<=max;i++){
        if(roomcheck(i,ptr,2*lines)){
            streak+=1;
        }
        else{
            if(maxstreak<streak) maxstreak=streak;
            streak=0;
        }
    }
    if(maxstreak<streak) maxstreak=streak;
    FILE *out;
    out=fopen("output.txt","w");
    fprintf(out,"%hi",maxstreak);
    free(ptr);
}