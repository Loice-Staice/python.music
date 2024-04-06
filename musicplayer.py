import pygame

pygame.init()

playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]

def play_playlist():
    for song in playlist:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        while pygame.mixer.music.play():
            pass  # Wait for the song to finish playing

# Main function
def main():
    print("Welcome to  Python Music Player!")
    print("Press 'p' to play the playlist.")

    while True:
        user_input = input("Enter a command ('p' to play): ").lower()
        if user_input == "p":
            play_playlist()
        elif user_input == "q":
            pass
        else:
            print("Invalid command. Press 'p' to play or 'q' to quit.")

if __name__ == "__main__":
    main()