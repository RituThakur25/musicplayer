import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("600x400")
        mixer.init()    
        self.playlist = []
        self.current_index = 0   
        self.create_widgets()

    def create_widgets(self):
     
        self.playlist_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="lightgray", selectbackground="blue")
        self.playlist_listbox.pack(pady=10)

      
        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack(side=tk.LEFT, padx=20)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.previous_button = tk.Button(self.root, text="previous", command=self.previous_music)
        self.previous_button.pack(side=tk.LEFT, padx=20)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_music)
        self.next_button.pack(side=tk.LEFT, padx=10)
        
       
        self.playlist_listbox.bind("<Double-1>", self.play_from_listbox)

    def add_song(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

        if file_path:
           
            self.playlist.append(file_path)
            song_name = os.path.basename(file_path)
            self.playlist_listbox.insert(tk.END, song_name)

    def play_music(self):
        if self.playlist:
            
            selected_index = self.playlist_listbox.curselection()
            if selected_index:
                self.current_index = selected_index[0]


            mixer.music.load(self.playlist[self.current_index])
            mixer.music.play()

    def stop_music(self):
        mixer.music.stop()

    def next_music(self):
       
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_music()

    def previous_music(self):
       
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play_music()


    def play_from_listbox(self, event):
      
        self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()