from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from preinsulated_steel import SteelPipe
from preinsulated_steel_images import Images
import base64


def add_pipe():
    global aa, pipe_list, selected_pipes
    if len(pipe_list) <= 3:
        pipe_list.append([float(variable_1.get()), float(variable_4.get()), variable_2.get(), variable_3.get()])
        pipe = float(variable_1.get())
        selected_pipes.append(pipe)
        selected_pipes.sort()
        for i,j in enumerate(pipe_list):
            Label(root,text=j[0]).grid(row=5+i,column=4)
            Label(root,text=j[1]).grid(row=5+i,column=5)
            Label(root,text=j[2]).grid(row=5+i,column=6)
            Label(root,text=j[3]).grid(row=5+i,column=7)
        selected_pipe = min(selected_pipes)
        for key, value in Lmax.items():
            if key == selected_pipe:
                if variable_3.get() == 'St 37.0':
                    Lmax_1 = value['St37.0_Lmax']
                else:
                    Lmax_1 = value['R35_Lmax']
        aa.set(Lmax_1)
        scale_calculate()
    else:
        pass


def reset():
    pipe_list.clear()
    selected_pipes.clear()
    variable_1.set(OPTIONS_1[5])
    variable_2.set(OPTIONS_2[0])
    variable_3.set(OPTIONS_3[0])
    variable_4.set(OPTIONS_4[6])
    variable_5.set(OPTIONS_5[1])
    slider_1 = Scale(root, from_=0, to=200, label='Arm 1 Length (L\u2081)', tickinterval=25, length=400, orient=HORIZONTAL)
    slider_1.grid(row=3, column=0, columnspan=5, sticky='we')
    slider_2 = Scale(root, from_=0, to=200, label='Arm 2 Length (L\u2082)', tickinterval=25, length=400, orient=HORIZONTAL)
    slider_2.grid(row=3, column= 6, columnspan=10, sticky='we')
    # labels = []
    for i in range(5,9):
        for j in range(4,11):
            lable_1 = Label(root,text=' - ').grid(row=i,column=j)
            assert label_1.forget
            print('destroyed')
    # for label in labels:
    #     label.destroy()
            
    # lable_a = Label(root,text= '                       ').grid(row=9, column=6)
    # lable_a.destroy
    # lable_b = Label(root,text= '                                 ').grid(row=10, column=9)
    # lable_b.destroy
    # lable_c = Label(root,text= '                                 ').grid(row=11, column=9)
    # lable_c.destroy 
    # Label(root,text= '    N/A    ').grid(row=10, column=9, sticky='we')
    # Label(root,text= '    N/A    ').grid(row=11, column=9, sticky= 'we')


def callback(*args):
    global aa_new
    aa_new = aa.get()


def scale_calculate():
    global slider_1, slider_2
    aa_new = aa.get()
    slider_1 = Scale(root, from_=0, to=aa_new, label='Arm 1 Length (L\u2081)', tickinterval=int(aa_new/5), length=400, orient=HORIZONTAL)
    slider_1.grid(row=3, column=0, columnspan=5, sticky='we')
    slider_2 = Scale(root, from_=0, to=aa_new, label='Arm 2 Length (L\u2082)', tickinterval=int(aa_new/5), length=400, orient=HORIZONTAL)
    slider_2.grid(row=3, column= 6, columnspan=10, sticky='we')


def scale_update(*args):
    global slider_1, slider_2
    v1 = float(variable_5.get())
    aa_new = aa.get()/v1
    slider_1 = Scale(root, from_=0, to=aa_new, label='Arm 1 Length (L\u2081)', tickinterval=int(aa_new/5), length=400, orient=HORIZONTAL)
    slider_1.grid(row=3, column=0, columnspan=5, sticky='we')
    slider_2 = Scale(root, from_=0, to=aa_new, label='Arm 2 Length (L\u2082)', tickinterval=int(aa_new/5), length=400, orient=HORIZONTAL)
    slider_2.grid(row=3, column=6, columnspan=10, sticky='we')
#    print('scale update sucess')


def calculate_z():
    L2 = []
    sg_1 = slider_1.get()
    sg_2 = slider_2.get()
    for i, j in enumerate(pipe_list):
        pipe_i = SteelPipe(carrier_dia=pipe_list[i][0], segment1_length=sg_1, segment2_length=sg_2, service_temp=pipe_list[i][1], buried_depth=float(variable_5.get()), insulation=pipe_list[i][2], steel_marking=pipe_list[i][3])
        lables = pipe_i.z_shape()
        Label(root, text=lables[1]).grid(row=5+i, column=8)
        Label(root, text=lables[2]).grid(row=5+i, column=9)
        Label(root, text=str(lables[0])+' '+'(Z shape)').grid(row=5+i, column=10)
        Label(root, text='  '+variable_5.get()).grid(row=9, column=6, sticky='w')
        if pipe_list[i][2] == 'Standard':
            L2.append(pipe_i.data()['Dzp_standard_insulaion'])
        elif pipe_list[i][2] == 'Plus':
            L2.append(pipe_i.data()['Dzp_insulation_plus'])
    trench_width = round((((sum(L2)*2)+(((len(L2)*2)+1)*200))/1000), 2)
    height = round(((float(variable_5.get())+0.1+(max(L2)/1000))), 2)
    Label(root, text=' Required area for Expansion Loop (m) - ').grid(row=11, column=5, columnspan=4, sticky='e')
    Label(root, text='                                     ').grid(row=11, column=9)
    Label(root, text='            N/A            ').grid(row=11, column=9)
    Label(root, text=str(trench_width)+' (W)'+' X '+str(height)+' (H)').grid(row=10, column=9, sticky='w')


def calculate_u():
    L2 = []
    arm_length = []
    sg_1 = slider_1.get()
    sg_2 = slider_2.get()
    for i, j in enumerate(pipe_list):
        pipe_i = SteelPipe(carrier_dia=pipe_list[i][0], segment1_length=sg_1, segment2_length=sg_2, service_temp=pipe_list[i][1], buried_depth=float(variable_5.get()), insulation=pipe_list[i][2], steel_marking=pipe_list[i][3])
        lables = pipe_i.u_shape()
        arm_length.append(lables[0])
        Label(root, text='              ').grid(row=5+i, column=8)
        Label(root, text='              ').grid(row=5+i, column=9)
        Label(root, text=lables[1]).grid(row=5+i, column=8)
        Label(root, text=lables[2]).grid(row=5+i, column=9)
        Label(root, text=str(lables[0])+' '+'(U shape)').grid(row=5+i, column=10)
        Label(root, text='  '+variable_5.get()).grid(row=9, column=6, sticky='w')
        if pipe_list[i][2] == 'Standard':
            L2.append(pipe_i.data()['Dzp_standard_insulaion'])
        elif pipe_list[i][2] == 'Plus':
            L2.append(pipe_i.data()['Dzp_insulation_plus'])
    trench_width = round((((sum(L2)*2)+(((len(L2)*2)-1)*200))/1000), 2)
    arm_length = round(max(arm_length), 2)
    width = round((trench_width + arm_length), 2)
    height = round(((float(variable_5.get())+0.1+(max(L2)/1000))), 2)
    Label(root,text= str(trench_width)+' (W)'+' X '+str(height)+' (H)').grid(row=10, column=9, sticky='w')
    Label(root,text= str(width)+' (W)'+' X '+str(width)+' (L)').grid(row=11,column=9, sticky='w')


def about():
    import webbrowser
    window = Toplevel(root)
    window.title("About District Heating System Calculator")
    label_1 = Label(window, text=' District Heating System Calculator is a simple tool to calculate the area\nrequired for buried district heating pipes expansion loops ', justify='center', pady=10, font=("Helvetica", 10))
    label_1.pack()
    label_2 = Label(window, text=' Caucluations are based on the CPV Preinsulated Steel Pipes Design Manual ', justify='center', pady=10, font=("Helvetica", 10))
    label_2.pack()
    window.grab_set()

root = Tk()
root.title("District Heating System Calculator")

'''GUI Images'''
image = Images()
Z_shape = image.z_shape
U_shape = image.u_shape
photo_1 = base64.b64decode(Z_shape)
photo_1 = PhotoImage(data=photo_1)
photo_2 = base64.b64decode(U_shape)
photo_2 = PhotoImage(data=photo_2)

OPTIONS_1 = [20,25,32,40,50,65,80,100,125,150,200,250,300,350,400,450,500,600]
OPTIONS_2 = ['Standard','Plus']
OPTIONS_3 = ['St 37.0','R-35']
OPTIONS_4 = [150,140,130,120,110,105,100,95,90,85,80,75,70,65,60,55]
OPTIONS_5 = [0.5,1.0,1.5,2.0,2.5,3.0]
Lmax = {20:{'St37.0_Lmax':22,'R35_Lmax':24},25:{'St37.0_Lmax':28,'R35_Lmax':31},32:{'St37.0_Lmax':29,'R35_Lmax':32},40:{'St37.0_Lmax':34,'R35_Lmax':38},50:{'St37.0_Lmax':42,'R35_Lmax':46},65:{'St37.0_Lmax':49,'R35_Lmax':53},80:{'St37.0_Lmax':55,'R35_Lmax':61},100:{'St37.0_Lmax':65,'R35_Lmax':71},125:{'St37.0_Lmax':72,'R35_Lmax':79},150:{'St37.0_Lmax':88,'R35_Lmax':97},200:{'St37.0_Lmax':104,'R35_Lmax':140},250:{'St37.0_Lmax':115,'R35_Lmax':156},300:{'St37.0_Lmax':137,'R35_Lmax':168},350:{'St37.0_Lmax':138,'R35_Lmax':187},400:{'St37.0_Lmax':158,'R35_Lmax':211},450:{'St37.0_Lmax':161,'R35_Lmax':239},500:{'St37.0_Lmax':162,'R35_Lmax':260},600:{'St37.0_Lmax':197,'R35_Lmax':None}}

variable_1 = StringVar(root)
variable_1.set(OPTIONS_1[5])
variable_2 = StringVar(root)
variable_2.set(OPTIONS_2[0])
variable_3 = StringVar(root)
variable_3.set(OPTIONS_3[0])
variable_4 = StringVar(root)
variable_4.set(OPTIONS_4[6])
variable_5 = StringVar(root)
variable_5.set(OPTIONS_5[1])

label_1 = Label(root, text='Pipe Size(mm)')
label_2 = Label(root, text = 'Service Temperature(\u00b0C)')
label_3 = Label(root, text = 'Buried Depth (m)')
label_4 = Label(root, text = 'Insulation Type')
label_5 = Label(root, text = 'Steel Marking')
label_11 = Label(root, text='Pipe Size', relief=FLAT)
label_21 = Label(root, text = 'Service Temperature', relief=FLAT)
label_41 = Label(root, text = 'Insulation Type', relief=FLAT)
label_51 = Label(root, text = 'Steel Marking', relief=FLAT)
label_61 = Label(root, text = 'C-Arm length (m)', relief=FLAT)
label_71 = Label(root, text = '\u0394L\u2081 (mm)', relief=FLAT)
label_81 = Label(root, text = '          \u0394L\u2082 (mm)          ', relief=FLAT)
w_1 = OptionMenu(root, variable_1, *OPTIONS_1)
w_2 = OptionMenu(root, variable_2, *OPTIONS_2)
w_3 = OptionMenu(root, variable_3, *OPTIONS_3)
w_4 = OptionMenu(root, variable_4, *OPTIONS_4)
w_5 = OptionMenu(root, variable_5, *OPTIONS_5, command=scale_update)

label_1.grid(row=0,column=1, sticky='we')
label_2.grid(row=0,column=3, sticky='we')
label_3.grid(row=1,column=1, sticky='we')
label_4.grid(row=0,column=5, sticky='we')
label_5.grid(row=0,column=7, sticky='we')
label_11.grid(row=4,column=4, sticky='we')
label_21.grid(row=4,column=5, sticky='we')
label_41.grid(row=4,column=6, sticky='we')
label_51.grid(row=4,column=7, sticky='we')
label_71.grid(row=4,column=8, sticky='e')
label_81.grid(row=4,column=9, sticky='we')
label_61.grid(row=4,column=10, sticky='we')
Label(root, text = 'Buried Depth (m) - ', relief=FLAT).grid(row=9,column=5, columnspan=2, sticky='w')
Label(root,text=' Required Trench Dimensions (m) - ').grid(row=10,column=5, columnspan = 4, sticky='e')
Label(root,text=' Required area for Expansion Loop (m) - ').grid(row=11,column=5, columnspan = 4, sticky='e')

w_1.grid(row=0,column=2, sticky='we')
w_2.grid(row=0,column=6, sticky='we')
w_3.grid(row=0,column=8, sticky='we')
w_4.grid(row=0,column=4, sticky='we')
w_5.grid(row=1,column=2, sticky='we')

ttk.Separator(root).place(x=0, y=30, relwidth=1)
ttk.Separator(root).place(x=0, y=60, relwidth=1)
ttk.Separator(root).place(x=0, y=140, relwidth=2)
ttk.Separator(root,orient=VERTICAL).grid(row=3, column=4)

'''Menu Bar'''
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Reset", command=reset)
filemenu.add_command(label="Exit", command=root.destroy)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
root.config(menu=menubar, )


'''Main Window'''
pipe_list = []
selected_pipes = []
aa = IntVar()
aa.set(0)
aa_new = 200

button_1 = Button(root, text = 'Add Pipe (F+R)', command=add_pipe)
button_1.grid(row=0, sticky='we')
button_1.flash()

button_2 = Button(root, text = 'Reset', bd = 3, command=reset)
button_2.grid(row=0, column=10, sticky='we')

button_3 = Button(root, text = 'Calculate U', image=photo_1, command=calculate_z, borderwidth=3)
button_3.grid(row=4, column = 0, rowspan=6, columnspan = 2, sticky='we')

button_4 = Button(root, text = 'Calculate Z', image=photo_2, command=calculate_u, borderwidth=3)
button_4.grid(row=4, column = 2, rowspan=6, columnspan = 2, sticky='we')

button_4 = Button(root, text = 'Exit', command=root.destroy, borderwidth=3)
button_4.grid(row=1, column = 10, sticky='we')

slider_1 = Scale(root, from_=0, to=aa_new, label='Arm 1 Length (L\u2081)', tickinterval=25, length=400, orient=HORIZONTAL)
slider_1.grid(row=3, column=0, columnspan=5, sticky='we')
slider_2 = Scale(root, from_=0, to=aa_new, label='Arm 2 Length (L\u2082)', tickinterval=25, length=400, orient=HORIZONTAL)
slider_2.grid(row=3, column= 6, columnspan=10, sticky='we')


aa.trace('w', callback)

root.mainloop()