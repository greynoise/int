#include <stdio.h>

int main(int argc, char *argv[]) {
    int i0;
    int i1;

    scanf("%d", &i0);
    printf("%d;", i0);
    scanf("%d", &i1);
    printf("%d;", i1);

    int res = 0;
    res = i0 + i1; 
    fprintf(stderr, "%d;", res);



    //return;
}
