from PIL import Image  ### 画像処理ライブラリPillow をインポート
man_count = 0
woman_count = 0

with open("list_attr_celeba.txt","r") as f:    ### 属性ファイルを開く
   for i in range(202599):   ### 全部で202,599枚処理する
         line = f.readline()   ### 1行データ読み込み
         line = line.split()  ### データを分割

         if  line[21]=="1" and line[9] == "1":  
            if man_count <= 400:
               image = Image.open("C:/Users/asd-0/Downloads/dataset/images/img_align_celeba/"+line[0])
               image.save("./train_man/"+line[0]) # 「0」フォルダーに保存
               man_count += 1
            else:
               image = Image.open("C:/Users/asd-0/Downloads/dataset/images/img_align_celeba/"+line[0])
               image.save("./test_man/"+line[0]) # 「0」フォルダーに保存
               man_count += 1
            
         
         elif line[21] == "-1" and line[9] == "1":
            if woman_count <= 400:
               image = Image.open("C:/Users/asd-0/Downloads/dataset/images/img_align_celeba/"+line[0])
               image.save("./train_woman/"+line[0]) # 「0」フォルダーに保存
               woman_count += 1
            else:
               image = Image.open("C:/Users/asd-0/Downloads/dataset/images/img_align_celeba/"+line[0])
               image.save("./test_woman/"+line[0]) # 「0」フォルダーに保存
               woman_count += 1
               
         if (man_count > 500 and woman_count > 500):
            break