#include<stdio.h>
#include<string.h>

void calculation(int a,int b,char c){
  if(c=='+'){
    printf("Result: %d\n", a+b);

  }
   else if(c=='-'){
    printf("Result: %d\n", a-b);

  }
  else if(c=='*'){
    printf("Result: %d\n", a*b);

  }
   else if(c=='/'){
    if(b==0){
      printf("cannot divide by 0\n");
    }
    else{printf("result: %d\n", a/b);}
   

  }


}

int main(){
  printf("welcome to calculator!\n");
  int number1;
  int number2;
  char operator;
  int boo;
  char *yesorno;
  while(boo){
    printf("enter first number: ");
    scanf("%d", &number1);
    printf("enter operator: ");
    scanf(" %c", &operator);
    printf("enter second number: ");
    scanf("%d", &number2);
    calculation(number1,number2,operator);
    printf("do you want to calculate again?\n");
    fgets(yesorno,4,stdin);
    if(strcmp(*yesorno,'yes')){
      boo=1;
    }
    else{boo=0;}



  }
  return 0;
}