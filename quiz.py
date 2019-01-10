import random as r


def ask_questions():
	"""Displays the question and takes in the answer. Then checks if the given answer has the key of the question."""
	fh = open('untitled.csv')
	row_count = len([i for i in fh])
	questions_needed = 5
	question_numbers = r.sample(range(1, row_count+1), questions_needed)
	question_numbers.sort()

	correct, wrong = 0, 0

	fh = open('untitled.csv')
	# get question and answers
	i = 1
	for line in fh:
		sl, question, key = line.split(',')
		key = key.rstrip()

		# print(f'{sl},{question},"{key}"') # for debugging

		sl = int(sl)
		if sl in question_numbers:
			print(i, ". ", question, "\nYour Ans: ", end='')
			ans = input().lower()

			if key in ans:
				print("Correct\n")
				correct += 1
			else:
				print("Wrong\n")
				wrong += 1

			i += 1
			del question_numbers[0]

	print(f"\nCorrect answers: {correct}\nWrong answers: {wrong}\n")


def main():
	ask_questions()


if __name__ == '__main__':
	main()
