import random # to make responses more dynamic

def fitness_chatbot():
    print("💪 Hey there! I'm FitBot, your virtual fitness buddy!")
    print("Let's talk about health, workouts, or motivation!")
    print("Type 'help' to see what you can ask about, or 'bye' to end our chat.\n")

    # Dictionary (data structure) for fitness topics
    fitness_info = {
        "workout": [
            "🏋️‍♀️ Aim for at least 3–5 workout sessions a week. Consistency beats perfection!",
            "🤸 Try mixing strength training, cardio, and stretching — your body loves variety!",
            "🔥 Even a 20-minute workout counts — just move that body!"
        ],
        "nutrition": [
            "🥗 Eat balanced meals: protein for muscle, carbs for energy, and veggies for nutrients!",
            "🍳 Don’t skip breakfast — your body needs fuel to start strong!",
            "🥑 Choose whole foods over processed ones — your body will thank you!"
        ],
        "hydration": [
            "💧 Drink water often! Around 2–3 liters per day is a great goal.",
            "🚰 Fun fact: being hydrated improves your focus *and* workouts!",
            "🫖 Herbal teas count too — as long as they’re unsweetened!"
        ],
        "rest": [
            "😴 Sleep 7–9 hours a night for recovery and muscle growth.",
            "🛌 Rest days are part of progress — not a break from it!",
            "🌙 Better sleep = better gains!"
        ],
        "motivation": [
            "🔥 Don’t wait for motivation — start small and it’ll come!",
            "✨ Progress, not perfection. You’re doing amazing!",
            "🏃 Remember: one workout at a time adds up to big results!"
        ],
        "weight gain": [
            "🍗 Eat more calories than you burn — but choose healthy, high-protein foods!",
            "🥜 Snacks like peanut butter, oats, and eggs help boost muscle mass!",
            "💪 Strength training + protein = healthy weight gain!"
        ],
        "weight loss": [
            "🥦 Stay in a calorie deficit — move more, eat smart!",
            "🚶 Add more steps to your day — even small movements matter!",
            "🍎 Be patient — consistency will always beat speed!"
        ]
    }

    # Fitness challenge suggestions
    challenges = [
        "Do 10 jumping jacks right now!",
        "Take a 30-second stretch break!",
        "Drink a glass of water before you continue!",
        "Do 5 squats while smiling 😄",
        "Walk around your room for 1 minute — go!"
    ]

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("FitBot: Bye for now! Stay strong, hydrated, and keep glowing 💪💧✨")
            break

        elif user_input == "help":
              print("FitBot: You can ask about: workout, nutrition, hydration, rest, motivation, weight gain, or weight loss.")

        elif user_input in fitness_info:
             # Randomly pick one of the responses for variety
             response = random.choice(fitness_info[user_input])
             print(f"FitBot: {response}")

             # Sometimes add a random fitness challenge for fun
             if random.random() < 0.3: # 30% chance
                 print(f"🏆 Challenge time: {random.choice(challenges)}")

        else:
             print("FitBot: Hmm, I'm not sure about that 🤔")
             print("Try typing 'help' to see what I can talk about!")

# Run chatbot
fitness_chatbot()