import audioio
import touchio
import board
import time

from digitalio import DigitalInOut, Direction

# Enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True

# Make the A1 cap sense pads
touch1 = touchio.TouchIn(board.A1)
# Make the A2 cap sense pads
touch2 = touchio.TouchIn(board.A2)
# Make the A3 cap sense pads
touch3 = touchio.TouchIn(board.A3)
# Make the A4 cap sense pads
touch4 = touchio.TouchIn(board.A4)
# Make the A5 cap sense pads
touch5 = touchio.TouchIn(board.A5)
# Make the A6 cap sense pads
touch6 = touchio.TouchIn(board.A6)
# Make the A7 cap sense pads
touch7 = touchio.TouchIn(board.A7)

# The seven audio files
audiofiles = ["bd_tek.wav", "elec_hi_snare.wav", "elec_cymbal.wav", "elec_blip2.wav", "bd_zome.wav", "bass_hit_c.wav", "drum_cowbell.wav"]
# AudioOut can be used to output an analog audio signal on a given pin.
a = audioio.AudioOut(board.A0)
# Since we are not using adafruit_circuitplayground.express import cpx, we would need to write our own play_file() function
def play_file(filename):
  f = open(filename, "rb")
  wave = audioio.WaveFile(f)
  a.play(wave)
  time.sleep(bpm/960)  # sixteenthNote delay

while True:
  for i in range(7):
    if touchPad[i].value:
      play_file(audiofiles[i])
