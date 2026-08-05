from fastapi import FastAPI,HTTPException,APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import token_decoder,token_creator,token_verifier
from models import register_class
from uploadfile import upload_file
from fastapi import FastAPI,HTTPException,UploadFile,File,Depends


router=APIRouter()


fake_database={1:{'day':'sunday','course_name':'math'}}
@router.post('/login')
def login(form_layout:OAuth2PasswordRequestForm=Depends()):
    if form_layout.username=='teacher' and form_layout.password=='teacher123':
        token_created_teacher=token_creator({'email':'teacher@universal.com','name':'uni_teacher','role':'teacher'})
        return {'access_token':token_created_teacher,'token_type':'bearer'}
    if form_layout.username=='student' and form_layout.password=='student123':
            token_created_student=token_creator({'email':'student@universal.com','name':'uni_student','role':'student'})
            return {'access_token':token_created_student,'token_type':'bearer'}
    
    raise HTTPException('there is something wrong with credentials')


@router.get('/only_for_students')
def students(student:str=Depends(token_verifier('student'))):
    return f'only {student} can access this'

@router.get('/only_for_teachers')
def teacher(teacher:str=Depends(token_verifier('teacher'))):
    return f'only {teacher} can access this'

@router.post('/register_the_course')
def course_register(id:int,class_schedule:register_class,teacher:str=Depends(token_verifier('teacher'))):
    for x in fake_database:
        if x == class_schedule.course_id:
            return 'its already saved'
        fake_database[class_schedule.course_id]={'day':class_schedule.day,'course_name':class_schedule.course_name}
        return {'data saved':fake_database[id]}



    







