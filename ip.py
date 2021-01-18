import tkinter, socket

window = tkinter.Tk()

window.resizable(False, False)

ip = tkinter.Label(window, text= socket.gethostbyname(socket.gethostname()), fg='black', font=("Helvetica", 36)).pack()

window.title("Here's your IP: " + socket.gethostbyname(socket.gethostname()))
window.geometry("300x50+10+20")
window.mainloop()