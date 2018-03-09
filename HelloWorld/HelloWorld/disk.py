from turtle import * 
2 
 
3 class Disk(object): 
4     def __init__(self, dname, xpos, ypos, dh, dw, col = "red"): 
5         self.name = dname 
6         self.x = xpos 
7         self.y = ypos 
8         self.h = dh 
9         self.w = dw 
10         self.color = col 
11 
 
12     def showdisk(self): 
13         pu() 
14         goto(self.x, self.y) 
15         pd() 
16         fillcolor(self.color) 
17         begin_fill() 
18         seth(0) 
19         fd(self.w / 2) 
20         lt(90) 
21         fd(self.h) 
22         lt(90) 
23         fd(self.w) 
24         lt(90) 
25         fd(self.h) 
26         lt(90) 
27         fd(self.w / 2) 
28         end_fill() 
29 
 
30     def newpos(self,x,y): 
31         self.x = x 
32         self.y = y 
33 
 
34     def cleardisk(self): 
35         pu() 
36         goto(self.x,self.y) 
37         pd() 
38         fillcolor("white") 
39         pencolor("white") 
40         begin_fill() 
41         seth(0) 
42         fd(self.w / 2) 
43         lt(90) 
44         fd(self.h) 
45         lt(90) 
46         fd(self.w) 
47         lt(90) 
48         fd(self.h) 
49         lt(90) 
50         fd(self.w / 2) 
51         end_fill() 
52         pencolor("black") 
53         fillcolor(self.color) 
54 
 
55     def getx(self): 
56         return self.x 
57 
 
58     def gety(self): 
59         return self.y 
60 
 
61     def getname(self): 
62         return self.name 
63 
 
64     def geth(self): 
65         return self.h 
66 
 
67     def getw(self): 
68         return self.w 
