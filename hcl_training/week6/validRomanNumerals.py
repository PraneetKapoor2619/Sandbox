regex_pattern = r"^([M]{0,3})(([C]{0,3})|(CD|CM)|(D[C]{0,3})){0,1}(([X]{0,3})|(XL|XC)|(L[X]{0,3})){0,1}(([I]{0,3})|(IV|IX)|(V[I]{0,3})){0,1}$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))