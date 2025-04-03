import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# this class inherits from FileSystemHandler 
# so we can reDefine methods like (oncreated , on deleted...)
class MyHandler(FileSystemEventHandler):
    def list_existing_files(self):

        # Lists all existing files containing 
        # 'content-banned' before monitoring starts.

        existing_files = [f for f in os.listdir(".") if "content-banned" in f]
        if existing_files:
            print("\n Existing 'content-banned' files in directory:")
            for file in existing_files:
                print(f"  - {file} " )
        
            print("Listening..")
        else:
            print("\n No existing 'content-banned' files found , listening ... ")

    #we create a helper function
    #in order to avoid repeating the ifs 
    def log_event(self, event, action):      
        file_name = os.path.basename(event.src_path)
        if "content-banned" in file_name:
          print(f" {file_name} has been {action}.")

    def on_created(self, event):
        self.log_event(event, "created")

    def on_modified(self, event):
        self.log_event(event, "modified")

    def on_deleted(self, event):
        self.log_event(event, "deleted")



def main():
    path_to_listen = "."
    event_handler = MyHandler()
    event_handler.list_existing_files()
    observer = Observer()
    observer.schedule(event_handler,path_to_listen,recursive=False)
    observer.start()
    try:
        # infinite loop for listening
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stop listening...")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()

   