from fastapi import FastAPI,HTTPException
from models import grades,student,course_raw


fake_db={'math':{'day':'sunday'}}
fake_enroll={1:{'math':33}}
kamo=['math']

class Services():
    def get(self,id:int):
        
        if id not in fake_enroll:
            return 'there is not student_id of this'
        return f'this student with {id} is real'
    def assign_marks(self,kamoku:str,id:int,remarks:int):
        jol=self.get(id)
        if jol:
            if id in fake_enroll:
                fake_enroll[id]={kamoku:remarks}
                return fake_enroll
        raise HTTPException(status_code=401,detail=('nah something is wrong/fake id'))
    def check_view(self,kamoku:str,id:int):
        kol=self.get(str,id)
        if kol:
            targ=fake_enroll[id]
            target=targ[kamoku]
            return f'your marks in {kamoku} is {target}'


serpico=Services()


    
        
    
        



