
def recursive(n,open,close,path,combination):
    if open==close==n:
        combination.append(path)
        return
    if open>n or close>n or open<close:
        return
    recursive(n,open+1,close,path+"(",combination)
    recursive(n,open,close+1,path+")",combination)

    

def generateParenthesis(n):
    open=0
    close=0
    combination=[]
    recursive(n,open,close,"",combination)
    return combination

n=3
c=generateParenthesis(3)
print(c)  

