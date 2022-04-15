#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n, k, benchmark, result;
	cin >> n >> k;
	vector<int> score_list;
	while (n > 0) {
		int score;
		cin >> score;
		score_list.push_back(score);
		--n;
	}
	benchmark = score_list[k - 1];
	result = 0;
	for (auto i:score_list)
		if (i >= benchmark && i > 0)
			++result;
	cout << result;
	return 0;
}
