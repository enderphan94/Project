#include <stdio.h>
#include <string.h>



void point(char* begin){
    char temp;
    char* end;
    end = begin + strlen(begin)-1;
	printf ("end %s \n",end);
    while(end>begin){
        temp = *end;
        *end = *begin;
        *begin = temp;
        end--;
        begin++;
    } 
}
int main(){
    char string[]= "abcdefgh";
    point(string);
    printf("%s \n", string);
}
