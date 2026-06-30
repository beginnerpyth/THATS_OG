import logging
def work(name:str):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)#in which level we need to set 
    #once we set track and set the security level
    formate=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    #once we set the format we need to do passs on terminal
    doh=logging.StreamHandler()
    doh.setFormatter(formate)#in which format we need to set 
    #once we set the format we need to save the file
    file_save=logging.FileHandler('mymemo.log')#it creates new log incase there isnot
    file_save.setFormatter(formate)
    #we need to make it connect to logger so evreything runs
    logger.addHandler(doh)
    logger.addHandler(file_save)

    return logger

