#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void main(void)
{
    int loop;
    char conv_flag[2];
    unsigned long data;//整数の表現形式を変える？

    for(loop=1;loop; )
    {
        printf("\n> ");
        if (scanf("%1s",&conv_flag[0])== EOF )
        {
            continue;
        }

        switch (conv_flag[0])
        {
        case 'd':
        case 'D':
            if (scanf("%ld",&data) !=1)
            {   
                scanf("%*s");
                continue;
                /* code */
            }
            printf("=%lX(HEX)",data);
            /* code */
            break;

        case 'h':
        case 'H':
            if (scanf("%lX",&data)!=1)
            {
                scanf("%*s");
                continue;
                /* code */
            }
            printf(" =lu(DEC)",data);
            break;
        case 'q':
        case 'Q':
            loop =0;
            break;
        
        default:
            scanf("%*s" );
            break;
        }
        
    }
}
