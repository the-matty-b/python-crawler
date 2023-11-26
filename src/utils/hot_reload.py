import pygame
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class HotReloadHandler(FileSystemEventHandler):
    def __init__(self, observer):
        self.observer = observer
        
    def on_any_event(self, event):
        if event.is_directory or not event.src_path.endswith(".py"):
            return
        print(f"Reloading due to change in {event.src_path}")
        pygame.quit()
        self.observer.stop()
        self.observer.join()
        exec(open("src/main.py").read(), globals())
        pygame.init()