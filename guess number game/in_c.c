#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
  srand(time(0));
  int number=rand()%100+1;//random number between 1 and 100
  int input=0;
  int count=0;
 
  
  while(input!=number){
    printf("enter input:\n");
    scanf("%d", &input);
    if(input>number){
      printf("too high\n");
    }
    else if(input<number){
      printf("too small\n");
    }
    count++;
  }
  printf("it took you %d tries\n", count);
  return 0;


}