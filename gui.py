from tkinter import*
from chat import get_response

BG_GRAY = "#D2B48C"  # Light brown
BG_COLOR = "#4A312C"  # Dark brown
TEXT_COLOR = "#4A312C"
CREAM = "#EAE0C8"

FONT = "Helvetica 11"
FONT_BOLD = "Helvetica 10 bold"

class ChatBOTApp:

    def __init__(self):
        
        self.window = Tk()
        self.bot_name = "Cayci Huseyin"
        self._setup_main_window()    

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):

        self.window.title("Coffee Store ChatBOT")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # Head Label
        head_label = Label(self.window, bg=BG_COLOR, fg=CREAM, text="Welcome!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
      
        # Divider
        line = Label(self.window, width=400, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.06, relheight=0.0175)

        # Text Widget
        self.text_widget = Text(self.window, width=20, height=2, bg=CREAM, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.75, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scroll Bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.97)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom Label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message Input
        self.message_entry = Entry(bottom_label, bg=BG_COLOR, fg=CREAM, font=FONT)
        self.message_entry.place(relwidth=0.75, relheight=0.06, relx=0.008, rely=0.011)
        self.message_entry.focus()
        self.message_entry.bind("<Return>", self._when_enter_pressed)

        # Send Button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda:self._when_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


    def _when_enter_pressed(self, event):
        message = self.message_entry.get()
        self._insert_message(message, "You")

    def _insert_message(self, message, sender):
        if not message:
            return
        self.message_entry.delete(0, END)
        input = f"{sender}: {message}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, input)
        self.text_widget.configure(state=DISABLED)

        response = f"{self.bot_name}: {get_response(message)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, response)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

        if "bye" in message.lower():
            self.window.after(2000, self.window.destroy)
        

if __name__=="__main__":
    app = ChatBOTApp()
    app.run()