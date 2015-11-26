#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>

int main ( int argc, char ** argv )
{
    FILE * numbers = fopen ("numbers","w");
    FILE * ans = fopen ( "answer", "w" );
    int a[100];
    srand ( time(NULL) );
    for ( int i=0;i<atoi(argv[1]);++i )
    {
        a[0] = rand();
        int min = rand();
        int idx = 0;
        fprintf ( numbers, "%d", a[0] );
        for ( int j=1;j<100;++j )
        {
            a[j] = rand();
            if ( min > a[j] )
            {
                min = a[j];
                idx = j;
            }
            fprintf ( numbers, " %d", a[j] );
        }
        fprintf ( numbers, "\n" );
        fprintf ( ans, "%d\n", idx );
    }
    fclose ( numbers );
    fclose ( ans );
}
