import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# this class inherits from FileSystemHandler so we can reDefine methods like (oncreated , on deleted...)
class MyHandler(FileSystemEventHandler):
    def list_existing_files(self):

        # Lists all existing files containing 'content-banned' before monitoring starts.

        existing_files = [f for f in os.listdir(".") if "content-banned" in f]
        if existing_files:
            print("\n Existing 'content-banned' files in directory:")
            for file in existing_files:
                print(f"  - {file} " )
        
            print("Listening..")
        else:
            print("\n No existing 'content-banned' files found , listening ... ")

    def on_created(self, event):
        # Check if 'content-banned' is in the file name
        if "content-banned" in os.path.basename(event.src_path):
            print(f"File {event.src_path} has been created")

    def on_modified(self, event):
        # Check if 'content-banned' is in the file name
        if "content-banned" in os.path.basename(event.src_path):
            print(f"File {event.src_path} has been modified")

    def on_deleted(self, event):
        # Check if 'content-banned' is in the file name
        if "content-banned" in os.path.basename(event.src_path):
            print(f"File {event.src_path} has been deleted")


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

   
