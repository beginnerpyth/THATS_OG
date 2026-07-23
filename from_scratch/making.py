from fastapi import FastAPI,APIRouter
from schema import create_user,update_user


da = [{'id':1,'email':'hsky779@gmail.com','name':'takahasi'}]

sap=FastAPI()
router=APIRouter(prefix=('/yup-we-are-back-again/'),tags=['allsame'])

@router.get('/')
def normal():
    return 'everyhting is fine'



@router.post('/')
def record(mak:create_user):
    data={'id':len(da)+1,'email':mak.email,'name':mak.name}
    da.append(data)
    return da

@router.put('/')
def update(jjk:update_user)
    for kk in da:
        if da['id']==jjk.id:
            da['name']==jjk.name
            da['email']==jjk.email
        return da

@router.delete('/')
def delete_record(id:int):
    if id in da:
        del id
    return 'that id which contain data deosnt exist'



