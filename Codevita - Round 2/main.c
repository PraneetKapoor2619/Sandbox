#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

int x; 

int solve()
{
	extern int x; 
	string number;
	number = to_string(x);
	int s = number.length();
	int m;
	if (s % 2 == 0)
		m = s / 2;
	else
		m = (s - 1) / 2;
	int flag = 1;
	for (int i = 0; i < m; ++i) {
		if (number[i] != number[s - i - 1]) {
			flag = 0;
			break;
		}
	}
	if (flag == 1)
		return true;
	else
		return false;
}

int main(int argc, char ** argv)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	/*********************************************
	 * INSERT VALUES HERE
	 *********************************************
	 */
	{
		extern int x;
		cin >> x;
	}
	/*********************************************
	 * CALL FUNCTION HERE
	 *********************************************
	 */
	auto start = high_resolution_clock::now();
	int ret = solve();
	cout << ret << endl;
	auto stop = high_resolution_clock::now();
	auto duration = duration_cast<microseconds>(stop - start);
	/*********************************************
	 * TIME IS DISPLAYED HERE
	 *********************************************
	 */
	cout << "Completed in " << duration.count()  << " us" << endl;
	return 0;
}

