print("operators in python:-")
print("Arithmetic operator:")
a=20;
b=30;
Sum=a+b;
Sub=a-b;
Mul=a*b;
Div=a/b;
Module=a%b;

print("SUM",a,"+",b,"=",Sum)
print("SUB",a,"-",b,"=",Sub)
print("MUL",a,"*",b,"=",Mul)
print("DIV",a,"/",b,"=",Div)
print("MODULE",a,"%",b,"=",Module)

print("Relational operator:")
a=100;
b=200;
c=a>b;
d=b<a;
e=(a==b);
f=a!=b;
g=a<=b;
h=a>=b;

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

print("Assignment operator:")
a=10;
b=20;
print("A=",a)
a += 10;
print("A=",a)
a-=10;
print("A=",a)
a*=2;
print("A=",a)
a/=1;
print("A=",a)
a%=2;
print("A=",a)

print("Logical operator:")
a=100;
b=200;
if(a and b==100):
    print("A AND B Both 100")
if(a or b==100):
    print("(A AND B) ANY 100")
if(not a==b):
    print("NOT EQUAL")

print("Bit wise operator")
a = 5       # Binary: 0101
b = 3       # Binary: 0011

print(a & b)    # Output: 1  (0001)
print(a | b)    # Output: 7  (0111)
print(a ^ b)    # Output: 6  (0110)
print(~a)       # Output: -6 (inverts bits and adds -1 in 2's complement)
print(a << 1)   # Output: 10 (1010)
print(a >> 1)   # Output: 2  (0010)

print("Ternary operator")
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status) 
