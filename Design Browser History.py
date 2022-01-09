'''You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]'''



class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage=homepage
        self.list1=[self.homepage]
        self.count=0
    def visit(self, url: str) -> None:
        if url not in self.list1:
            self.list1=self.list1[:self.count+1]
            self.list1.append(url)
            self.count+=1
            
    def back(self, steps: int) -> str:
        self.count=self.count-steps
        if self.count<0:
            self.count=0
            return self.list1[self.count]
        else:
            return self.list1[self.count]

    def forward(self, steps: int) -> str:
        self.count+=steps
        if self.count>=len(self.list1)-1:
            self.count=len(self.list1)-1
            return self.list1[-1]
        else:
            return self.list1[self.count]
