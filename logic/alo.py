from logicPlan import *
from logic import pl_true
import logicPlan
A=Expr('A')
B=Expr('B')
C=Expr('C')
D=Expr('D')
literals=[A,B,C,D]
conjunc = list()
conjunc1 = list()
noLiterals = len(literals)
# for i in range(0, noLiterals):
#         tempList=[x for x in literals if x != literals[i]]
#         conjunc.append(logic.conjoin(literals[i], ~disjoin(tempList)))
m=logicPlan.exactlyOne(literals)
model1 = {A:False, B:False, C:False, D:False}
model2 = {A:False, B:True, C:False, D:False}
model3 = {A:False, B:True, C:False, D:True}


ans1 = logic.pl_true(m,model1)
ans2 = logic.pl_true(m,model2)
ans3 = logic.pl_true(m,model3)

ans = [ans1, ans2, ans3]
print(ans,m)