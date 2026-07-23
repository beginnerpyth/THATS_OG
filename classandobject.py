class family:
    def __init__(self,name,age,is_rich):
        self.name=name
        self.age=age
        self.is_rich=is_rich
    def use(self):
        return f'he is a guy{self.name},and age is{self.age},is he rich ? {self.is_rich}'
    def knoe(self):
        return f'he is a member of gangsta whose name is {self.name} and age is {self.age} but is he rich {self.is_rich}'

object1=family('father',58,True)
object2=family('brother',27,True)
b=object1.use()
c=object2.knoe()
print(b)
print(c)
 #inhritence 
class laudu():
    def action(self):#so you need self each and evry time inside class if you want to do specific behaviour
     return f'he is fool'
class mahalaudu(laudu):
    def aura(self):
        return f'very very low'
b=laudu()
c=mahalaudu()
print(c.action())
print(c.aura())
#multiple inheritance
class A:
    def rar(self):
        return f'he is a guy'
class B(A):
    def var(self):
        return f'he is a monk'
class C(B):
    def jar(self):
        return f'he is a saint_'
a=A()
b=B()
c=C()
print(b.rar())
print(c.rar())

#super()
class rsp():
    def __init__ (self,vote,pradesh):
        self.vote=vote#self defines each object like object1 and object2 without self it is undefined
        self.pradesh=pradesh
    
    
    def total_vote(self):
        return f'total vote is {self.vote * self.pradesh}'#why we used self.votes? cause to seperate each object
class mato(rsp):
    def __init__(self,votes):
        super().__init__(votes,votes)#super copies the whole function/condcutor and inserted 2 args 
janta1=rsp(11000,88)#cause we copied from rsp __init__ that have two args so we just gave 2 args 
janta2=mato(700)

print(janta1.total_vote())
print(janta2.total_vote())#nothing comploicated cause it is just inheritanc