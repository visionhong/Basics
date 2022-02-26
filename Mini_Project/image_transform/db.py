import pandas as pd
from sqlalchemy import create_engine
from PIL import Image
import base64
from io import BytesIO
from tkinter import messagebox

def judge(filename,engine): # 파일명 중복 판단
    img_df = pd.read_sql(sql='select*from images', con=engine)  # sql문의 실행문을 데이터 프레임으로 받아옴
    if (img_df['filename'] == filename).any():
        messagebox.showinfo(title='error', message='이미 존재하는 파일명입니다.')
        return False
    return True

def saveDB(filename,img,target):
    engine = create_engine('mysql+pymysql://testuser:testpw@localhost/testdb', echo=False)

    if judge(filename,engine) == False:
        return
    buffer = BytesIO()
    # im = Image.open('transformed_images/'+filename)

    img.save(buffer, format='jpeg')
    img_str = base64.b64encode(buffer.getvalue())
    # print(img_str) # 변환된 데이터

    img_df = pd.DataFrame({'image_data':[img_str],'filename':[filename],'label':[target]})
    # print(img_df)
    img_df.to_sql('images',con=engine,if_exists='append',index=False)

def loadDB(filename):
    print(filename)
    engine = create_engine('mysql+pymysql://testuser:testpw@localhost/testdb', echo=False)
    img_df = pd.read_sql(sql='select*from images',con=engine)
    # print(img_df[img_df['filename'].isin([filename])])
    try:
        pick = img_df[img_df['filename'].isin([filename])]['image_data'].values[0]
    except Exception as e:
        return False
    img = base64.decodestring(pick)
    im = Image.open(BytesIO(img))
    #im.show()
    return im

def count():
    engine = create_engine('mysql+pymysql://testuser:testpw@localhost/testdb', echo=False)
    img_df = pd.read_sql(sql='select*from images', con=engine)

    all = img_df.shape[0]
    bird = img_df[img_df['label'] == '앵무새'].shape[0]
    cat = img_df[img_df['label'] == '고양이'].shape[0]
    dog = img_df[img_df['label'] == '개'].shape[0]
    deer = img_df[img_df['label'] == '사슴'].shape[0]
    fox = img_df[img_df['label'] == '여우'].shape[0]
    hedgehog = img_df[img_df['label'] == '고슴도치'].shape[0]
    raccoon = img_df[img_df['label'] == '라쿤'].shape[0]
    return [all,bird,cat,dog,deer,fox,hedgehog,raccoon]


# loadDB()