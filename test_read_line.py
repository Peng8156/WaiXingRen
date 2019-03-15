import sys

with open('high_score.txt', 'r') as file_obj:
    read_highscore = file_obj.readline()

print(read_highscore)