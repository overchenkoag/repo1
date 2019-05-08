class A:
    name="C200"

    def start(self):
        print("start")
    def change(self):
        A.name="SSS"



b=A()
c=A()
b.arrrr=1

b.name="DDD"
print(b.name)
print(c.name)
b.change()
A.name="RRR"
d=A()
print(b.name)
print(d.name)
