#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>

#define MAX 256
#define ALPHA 26

void main(void)
{
    char str[MAX];
    int alpha[ALPHA];
    int i;

    memset(&alpha[0],'\0',sizeof alpha );//初期化
    for ( ; scanf("%s",&str[0]) !=EOF; )
    {
        for ( i = 0; str[i]!='\0'; i++)
        {
            if(isalpha(str[i]))
            {
                str[i]=(char)toupper(str[i]);
                (alpha[str[i]-'A'])++;
            }
        }

        for ( i = 0; i < ALPHA; i++)
        {
            if((i%5)==0)
            {
                putchar('\n');
            }
            /* code */
        }
        
        
    }
    
}