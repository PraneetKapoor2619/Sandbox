#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using namespace std::chrono;

int solve()
{
	double pi = 3.141592653589793;
	double r1, r2, s1, s2, t, d;
	cin >> r1 >> r2 >> s1 >> s2 >> t >> d;

	double e1, e2, f1, f2, w1, w2;
	e1 = 0;
	f1 = 2 * acos((pow(r1, 2) + pow(d, 2) - pow(r2, 2)) / (2 * r1 * d));
	e2 = 2 * acos((pow(r2, 2) + pow(d, 2) - pow(r1, 2)) / (2 * r2 * d));
	f2 = 0;
	w1 = s1 / r1;
	w2 = s2 / r2;
	
	vector<int> me1, mf1, me2, mf2;
	for (int n = 0 ; ; ++n) {
		int t1 = (e1 + (2*pi*n)) / w1;
		if ((int)t1 != 0)
			if (t1 <= t)
				me1.insert(me1.end(), (int)t1);
			else
				break;
		t1 = (f1 + (2*pi*n)) / w1;
		if ((int)t1 != 0)
			if (t1 <= t)
				mf1.insert(mf1.end(), (int)t1);
			else
				break;
	}
	for (int n = 0 ; ; ++n) {
		int t1 = (e2 + (2*pi*n)) / w2;
		if ((int)t1 != 0)
			if (t1 <= t)
				me2.insert(me2.end(), (int)t1);
			else
				break;
		t1 = (f2 + (2*pi*n)) / w2;
		if ((int)t1 != 0)
			if (t1 <= t)
				mf2.insert(mf2.end(), (int)t1);
			else
				break;
	}

	vector<int> E(me1.size() + me2.size());
	set_intersection(me1.begin(), me1.end(), me2.begin(), me2.end(), E.begin());
	vector<int> F(mf1.size() + mf2.size());
	set_intersection(mf1.begin(), mf1.end(), mf2.begin(), mf2.end(), F.begin());

	if (e1 != f1)
		if (E.size())
			cout << E[0] << " E" << endl;
		else
			cout << F[0] << " F" << endl;
	else if (e1 == f1)
		cout << E[0] << " E&F" << endl;
	else
		cout << "no crash" << endl;
	
	return 0;
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

	}
	/*********************************************
	 * CALL FUNCTION HERE
	 *********************************************
	 */
	auto start = high_resolution_clock::now();
	solve();
	auto stop = high_resolution_clock::now();
	auto duration = duration_cast<microseconds>(stop - start);
	/*********************************************
	 * TIME IS DISPLAYED HERE
	 *********************************************
	 */
	cout << "Completed in " << duration.count()  << " us" << endl;
	return 0;
}

