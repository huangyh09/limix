from io import StringIO


def get_dataframe():
    import pandas

    csv = r""",value,category,variable
0,85,1 min,rest
1,85,15 min,rest
2,88,30 min,rest
3,90,1 min,rest
4,92,15 min,rest
5,93,30 min,rest
6,97,1 min,rest
7,97,15 min,rest
8,94,30 min,rest
9,80,1 min,rest
10,82,15 min,rest
11,83,30 min,rest
12,91,1 min,rest
13,92,15 min,rest
14,91,30 min,rest
15,83,1 min,rest
16,83,15 min,rest
17,84,30 min,rest
18,87,1 min,rest
19,88,15 min,rest
20,90,30 min,rest
21,92,1 min,rest
22,94,15 min,rest
23,95,30 min,rest
24,97,1 min,rest
25,99,15 min,rest
26,96,30 min,rest
27,100,1 min,rest
28,97,15 min,rest
29,100,30 min,rest
30,86,1 min,walking
31,86,15 min,walking
32,84,30 min,walking
33,93,1 min,walking
34,103,15 min,walking
35,104,30 min,walking
36,90,1 min,walking
37,92,15 min,walking
38,93,30 min,walking
39,95,1 min,walking
40,96,15 min,walking
41,100,30 min,walking
42,89,1 min,walking
43,96,15 min,walking
44,95,30 min,walking
45,84,1 min,walking
46,86,15 min,walking
47,89,30 min,walking
48,103,1 min,walking
49,109,15 min,walking
50,90,30 min,walking
51,92,1 min,walking
52,96,15 min,walking
53,101,30 min,walking
54,97,1 min,walking
55,98,15 min,walking
56,100,30 min,walking
57,102,1 min,walking
58,104,15 min,walking
59,103,30 min,walking
60,93,1 min,running
61,98,15 min,running
62,110,30 min,running
63,98,1 min,running
64,104,15 min,running
65,112,30 min,running
66,98,1 min,running
67,105,15 min,running
68,99,30 min,running
69,87,1 min,running
70,132,15 min,running
71,120,30 min,running
72,94,1 min,running
73,110,15 min,running
74,116,30 min,running
75,95,1 min,running
76,126,15 min,running
77,143,30 min,running
78,100,1 min,running
79,126,15 min,running
80,140,30 min,running
81,103,1 min,running
82,124,15 min,running
83,140,30 min,running
84,94,1 min,running
85,135,15 min,running
86,130,30 min,running
87,99,1 min,running
88,111,15 min,running
89,150,30 min,running"""

    return pandas.DataFrame.read_csv(StringIO(csv))
