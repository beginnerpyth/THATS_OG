import logging
#we use logging because to track the history with developer and fastapi
def ram(name:str):
    #once we set the file to track and which level of security to choose wwe
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #we need to set format in which patter we receive the data
    formate=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    #once we set the setFormatter we need to set format for terminal and file
    ter=logging.StreamHandler()
    ter.setFormatter(formate)
    #once we set for terminal we need to save in file
    file_suv=logging.FileHandler('pap.log')
    file_suv.setFormatter(formate)#in setFormatter we set the formate in which pattern we do
    #now we need to execute
    logger.addHandler(ter)#we addHandler where StreamHandler and FileHandler we can insert
    logger.addHandler(file_suv)

    return logger
