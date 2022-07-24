#include <iostream>


using namespace std;


int main(int argc, char **argv)
{
	int N = 10;
	int *ptr = (int *) calloc(N, sizeof(int));
	cout << "ptr -> " << ptr << endl;

	for (int i = 0; i < N; ++i) {
		cout << *(ptr + i) << "  ";
		ptr[i] = i + 1;
	}
	cout << endl;

	for (int i = 0; i < N; ++i) {
		cout << *(ptr + i) << " ";
	}
	cout << endl;

	free(ptr);
	for (int i = 0; i < N; ++i) {
		cout << *(ptr + i) << " ";
	}
	cout << endl;
	return 0;
}