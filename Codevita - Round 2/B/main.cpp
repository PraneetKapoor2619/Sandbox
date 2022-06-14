#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, count = 0, total = 1;
	cin >> n;
	vector<int> list(n), range(n);
	iota(begin(list), end(list), 1);
	iota(begin(range), end(range), 1);
	swap(list[0], list[1]);
	auto vb = list.begin();
	auto ve = list.end();
	int first = list[0];
	for (int i = 1; i <= (n - 1); ++i)
		total *= i;
	do {
		if (list[0] != first)
			break;
		for (auto i:range) {
			if (i == list[i]) {
				++count;
				break;
			}
		}
		for (auto i:list)
			cout << i << " ";
		cout << endl;
	} while (next_permutation(begin(list), end(list)));
	cout << count << endl;
	cout << total + ((n - 1)*count) << endl;
	return 0;
}
