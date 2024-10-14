from pydub import AudioSegment
from pydub.playback import play

# Function to create mashup from the downloaded songs
def create_mashup(song_paths, output_path="mashup.mp3"):
    mashup = AudioSegment.empty()

    for song in song_paths:
        try:
            audio = AudioSegment.from_file(song)
            duration = len(audio)  # Length of the song in milliseconds
            start = int(duration * 0.1)  # Start from 10% of the song
            end = int(duration * 0.3)    # Use 20% of the song for the mashup
            print(f"Adding {song} to the mashup")
            mashup += audio[start:end]  # Add a 20% portion of the song
        except Exception as e:
            print(f"Error processing {song}: {e}")

    # Export the mashup to a file
    mashup.export(output_path, format="mp3")
    print(f"Mashup created: {output_path}")

# Create a mashup from the downloaded songs
if downloaded_songs:
    create_mashup(downloaded_songs)
else:
    print("No songs were downloaded.")
