import csv
from django.core.management import execute_from_command_line

def main():
    with open('newfile.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Create a Question object and populate its fields
            question = Question(
                text=row['text'],
                option_a=row['option_a'],
                option_b=row['option_b'],
                option_c=row['option_c'],
                option_d=row['option_d'],
                correct_answer=row['correct_answer']
            )
            question.save()

if __name__ == '__main__':
    execute_from_command_line(['manage.py', 'runscript', 'import_csv'])