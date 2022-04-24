#include <bits/stdc++.h>

using namespace std;

void combinations(vector<int> seed, vector<int> tmp, int sp, int N, int *max) {
	for (sp; sp < N; ++sp) {
		tmp.push_back(seed[sp]);
		if (tmp.size() > N / 2) {
			return;
		}
		else {
			int z = 0;
			for (auto i : tmp) {
				z ^= i;
			}
			if (z >= *max) {
				*max = z;
			}
			combinations(seed, tmp, sp, N, max);
			tmp.pop_back();
		}
	}
	return;
}

int main (int argc, char ** argv) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout << "Hello world!!" << endl;

	int N, max;
	cin >> N;
	vector<int> array, tmp;
	tmp.push_back(1);
	for (int i = 0; i < N; ++i) {
		int p;
		cin >> p;
		array[i] = p;
	}

	max = 0;
	//combinations(array, tmp, 0, N, &max);

	cout << max << endl;
	return 0;
}


