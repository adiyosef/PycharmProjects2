import Utils

# writing a score file with incremented user score
def add_score(points):
    try:
        score_file = open("/Users/adi.y/PycharmProjects/devexp/Project1/" + Utils.SCORES_FILE_NAME, 'r+')
        current_points = int(score_file.read())
        current_points = current_points + points
        score_file.seek(0)
        score_file.write(str(current_points))

# if file not found creating a file and writing the score
    except OSError as e:
        print(e, "\n created a new file and saved the score")
        score_file = open("/Users/adi.y/PycharmProjects/devexp/Project1/" + Utils.SCORES_FILE_NAME, 'w')
        score_file.write(str(points))
# close score file
    finally:
        score_file.close()
