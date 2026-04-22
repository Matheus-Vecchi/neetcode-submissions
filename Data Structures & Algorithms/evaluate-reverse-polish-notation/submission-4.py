class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        aux = []

        for pos, i in enumerate(tokens):
            if i == "+":
                temp = aux[-1] + aux[-2]
                aux.pop()
                aux.pop()
                aux.append(temp)
            elif i == "-":
                temp = aux[-2] - aux[-1]
                aux.pop()
                aux.pop()
                aux.append(temp)
            elif i == "*":
                temp = aux[-2] * aux[-1]
                aux.pop()
                aux.pop()
                aux.append(temp)
            elif i == "/":
                temp = int(aux[-2] / aux[-1])
                aux.pop()
                aux.pop()
                aux.append(temp)
            else:
                aux.append(int(i))

        return aux[0]
        