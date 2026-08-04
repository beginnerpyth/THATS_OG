from fastapi import FastAPI,HTTPException,APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import token_creator,token_decoder,verfier
from models import course_raw,student,grades_touroku,student_db,course_toruoku
from services import serpico
from databse import get_db
from sqlalchemy.orm import Session
router=APIRouter()
fake_db={'math':{'day':'sunday'}}

kamo=['math']

fake_database=[{'total_items':x} for x in range(1,101)]


@router.post('/login')
def login(gg:OAuth2PasswordRequestForm=Depends()):
    if gg.username=='admin' and gg.password=='admin123':
        adm=token_creator({'username':'admin'})
        return {'access_token':adm,'token_type':'bearer'}
    if gg.username=='user' and gg.password=='user123':
            user=token_creator({'username':'user'})
            return {'access_token':user,'token_type':'bearer'}
    raise HTTPException(status_code=403,detail=('you are forbidden'))

@router.post('/courses')
def course(kawari:course_raw,admin:str=Depends(verfier('admin'))):#in python non default parameter
     #must come before default parameter..
    if kawari.c_name in fake_db:
        return 'already here'
    fake_db[kawari.c_name]={'class':kawari.day}
    return f'welcome {admin} just added the {fake_db}'

#@router.post('/enroll_for_studs')
#def enroll(kamoku:str,id:int,en:student,student_only:str=Depends(verfier('user'))):
     
 #    if id not in fake_enroll:
 #         return'there is no student with this id'
 #    if kamoku in kamo:
 #         return 'already here'
 #    fake_enroll[id]={'sub':en.subject}
     
@router.post('/grades')
def add_grade(kamoku:str,id:int,remarks:int,only_admin:str=Depends(verfier('admin'))):
      return serpico.assign_marks(kamoku,id,remarks)
     
     

@router.get('/all_class')#we have to include slash at first
def all_course():
     return fake_db
#so the data we inserted in fake_db only saved when it is online


@router.post('/pagination')
def post_studs(search:str,secret_key:int,page:int=1,size:int=10,db:Session=Depends(get_db)):
     #pagination
     skip=(page-1)*size
     paginated_data=fake_database[skip:skip+size]
     if secret_key==1:
          return paginated_data
     show_user=db.query(course_toruoku)
     specific_show_user=show_user.filter(course_toruoku.c_name.contains(search))
     specific_show_user_count=specific_show_user.count()
     specific_show_user_offset=specific_show_user.offset(skip).limit(size).all()

     return{'search':search,
            'secret_key':secret_key,
              'skip':skip,
              'page':page,
              'size':size,
              'data':specific_show_user_offset}




     




     
     

     
     
     
     



     




     
     
