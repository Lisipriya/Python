from replit import audio
volume = 1
def main():
  source = audio.play_file("baby sleep.wav")
  continue_sound = True
  while continue_sound:
    source.volume = 0.5
    choice = input("Enter command: ").lower()
    if choice == 'up':
      source.volume += 0.25
    elif choice == 'down':
      source.volume -= 0.25
    elif choice == "pause":
      source.paused = not source.paused
    elif choice == "exit":
      continue_sound = False
main()
#2nd method
from playsound import playsound
can_play = True
while can_play:
    playsound("Downloads\Babysleep.wav")
    user_choice = input("Play Again? ([True]/False): ")
    if user_choice and type(user_choice) == bool:
        can_play = user_choice