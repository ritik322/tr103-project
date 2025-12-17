import customtkinter
import threading
import os 
from brain import Brain
from listen import listen
from speak import say
from actions import execute_intent

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

class AssistantApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("300x250")
        self.title("AI Assistant")
        self.resizable(True, True)

        self.chat_area = customtkinter.CTkTextbox(self, width=280, height=150)
        self.chat_area.pack(pady=10)
        self.chat_area.configure(state="disabled")

        self.status_label = customtkinter.CTkLabel(self, text="Status: Ready", font=("Arial", 14))
        self.status_label.pack(pady=5)

        self.listen_button = customtkinter.CTkButton(self, text="Start Listening", command=self.start_thread)
        self.listen_button.pack(pady=10)

        self.ai_brain = Brain()

    def update_chat(self, sender, message):
        self.chat_area.configure(state="normal")
        self.chat_area.insert("end", f"{sender}: {message}\n")
        self.chat_area.configure(state="disabled")
        self.chat_area.see("end")

    def start_thread(self):
        self.status_label.configure(text="Status: Active")
        self.listen_button.configure(state="disabled")
        thread = threading.Thread(target=self.run_assistant)
        thread.start()

    def run_assistant(self):
        self.update_chat("System", "Online and ready.")
        say("System online")
        
        while True:
            self.status_label.configure(text="Status: Listening...")
            text = listen()
            
            if text:
                self.status_label.configure(text="Status: Processing...")
                self.update_chat("You", text)
                
                intent = self.ai_brain.predict(text)
                self.update_chat("AI", f"Detected Intent -> {intent}")
                
                execute_intent(intent, text)
                
                if intent == "goodbye":
                    self.status_label.configure(text="Status: Shutting down...")
                    self.update_chat("System", "Closing...")
                    self.destroy()
                    os._exit(0)   
                
            self.status_label.configure(text="Status: Idle")

if __name__ == "__main__":
    app = AssistantApp()
    app.mainloop()