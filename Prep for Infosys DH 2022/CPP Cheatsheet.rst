Date: 21.04.2022

Things related strings and vectors. 
The following for each:
* declaration

* initialization

* Insertion and deletion

* Finding positions of elements

* Iteration and printing

* Length

* Swapping and Copying

* Passing to functions

* Permutations

Strings
=======

Declaration
-----------

string arr;

Initialization
--------------

getline(cin, arr);

Insertion
---------

arr.push_back('s');

arr.insert(pos, char/string);

Deletion
--------

arr.pop_back();         // removes the last element

remove() finds all occurrences of a specific character in the string. Pass it on erase() method

arr.erase(remove(arr.begin(), arr.end(), 'A'), arr.end());

Finding positions of elements
-----------------------------

arr.find('A');

Iteration and Printing
----------------------

std::string::iterator it;               // forward iterator

for (it = arr.begin(); it != arr.end(); ++it) {
        do your stuff here;
}

std::string::reverse_iterator rit;      // reverse iterator

for (rit = arr.rbegin(); rit != arr.rend(); ++rit) {
        do your stuff here;
}

Length
------

arr.length();           // no. of characters in the string

arr.capacity();         // capacity of the string, >= arr.length

arr.resize(num);        // changes size of the string

arr.shrink_to_fit();    // minimizes capacity of the string

Swapping and Copying
--------------------

arr.copy(target_string/char_array, length to be copied, starting point in destination);

arr.swap(arr2);         // swaps both arr1 and arr2

Passing to functions
--------------------

void print(string got_it)
{
        cout << got_it << endl;
}

int main()
{
        string arr;
        getline(cin, arr);
        print(arr);
        return 0;
}

Sort
----

sort(arr.begin(), arr.end());

Permutations
------------

go figure

----------------------------------------------------------------------------------------------------------------------------

Vectors
=======

Declaration
-----------

vector<type> name;

vector<type> name(size);

Initialization
--------------

vec.assign(n, val);             // val is put into vec n times

Insertion
---------

vec.push_back(5);
vec.insert(position, element);

Deletion
--------

vec.pop_back();
vec.erase(position);

Finding positions of elements
-----------------------------

std::vector<type>::iterator itr = std::find(vec.begin(), vec.end(), element);
if (itr != vec.end()) 
        cout << std::distance(vec.begin(), itr);

Iteration and Printing
----------------------

vec.begin(), vec.cbegin()
vec.rbegin(), vec.crbegin()

vec.end(), vec.cend()
vec.rend(), vec.crend()

Length
------

vec.size() = number of elements in the vector

Swapping and Copying
--------------------

vec.swap(vec2);                 // swaps vec with vec2, sizes may differ. types must be the same

Passing to functions
--------------------

void func (vector<int> vec) {    // Pass by value

}

void func (vector<int>& vec) {  // Pass by reference

}

Sort
----

sort(vec.begin(), vec.end());

Permutations
------------

do {
        ;
} while (next_permutation(begin(list), end(list)));

Consecutive integers filled vector
----------------------------------

iota(begin(vec), end(vec), 1);

