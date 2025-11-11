from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LyraMonitor(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("lyra_emotional_states.json"):
            print("Lyra’s emotions updated — syncing voice...")
            # Trigger voice update or dashboard refresh

observer = Observer()
observer.schedule(LyraMonitor(), path="C:/Lyra", recursive=False)
observer.start()