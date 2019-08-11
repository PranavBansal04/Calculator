from tkinter import *           ##importing tkinter library

def btnClick(numbers):          ##this function will be called when any button is pressed
##                                  on the calculator. It will simply append the input
##                                  to the display rectangle    
    exp=str(text_Input.get())+str(numbers)   #text_Input.get()  gets the previously appended 
##                                               string to the display                       
    text_Input.set(exp)                         #the exp variable has the new string after
##                                                  new input from the user    


# below function is called when clear button is pressed on calculator
#It sets the display text to null
def btnClearDisplay():
    text_Input.set("")

#this function will be called when "=" button is pressed on the calculator
#Pressing ener key on keyboard will also invoke this function
# it has one argument which is of NONE type. It is because I have bind the
# enter key capture with the app which you will see below.
#Its syntax is like - "root.bind('<Return>', function_name)"
#so when enter key is pressed it actually passes an argument.
# when the "=" will be pressed on calculator then no argument will be passes
#and that will be fine as the argument is explicitly being set to NONE in the function
def btnEqualsInput(event=None):
    exp=text_Input.get()        #getting the string text from display rectangle
    try:
        sumup=str(eval(exp))    #'eval' is a function which evaluates any string as
##                                python expression          
        text_Input.set(sumup)   #once the expression is evaluated, the final output
                                ##will be shown on display
    except Exception:
        text_Input.set("Invalid Expression!")   #if there is some error in the input
                                                #then an exception will be raised

cal=Tk()            #tkinter window
cal.title("Calculator")#setting title

text_Input=StringVar()  #variable for storing string from display

#every button except '=' and 'C' calls the btnClick function
#with the corresponding argument

#creating display box which actually is an Entry
textDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=25,
                  insertwidth=4,bg='white',justify='right').grid(columnspan=4)    
                                                             
#button for digit '7'
btn7=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="7",bg='white',command=lambda:btnClick(7)).grid(row=1,column=0)

#button for digit '8'
btn8=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="8",bg='white',command=lambda:btnClick(8)).grid(row=1,column=1)

#button for digit '9'
btn9=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="9",bg='white',command=lambda:btnClick(9)).grid(row=1,column=2)

# above are the top three buttons in the calculator as can be seen
#from their .grid() attribute. they all belong to the same row i.e. one in this case

#button for '+' operator, in the row 1
Addition=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="+",bg='white',command=lambda:btnClick("+")).grid(row=1,column=3)


#button for digit '4'
btn4=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="4",bg='white',command=lambda:btnClick(4)).grid(row=2,column=0)

#button for digit '5'
btn5=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="5",bg='white',command=lambda:btnClick(5)).grid(row=2,column=1)

#button for digit '6'
btn6=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="6",bg='white',command=lambda:btnClick(6)).grid(row=2,column=2)

#row 2  of buttons contain 4,5,6 and '-' operator


#button for '-' operator
Subtraction=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="-",bg='white',command=lambda:btnClick("-")).grid(row=2,column=3)


#button for digit '1'
btn1=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="1",bg='white',command=lambda:btnClick(1)).grid(row=3,column=0)

#button for digit '2'
btn2=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="2",bg='white',command=lambda:btnClick(2)).grid(row=3,column=1)

#button for digit '3'
btn3=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="3",bg='white',command=lambda:btnClick(3)).grid(row=3,column=2)

#row 3 has buttons 1,2,3 and '*' operator

#button for '*' operator, row 3
Multiply=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="*",bg='white',command=lambda:btnClick("*")).grid(row=3,column=3)

#button for digit '9'
btn0=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="0",bg='white',command=lambda:btnClick(0)).grid(row=4,column=0)

#Clear Button - clears the display
btnClear=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="C",bg='white',command=btnClearDisplay).grid(row=4,column=1)

#'=' button
btnEquals=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="=",bg='white',command=btnEqualsInput).grid(row=4,column=2)

#the below line of code captures the press of 'Enter' key from keyboard
#and when enter key is pressed, the function btnEqualsInput will be called
cal.bind('<Return>', btnEqualsInput)


#button for '/' operator
Division=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="/",bg='white',command=lambda:btnClick("/")).grid(row=4,column=3)

#button for '^' (power)
power=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="^",bg='white',command=lambda:btnClick("**")).grid(row=5,column=3)

#button for '('
bracket1=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text="(",bg='white',command=lambda:btnClick("(")).grid(row=5,column=0)


#button for ')'
bracket2=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text=")",bg='white',command=lambda:btnClick(")")).grid(row=5,column=1)

#button for decimal point(.)
decimal=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
            text=".",bg='white',command=lambda:btnClick(".")).grid(row=5,column=2)


#mainloop() is used when you are ready for the application to run. mainloop()
#is an infinite loop used to run the application, wait for an event to occur
#and process the event till the window is not closed.
cal.mainloop()    
