import random

questions = {
    "Why did the banana go to the doctor?":"Because it wasn’t peeling well!",
    "What has four wheels and flies?":"A garbage truck!",
    "Why was the math book sad?":"Because it had too many problems!",
    "What do you call a sleeping bull?":"A bulldozer!",
    "Why can’t your nose be 12 inches long?":"Because then it would be a foot!",
    "What do cats eat for breakfast?":"Mice Krispies!",
    "Why did the computer go to the doctor?":"Because it had a virus!",
    "What do you call a bear with no teeth?":"A gummy bear!",
    "Why did the student eat his homework?":"Because the teacher said it was a piece of cake!",
    "What kind of tree fits in your hand?":"A palm tree!",
    "Why did the bicycle fall over?":"Because it was two-tired!",
    "What do you call cheese that isn't yours?":"Nacho cheese!",
    "What has ears but cannot hear?":"A cornfield!",
    "Why are fish so smart?":"Because they live in schools!",
    "What do you call a fake noodle?":"An impasta!"

}

def funny_questions():
    selected_question = random.choice(list(questions.keys()))
    print("Question: ", selected_question,)
    print("Answer: ", questions[selected_question])
