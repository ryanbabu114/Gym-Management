from tkinter import *


def employee_form():
    global back_image
    member_frame=Frame(window, width=1070,height=567)
    member_frame.place(x=300, y=100)
    heading_label=Label(member_frame, text='Manage Member Details',font=('calibri',16, 'bold'),bg='#0f4d7d',fg='white')
    heading_label.place(x=0,y=0,relwidth=1)

    back_image=PhotoImage(file='left-arrow.png')
    back_button=Button(member_frame,image=back_image,bd=0,cursor='hand2',command=lambda :member_frame.place_forget())
    back_button.place(x=10,y=40)


window=Tk()

window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable (0, 0)
window.config(bg='white')
bg_image=PhotoImage(file='weightlifter1.png')
titleLabel=Label(window,image=bg_image,compound=LEFT, text="Gym  Management System",font=('arial',40,'bold'),bg='#010c48',fg='white',anchor='w',padx=20)

titleLabel.place(x=0,y=0,relwidth=1)

LogoutButton=Button(window,text='Logout',font=('corbel', 20, 'bold'),fg='#010c48')
LogoutButton.place(x=1100,y=10)
subtitleLabel=Label(window, text='Welcome Admin\t\t Date: 08-07-2024\t\t Time: 12:36:17 pm',font=('calibri', 15, 'bold'), bg='#4d636d',fg='white')
subtitleLabel.place(x=0,y=70,relwidth=1)

leftFrame=Frame (window)
leftFrame.place(x=0,y=102,width=300,height=555)

logoImage=PhotoImage(file='fitness.png')

imageLabel=Label(leftFrame, image=logoImage)
imageLabel.pack()

menuLabel=Label(leftFrame,text='Menu',font=('calibri',20),bg='#009688')
menuLabel.pack(fill=X)

memberadd_icon=PhotoImage(file='useradd.png')
memberadd_button=Button(leftFrame,image=memberadd_icon,compound=LEFT, text='Add Members',font=('calibri',20, 'bold'),anchor='w',padx=10,command=employee_form)
memberadd_button.pack(fill=X)

memberdel_icon=PhotoImage(file='user (1).png')
memberdel_button=Button(leftFrame,image=memberdel_icon,compound=LEFT, text='Remove Members',font=('calibri',20, 'bold'),anchor='w',padx=10)
memberdel_button.pack(fill=X)

addwork_icon=PhotoImage(file='add.png')
addwork_button=Button(leftFrame,image=addwork_icon,compound=LEFT, text='Workout',font=('calibri',20, 'bold'),anchor='w',padx=10)
addwork_button.pack(fill=X)

memberview_icon=PhotoImage(file='team.png')
memberview_button=Button(leftFrame,image=memberview_icon,compound=LEFT, text='Members',font=('calibri',20, 'bold'),anchor='w',padx=10)
memberview_button.pack(fill=X)

member_frame=Frame(window,bg='#2C3E50',relief=RIDGE)
member_frame.place(x=400,y=125,height=170,width=288)
total_member_icon=PhotoImage(file='diversity.png')
total_member_icon_label=Label(member_frame,image=total_member_icon,bg='#2C3E50')
total_member_icon_label.pack(pady=10)
total_member_label=Label(member_frame, text='Total Members',bg='#2C3E58',fg='white',font=('calibri',20,'bold'))
total_member_label.pack(pady=5)
total_membercount_label=Label(member_frame, text='0',bg='#2C3E58',fg='white',font=('calibri',20,'bold'))
total_membercount_label.pack()

workout_frame=Frame(window,bg='#8E44AD',relief=RIDGE)
workout_frame.place(x=800,y=125,height=170,width=288)
total_workout_icon=PhotoImage(file='wellness.png')
total_workout_icon_label=Label(workout_frame,image=total_workout_icon,bg='#8E44AD')
total_workout_icon_label.pack(pady=10)
total_workout_label=Label(workout_frame, text='Total Workout',bg='#8E44AD',fg='white',font=('calibri',20,'bold'))
total_workout_label.pack(pady=5)
total_workoutcount_label=Label(workout_frame, text='0',bg='#8E44AD',fg='white',font=('calibri',20,'bold'))
total_workoutcount_label.pack()

window.mainloop()