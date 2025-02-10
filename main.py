import time

from lib import download_func, isFileExist, banner

def runingTka():
    i = 0
    while i <= 1:
        print(i)
        i = i + 1
    return True

class runnableTask:
    def __init__(self, url):
        self.paused = False
        self.running = True
        self.url = url
    
    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False

    def stop(self):
        self.running = False

    def run(self):
        try:
            while self.running:
                if not self.paused:
                    downloadInstance = download_func.DownloadFile(self.url)
                    if downloadInstance == True:
                        self.stop()
        except KeyboardInterrupt:
            self.pause()
            self.handle_user_input()

    def handle_user_input(self):
        while True:
            user_input = input("Do you want to (R)esume or (Q)uit? ").strip().lower()
            if user_input == 'r':
                self.resume()
                self.run()  # Continue running the task
                break
            elif user_input == 'q':
                print("Exiting task...")
                self.stop()
                break
            else:
                print("Invalid input. Please enter 'R' to resume or 'Q' to quit.")

def main():
    banner.banner()
    userUrl = input("Enter your url : ")
    task = runnableTask(userUrl)
    task.run()
        

if __name__ == "__main__":
    main()