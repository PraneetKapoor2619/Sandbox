#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int M, N, r, c;
	cin >> M >> N;
	int array[M][N];
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> array[i][j];
			if (array[i][j] == 0) {
				r = i;
				c = j;
			}
		}
	}
	int least, r1, c1, rp, cp, br, er, bc, ec, sum;
	sum = 0;
	while (r != 0 && c != 0) {
		least = 11e+04;
		if (r - 1 < 0)
			br = 0;
		else
			br = r - 1;
		if (c - 1 < 0)
			bc = 0;
		else
			bc = c - 1;
		if (r + 1 > M - 1)
			er = M - 1;
		else 
			er = r + 1;
		if (c + 1 > N - 1)
			ec = N - 1;
		else 
			ec = c + 1;
		for (int i = br; i <= er; ++i) {
			for (int j = bc; j <= ec; ++j) {
				if (array[i][j] < least && ((i != r) || (j != c)) && ((i != rp)||(j != cp))) {
					least = array[i][j];
					r1 = i;
					c1 = j;
				}
			}
		};
		rp = r;
		cp = c;
		r = r1;
		c = c1;
		sum += least;
	}
	cout << sum << endl;
	return 0;
}
