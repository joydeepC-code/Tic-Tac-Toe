from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.title("Tic Tac Toe")

#labels
Label(window, text="Player 1: X", font=("Helvecta 16 bold")).grid(row=0, column=1)
Label(window, text="Player 2: O", font=("Helvecta 16 bold")).grid(row=0, column=2)

boxNo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark = ''
noOfClicks = 0

boxes = ["box"] * 10

def winConditions (boxes, sign):
    return ((boxes[1] == boxes[2] == boxes[3] == sign)
        or (boxes[4] == boxes[5] == boxes[6] == sign)
        or (boxes[7] == boxes[8] == boxes[9] == sign)
        or (boxes[1] == boxes[5] == boxes[9] == sign)
        or (boxes[3] == boxes[5] == boxes[7] == sign)
        or (boxes[1] == boxes[4] == boxes[7] == sign)
        or (boxes[2] == boxes[5] == boxes[8] == sign)
        or (boxes[3] == boxes[6] == boxes[9] == sign))

def updater (box):
    global noOfClicks, mark, boxNo

    if box == 1 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button1.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()

        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()

    if box == 2 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button2.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()

        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()

    if box == 3 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button3.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()

        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()

    if box == 4 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button4.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()

        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()

    if box == 5 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button5.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()

        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()

    if box == 6 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button6.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()

        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()

    if box == 7 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button7.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()

        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()

    if box == 8 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button8.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()

        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()

    if box == 9 and box in boxNo:
        boxNo.remove(box)

        if noOfClicks % 2 == 0:
            mark = 'X'
            boxes[box] = mark

        elif noOfClicks % 2 == 1:
            mark = 'O'
            boxes[box] = mark

        button9.config(text = mark)
        noOfClicks += 1
        sign = mark

        if (winConditions(boxes, sign) and sign == 'X'):
            msg.showinfo("Result", "Player 1 wins")
            window.destroy()
        elif (winConditions(boxes, sign) and sign == 'O'):
            msg.showinfo("Result", "Player 2 wins")
            window.destroy()
    #draw
    if (noOfClicks > 8 and winConditions(boxes, 'X') == False and winConditions(boxes, 'O') == False):
        msg.showinfo("Result", "Match tied")
        window.destroy()

button1 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(1))
button1.grid(row=1, column=1)
button2 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(2))
button2.grid(row=1, column=2)
button3 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(3))
button3.grid(row=1, column=3)
button4 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(4))
button4.grid(row=2, column=1)
button5 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(5))
button5.grid(row=2, column=2)
button6 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(6))
button6.grid(row=2, column=3)
button7 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(7))
button7.grid(row=3, column=1)
button8 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(8))
button8.grid(row=3, column=2)
button9 = Button(window, width=15, font=("Helvecta 16 bold"), height=7, command=lambda:updater(9))
button9.grid(row=3, column=3)

window.mainloop()