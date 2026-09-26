class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if (i!="+") and (i!="-") and (i!="*") and (i!="/"):
                stack.append(int(i))
            else:
                B=stack.pop()
                A=stack.pop()
                if i=="+":
                    res=A+B
                elif i=="-":
                    res=A-B
                elif i=="*":
                    res=A*B
                else:
                    res=int(A/B)
                stack.append(res)
        return stack[-1]