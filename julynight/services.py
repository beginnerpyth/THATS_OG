from fastapi import FastAPI,HTTPException
fake_users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@test.com', 'role': 'admin'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@test.com', 'role': 'user'},
    {'id': 3, 'name': 'Carol', 'email': 'carol@test.com', 'role': 'user'},
]

class secondfloor():
    def get_user_by_id(self,id:int):
       # self.name=name#if we do this our app will crash...and we are dealing like webrequest which changes time to time so we dont..
        #self.id=id#so we make this self.id=id when we want it to be same for long time like database
        for x in fake_users:
            if x['id']==id:
                
                return x
        raise HTTPException(detail='there is no such data')

    def update_user(self,name:str,id:int,role:str):
        up_user=self.get_user_by_id(id)
        if up_user:
            up_user['name']=name
            
            up_user['role']=role
            return up_user
    def create_user(self,name:str,id:int,role:str,email:str):
        data=self.get_user_by_id(id)
        if data:
            raise HTTPException(detail='its already there')
        baba={'name':name,'id':id,'role':role,'email':email}
        fake_users.append(baba)








    

    

    

             

