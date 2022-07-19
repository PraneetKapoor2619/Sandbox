#include <iostream>


int * Malloc(int);
int * Calloc(int);
int allocate(int *);
int print(int *);
int Free(int *);


using namespace std;


int main(int argc, char **argv)
{
        cout << "Hello world\n" << "Using malloc() to create 4 integer block" << endl;
        
        int *ptr = Malloc(4);
        cout << "Before assigning something...\n";
        print(ptr);
        allocate(ptr);
        cout << "After assigning something...\n";
        print(ptr);
        cout << "Freeing memory " << ptr << "...\n";
        Free(ptr);

        cout  << "Using calloc() to create 4 integer block" << endl;
        Calloc(4);
        cout << "Before assigning something...\n";
        print(ptr);
        allocate(ptr);
        cout << "After assigning something...\n";
        print(ptr);
        cout << "Freeing memory " << ptr << "...\n";
        Free(ptr);

        return 0;
}

/*
same thing!! Adding N to a ptr = ptr + (N * (size of the type of variable ptr points to))
cout << ptr << " " << ptr + 1 << endl;
int i = 0;
cout << &ptr[i];
++i;
cout << " " << &ptr[i] << endl;
*/

int * Malloc(int n)
{
        /*
        malloc() returns a pointer to a block of free memory which has been created.
        (cast-type *) malloc(quantity * sizeof(type));
        malloc() also initializes the elements to zero. Maybe that is how it works under the 
        hood.
        */

        int *ptr = (int *) malloc((n + 1) * sizeof(int));
        ptr[n] = (int) NULL;    // still a good safety check :-)
        return ptr;
}


int * Calloc(int n)
{
        /*
        calloc(), just like malloc, allocates a contiguous block of memory of specified size.
        (cast-type *) calloc(quantity, sizeof(type));
        Note that calloc also initializes ever block with a default value of 0.
        This is not done by malloc().
        */

        int *ptr = (int *) calloc(n + 1, sizeof(int));
        return ptr;
}


int allocate(int *ptr)
{
        /*
        A small subroutine for allocating values to the memory blocks
        */
        for (int i = 0; i < 4; ++i) {
                ptr[i] = i + 1;
        }
        return 0;
}


int print(int *ptr)
{
        /*
        A subroutine for printing a block of memory.
        */

        for (int i = 0; i < 4; ++i) {
                cout << ptr[i] << " ";
        }
        cout << "\n";
        return 0;
}


int Free(int *ptr)
{
        /*
        Note the free() de-allocates the complete block of memory pointed at by the ptr which is 
        its paramater.
        */

        free(ptr);
        cout << "Memory freed successfully!!\n";
        return 0;
}