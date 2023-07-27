class GUI:
    def __init__(self, master):
        self.master = master
        self.x = 0
        self.TheMainGUI()

    def TheMainGUI(self):
        self.master.geometry('800x150')
        self.master.title('Gary Analytica')
        #===========================================================================================================================================================
        self.frame_label = Frame(self.master)
        self.frame_label.pack()
        Label(self.frame_label, text='Welcome To Gary', font=('Times', 30)).grid(row=0, column=2)
        #===========================================================================================================================================================
        self.frame_menu = Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(padding=(50, 15))
        #===========================================================================================================================================================        #---------------------------------------------------------------------------------------------------------------------------
        self.style = Style()
        self.style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='4')
        self.style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])
        #===========================================================================================================================================================
        self.buttons = Frame(self.master)
        self.buttons.pack()
        #===========================================================================================================================================================
        Button(self.buttons, text="Face Restoration", command=self.ptn1).grid(row=0, column=0, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text="Full Analysis", command=self.ptn2).grid(row=0, column=1, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text="3D Modeling", command=self.ptn3).grid(row=0, column=2, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text="Cancel", command=self.ptn4).grid(row=0, column=3, columnspan=1, padx=5, pady=5)
    #===========================================================================================================================================================
    def ptn1(self):
        self.x = 1
        self.master.quit()
    def ptn2(self):
        self.x = 2
        self.master.quit()
    def ptn3(self):
        self.x = 3
        self.master.quit()
    def ptn4(self):
        self.master.quit()
    def run(self):
        return self.x

#===========================================================================================================================================================        

class OutputGUI:
    def __init__(self, master, gender, age, glasses, mask):
        self.master = master
        self.gender = gender
        self.mask = mask
        self.age = age
        self.glasses = glasses

        self.TheMainGUI()

    def TheMainGUI(self):
        self.master.geometry('800x150')
        self.master.title('Gary Analytica')
        #===========================================================================================================================================================
        self.frame_label = Frame(self.master)
        self.frame_label.pack()
        Label(self.frame_label, text='Full Analysis Results', font=('Times', 30)).grid(row=0, column=2)
        #===========================================================================================================================================================
        self.frame_menu = Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(padding=(50, 15))
        #===========================================================================================================================================================        #---------------------------------------------------------------------------------------------------------------------------
        self.style = Style()
        self.style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='4')
        self.style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])
        #===========================================================================================================================================================
        self.buttons = Frame(self.master)
        self.buttons.pack()
        #===========================================================================================================================================================
        Button(self.buttons, text=self.gender, command=self.action).grid(row=0, column=0, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text=self.age, command=self.action).grid(row=0, column=1, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text=self.glasses, command=self.action).grid(row=0, column=2, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text=self.mask, command=self.action).grid(row=0, column=3, columnspan=1, padx=5, pady=5)
    #===========================================================================================================================================================
    def action(self):
        pass
    def ptn4(self):
        self.master.quit()
    def run(self):
        pass
#===========================================================================================================================================================        



class Click:
    def __init__(self, yolo_path, output_path, video_path, mapping):
        self.yolo_path = yolo_path
        self.output_path = output_path
        self.video_path = video_path
        self.flag = False
        self.i = 0
        self.frame = None
        self.coo = []
        self.mapping = mapping
        self.object_counter = 0
        self.clicked_counter = 0

    def mouseHandler(self, event, x, y, flags, params):

        if event == cv2.EVENT_LBUTTONDOWN:
            # print(x, y)
            self.i += 1
            # print(i)
            # os.chdir(r"C:\Users\Amr\Desktop\Graduration Project\attributes_script\My_script\yolov7-main")
            cv2.imwrite(self.output_path + "\Clicked_frames\pic" + str(self.i) + ".jpg", self.frame)
            subprocess.run([os.path.join(config.main_dir, 'Python/python.exe'), self.yolo_path + '\detect.py', '--weights',
                            self.yolo_path + "\yolov7-tiny.pt",
                            '--source',
                            self.output_path + "\Clicked_frames\pic"
                            + str(self.i) + ".jpg",
                            '--save-txt', '--project', self.output_path + '/detect'])
            if self.i == 1:
                os.chdir(self.output_path + "\detect\exp\labels")
            else:
                os.chdir(self.output_path + "\detect\exp" + str(self.i) + "\labels")
            self.coo.append((x, y))
            read_file = pd.read_csv("pic" + str(self.i) + ".txt", header=None, sep=" ")
            read_file = read_file.rename(columns={0: 'Class', 1: 'X_Norm', 2: 'Y_Norm', 3: 'Width', 4: 'Height'})
            self.flag = True
            read_file['X_Norm'] = (read_file['X_Norm'] * self.frame.shape[1]).astype('int32')
            read_file['Y_Norm'] = (read_file['Y_Norm'] * self.frame.shape[0]).astype('int32')
            read_file['Width'] = read_file['Width'] * self.frame.shape[1]
            read_file['Height'] = read_file['Height'] * self.frame.shape[0]
            read_file["x_min"] = (read_file['X_Norm'] - read_file['Width'] / 2).astype('int32')
            read_file["y_min"] = (read_file['Y_Norm'] - read_file['Height'] / 2).astype('int32')
            read_file["x_max"] = (read_file['X_Norm'] + read_file['Width'] / 2).astype('int32')
            read_file["y_max"] = (read_file['Y_Norm'] + read_file['Height'] / 2).astype('int32')

            new_pd = read_file[['Class', 'X_Norm', 'Y_Norm', "x_min", "y_min", "x_max", "y_max"]]
            new_pd = new_pd.loc[
                (new_pd["x_min"] < x) & (new_pd["y_min"] < y) & (new_pd['x_max'] > x) & (new_pd['y_max'] > y)]
            new_pd['distance'] = (new_pd['X_Norm'] - x) ** 2 + (new_pd['Y_Norm'] - y) ** 2
            print(new_pd)

            new_pd = new_pd[new_pd['distance'] == new_pd['distance'].min()]
            img = self.frame[new_pd.iloc[0]['y_min']:new_pd.iloc[0]['y_max'],
                  new_pd.iloc[0]['x_min']:new_pd.iloc[0]['x_max']]
            #ig = Super_Resoultion(img).run()
            now_dir = os.getcwd()
            os.chdir(self.output_path + "\Clicked_objects")
            cv2.imwrite('object_' + str(self.object_counter) + '.jpg', img)
            self.object_counter += 1
            # cv2.imshow('im', ig)
            cv2.imshow('im', img)
            # print(os.getcwd())
            #---------------------------------------------------------------
            mainWindow = Tk()
            user_gui = GUI(mainWindow)
            mainWindow.mainloop()
            user_choice = user_gui.run()
            mainWindow.destroy()
            #---------------------------------------------------------------
            if user_choice == 1:
                os.chdir(config.main_dir)
                img_path = self.output_path + '\Clicked_objects' + '\object_' + str(self.object_counter-1) + '.jpg'
                subprocess.run([os.path.join(config.main_dir, 'Python/python.exe'), os.path.join(config.main_dir, 'GFPGAN-master\\inference_gfpgan.py') , '-i',
                            img_path, '-o', self.output_path])
            elif user_choice == 2:
                if new_pd.iloc[0][0] == 0:
                    lst = []
                    # print(os.getcwd())
                    # now_dir = os.getcwd()
                    # print(os.getcwd())
                    os.chdir(self.output_path + "\Full_Analysis_outputs")
                    cv2.imwrite('clicked_' + str(self.clicked_counter) + '.jpg', img)
                    f = open('clicked_' + str(self.clicked_counter) + '.txt', "w+")
                    self.clicked_counter += 1
                    im = cv2.resize(img, (256, 256))
                    im = im.reshape(1, 256, 256, 3)
                    model_mask = load_model(c.mask_path)
                    #model_cap = c.binary_hat_path
                    model_gender = load_model(c.gender_path)
                    model_glasses = load_model(c.glasses_path)
                    model_age = load_model(c.avg_age_path)
                    mask_no_mask = model_mask.predict(im)
                
                    f.write(self.mapping['mask'][np.argmax(mask_no_mask)] + '\n')
                    gender = model_gender.predict(im)
                    f.write(self.mapping['gender'][np.argmax(gender)] + '\n')
                    #hat = model_cap.predict(im)
                    #f.write(self.mapping['hat'][np.argmax(hat)] + '\n')
                    glasses = model_glasses.predict(im)
                    f.write(self.mapping['Glasses'][np.argmax(glasses)] + '\n')
                    age = model_age.predict(im)
                    f.write(self.mapping['avg_age'][np.argmax(age)] + '\n')
                    # print(os.getcwd())
                    # lst.append()
                    # for i in range(10):
                    #     f.write("This is line %d\r\n" % (i + 1))
                    f.close()
                    # print(f'{mask_no_mask}  +  {gender}  +  {cap}  +  {glasses}')
                    # mask_or_no = model_mask(im)
                    # gender = model_gender(im)
                    # print('in Persons model')
                    # print(self.mapping['mask'][np.argmax(mask_no_mask)])
                    master_ui = Tk()
                    user_gui = OutputGUI(master_ui, self.mapping['gender'][np.argmax(gender)], self.mapping['avg_age'][np.argmax(age)], self.mapping['Glasses'][np.argmax(glasses)], self.mapping['mask'][np.argmax(mask_no_mask)])
                    master_ui.mainloop()
                    master_ui.destroy()
                elif new_pd.iloc[0][0] == 2:
                    now_dir = os.getcwd()
                    os.chdir(self.output_path + "\Full_Analysis_outputs")
                    cv2.imwrite('clicked_' + str(self.clicked_counter) + '.jpg', img)
                    im = cv2.resize(img, (256, 256))
                    im = im.reshape(1, 256, 256, 3)
                    f = open('clicked_' + str(self.clicked_counter) + '.txt', "w+")
                    # ---------------------------------------
                    # mask_no_mask = model_mask.predict(im)
                    # f.write(self.mapping['mask'][np.argmax(mask_no_mask)] + '\n')
                    # gender = model_gender.predict(im)
                    # f.write(self.mapping['gender'][np.argmax(gender)] + '\n')
                    # hat = model_cap.predict(im)
                    # f.write(self.mapping['hat'][np.argmax(hat)] + '\n')
                    # glasses = model_glasses.predict(im)
                    # f.write(self.mapping['glasses'][np.argmax(glasses)] + '\n')
                    # ----------------------------------------
                    # print(os.getcwd())
                    # lst.append()
                    # for i in range(10):
                    #     f.write("This is line %d\r\n" % (i + 1))
                    f.close()
                    # car_type = model_car_type(im)
                    # car_plate = model_car_plate(im)
                    print('in Cars model')
                    self.clicked_counter += 1
            elif user_choice == 3:
                os.chdir(config.main_dir)
                img_path = self.output_path + '\Clicked_objects' + '\object_' + str(self.object_counter-1) + '.jpg'
                subprocess.run([os.path.join(config.main_dir, 'Python/python.exe'), os.path.join(config.main_dir, 'pifuhd\\run_pifuhd.py') , '--image_path',
                            img_path])
            #--------------------------------------------------------------


    def run(self):
        font = cv2.FONT_HERSHEY_SIMPLEX
        shutil.rmtree(self.output_path, ignore_errors=True)
        os.mkdir(self.output_path)
        os.mkdir(self.output_path + "\Clicked_frames")
        os.mkdir(self.output_path + "\detect")
        os.mkdir(self.output_path + "\Clicked_objects")
        os.mkdir(self.output_path + "\Face_Restoration_outputs")
        os.mkdir(self.output_path + "\Full_Analysis_outputs")
        os.mkdir(self.output_path + "/3D_modeling_outputs")
        cap = cv2.VideoCapture(self.video_path)
        # fps = cap.get(cv2.CAP_PROP_FPS)

        while cap.isOpened():
            # Capture frame-by-frame
            cv2.namedWindow('Video')
            cv2.setMouseCallback('Video', self.mouseHandler)
            _, self.frame = cap.read()
            if _:
                cv2.imshow('Video', self.frame)
                cv2.waitKey(5)
                if self.flag:
                    cv2.waitKey()
                    self.flag = False
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif cv2.waitKey(1) & 0xFF == ord(' '):
                # print('Karim')
                cv2.waitKey()
        cap.release()
        cv2.destroyAllWindows()
        # print(self.coo)



if __name__ == "__main__":

    import os
    import cv2
    import subprocess
    import shutil
    import time
    import argparse
    from CONF import config
    from Gary.garySE.cfg import config as c
    from tkinter.ttk import *
    import numpy as np
    import pandas as pd
    from keras.models import load_model
    from tkinter import Tk
    # model_gender = load_model(config.gender_path)
    # model_cap = load_model(config.hat_path)
    # model_glasses = load_model(config.glasses_path)
    # mapping = {
    #     'hat': {0: 'bonnet',  1: 'cap', 2: 'capuchon', 3: 'helmet', 4: 'hijab', 5: 'ice cap', 6: 'without_cap'},
    #     'glasses': {0: 'with_glasses',  1: 'without_glasses'},
    #     'avg_age': {0: 'old', 1: 'young', 2: 'youth'},
    #     #'mask': {0: 'with_mask',  1: 'without_mask'},
    #     'gender': {0: 'female', 1: 'male'}
    # }

    mapping = {
        'hat': {0: 'bonnet',  1: 'cap', 2: 'capuchon', 3: 'helmet', 4: 'hijab', 5: 'ice cap', 6: 'without_cap'},
        'Glasses': {0: 'With Glasses',  1: 'Without Glasses'},
        'avg_age': {0: 'Old', 1: 'Young', 2: 'Youth'},
        'mask': {0: 'With Mask',  1: 'Without Mask'},
        'gender': {0: 'Female', 1: 'Male'}
    }
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, help='Video path')
    opt = parser.parse_args()
    video_path = opt.video_path
    yolo_path = config.yolo_dir
    output_path = os.path.join(config.output_dir, "onthespotout")
    Click(yolo_path, output_path, video_path, mapping=mapping).run()
