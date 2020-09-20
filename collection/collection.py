# counter, namedtuple (kinda act like struct) , OrderdDict(similar to dict),
# defaultdict(dict but have a default value to key so no key error.),
# deque(double ended queue) append, appendleft, pop, popleft, extend, extendleft
from collections import Counter, namedtuple

str = 'aaaabbbbcc'
count = Counter(str)
print(f'{count=}')
print(f'{count.most_common(2)=}')

point = namedtuple('Point', 'x,y')
pt = point(1, 2)
print(pt)
