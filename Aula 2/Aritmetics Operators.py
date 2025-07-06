'''
Operadores aritméticos
Os operadores no Python são:
+  Plus sign             Addition/Concatenation      
-  Minus sign            Subtraction
*  Asterisk              Multiplication/Repetition
/  Bar                   Division
// Double bar            Division wth whole result (sem número quebrado)
%  Percentage            Module (rest of division)
** Double Asterisk       Potentiation

Operations of the same priority are made from left to right,
parentheses change the priority.
'''''

print("soma 2 com 2:", 2+2) # 4
print("concatena 2 com 2:", '2' + '2') # 22
print("multiplica 2 com 2:", 2*2) # 4
print("repete TWICE 2 vezes:", 'TWICE'*2) #TWICETWICE
print("division 10 for 3:", 10/3) # 3.33333333333333335
print("divide 10 com 3 (valor inteiro):", 10//3) # 3
print("resto da divisão 10 com 3:", 10%3) # 1
print("2 elevado a 3:", 2**3) # 8
print("alterando a prioridade", (5+2)*10) # (5+2)=7 7*10=70
