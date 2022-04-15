#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n;
	string word;
	vector<string> list;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cin >> word;
		list.push_back(word);
	}
	for (auto i:list) {
		if (i.length() <= 10)
			cout << i << endl;
		else
			cout << i[0] << i.length() - 2 << i.back() << endl;
	}
	return 0;
}
