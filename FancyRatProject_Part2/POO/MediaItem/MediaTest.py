from AudioBook import AudioBook
from Movie import Movie
from Song import Song

# Create an audio book object
audio_book = AudioBook("Harry Potter", "1:30:00 hs", "Joanne Kathleen Rowling", 4344234232)

# Print the object
print(audio_book)

# Play the audio book
audio_book.play()

# stop the audio book
audio_book.stop()

# Display the info of the audio book
audio_book.display_info()

# Create a movie object
movie = Movie("Puss in boots", "2:30 hs", "Chris Miller", 2011)

# Print the movie
print(movie)

# Play the movie
movie.play()

# Stop the movie
movie.stop()

# Display the info of the movie
movie.display_info()

# Create a song object
song = Song("Imagine", "John Lennon", "Plastic Ono Band", "3:03")

# Print the song object
print(song)

# Play the song
song.play()

# Stop the song
song.stop()

# Display information about the song
song.display_info()