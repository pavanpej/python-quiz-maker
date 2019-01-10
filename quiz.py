import random as r


def ask_questions():
	fh = open('untitled.csv')
	row_count = len([i for i in fh])
	questions_needed = 5
	question_numbers = r.sample(range(0, row_count), questions_needed)
	question_numbers.sort()

	correct, wrong = 0, 0

	fh = open('untitled.csv')
	# get question and answers
	for line in fh:
		sl, question, key = line.split(',')
		key = key.rstrip()
		print(f'{sl},{question},"{key}"')
		sl = int(sl)
		if sl in question_numbers:
			print(sl, "\t", question, "\nAns: ", end='')
			ans = input().lower()

			if key in ans:
				print("Correct\n")
				correct += 1
			else:
				print("Wrong\n")
				wrong += 1

			del question_numbers[0]

	print(f"\nCorrect answers: {correct}\nWrong answers: {wrong}\n")


def main():
	ask_questions()


if __name__ == '__main__':
	main()
