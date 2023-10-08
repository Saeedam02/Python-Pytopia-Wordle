from  Wordle import Wordle

file_path = 'src/data/words_frequency.txt'
wordle = Wordle(file_path, word_len=5, limit= 10_000)
wordle.run()
