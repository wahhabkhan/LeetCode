class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = '+'
        s = s.replace(" ", "")

        for i,ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
        
            #if operator or last character
            if not ch.isdigit() or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev // num))
                    else:
                        stack.append(prev // num)  
                    #equivalent to above code:   
                    #stack.append(int(prev / num))                       
                
                sign = ch
                num = 0
        
        return sum(stack)


        
