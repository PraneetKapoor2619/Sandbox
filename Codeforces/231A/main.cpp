#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n, c1, c2, c3, total;
	cin >> n;
	total = 0;
	while ( n > 0) {
		cin >> c1 >> c2 >> c3;
		if (c1 + c2 + c3 >= 2)
			++total;
		--n;
	}
	cout << total;
	return 0;
}
