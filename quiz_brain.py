import pandas as pd
import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.missed_questions = []  # Track missed questions

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            # Add missed question to the list
            self.missed_questions.append({
                "Question": self.current_question.text,
                "Correct Answer": self.current_question.answer
            })
            return False

    def save_missed_questions(self, filename="missed_questions.csv"):
        """Save missed questions as a CSV file with HTML unescaped."""
        if self.missed_questions:
            # Unescape HTML characters in the question text
            unescaped_data = [
                {
                    "Question": html.unescape(q["Question"]),
                    "Correct Answer": q["Correct Answer"],
                }
                for q in self.missed_questions
            ]
            df = pd.DataFrame(unescaped_data)
            df.to_csv(filename, index=False, encoding="utf-8")
            print(f"Missed questions saved to {filename}.")
        else:
            print("No missed questions to save.")
