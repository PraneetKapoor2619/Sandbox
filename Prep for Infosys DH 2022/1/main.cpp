#include <bits/stdc++.h>

using namespace std;

int swap (string &input, int i, int N, int a, int *cash) {
	if (*cash >= a) {
		for (int j = N - 1; j > i; --j) {
			if (input[i] == '1' && input[j] == '0') {
				input[i] = '0';
				input[j] = '1';
				*cash -= a;
				return 0;
			}
		}
	}
	return 1;
}

int flip (string &input, int i, int N, int b, int *cash) {
	if (*cash >= b) {
		if (input[i] == '1') {
			input[i] = '0';
			*cash -= b;
			return 0;
		}
	}
	return 1;
}

int main (int argc, char ** argv) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string input;
	int N, cash, a, b;
	cin >> N >> input >> cash >> a >> b;
	
	for (int i = 0; i < N && cash > 0; ++i) {
		if (a <= b) {
			if(swap(input, i, N, a, &cash) != 0)
				flip(input, i, N, b, &cash);
		}
		else {
			if(flip(input, i, N, b, &cash) != 0)
				swap(input, i, N, a, &cash);
		}
	}
	
	long int result = 0;
	for (int i = 0; i < N; ++i)
		result += ((input[i] - '0') * pow(2, N - 1 - i));
	cout << result << endl;
	return 0;
}


