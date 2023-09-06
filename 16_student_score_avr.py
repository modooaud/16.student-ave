# ................calculating average score of four subjects each for 16 students...........
subjects = ['english','maths', 'science', 'accounting']
total_score = 0
for exam_scores in range(4):
    all_score = int(input(f'please enter exam_scores{input(exam_scores)'{subjects}'}))
    total_score = total_score + all_score
ave_score = total_score / 4
