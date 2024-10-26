import re

# Define the questions and answers
qa_pairs = {
    #General Knowledge
    "what is the capital of france?": "Paris.",
    "who wrote romeo and juliet?": "William Shakespeare.",
    "what is the largest continent?": "Asia.",
    "what year did world war i begin?": "1914.",
    "who is known as the 'father of modern physics'?": "Albert Einstein.",
    "what is the main language spoken in spain?": "Spanish.",
    "what is the currency of the united states?": "US Dollar.",
    "what is the longest river in the world?": "The Nile.",
    "who painted the sistine chapel ceiling?": "Michelangelo.",
    "what planet is known as the red planet?": "Mars.",
    "what is the capital of japan?": "Tokyo.",
    "how many continents are there?": "Seven.",
    "what is the largest ocean on earth?": "The Pacific Ocean.",
    "who discovered penicillin?": "Alexander Fleming.",
    "what is the chemical symbol for gold?": "Au.",
    "who was the first woman to fly solo across the atlantic?": "Amelia Earhart.",
    "what is the smallest country in the world?": "Vatican City.",
    "who is known for the theory of evolution?": "Charles Darwin.",
    "what is the hardest natural substance on earth?": "Diamond.",
    "what is the main ingredient in hummus?": "Chickpeas.",
    "what is the capital of canada?": "Ottawa.",
    "how many bones are in the adult human body?": "206.",
    "what is the main gas in the earth's atmosphere?": "Nitrogen.",
    "what is the largest animal on earth?": "The blue whale.",
    "what year did the berlin wall fall?": "1989.",
    
    #Technology
    "what does cpu stand for?": "Central Processing Unit.",
    "what is the main function of ram?": "To store data temporarily for quick access by the cpu.",
    "what does html stand for?": "HyperText Markup Language.",
    "what is the main purpose of an operating system?": "To manage computer hardware and software resources.",
    "what is artificial intelligence?": "The simulation of human intelligence in machines.",
    "what is the primary function of a router?": "To direct data traffic between networks.",
    "what is a computer virus?": "A malicious software program that can replicate itself.",
    "what does wifi stand for?": "Wireless Fidelity.",
    "what is the internet of things?": "The network of physical devices connected to the internet.",
    "what is cloud computing?": "Storing and accessing data and programs over the internet instead of on a local computer.",
    "what is the function of a motherboard?": "It connects all the components of a computer together.",
    "what is an SSD?": "A Solid State Drive, a type of storage that uses flash memory.",
    "what is the difference between RAM and ROM?": "RAM is volatile memory used for temporary storage, while ROM is non-volatile and used for permanent storage.",
    "what is phishing?": "A method used to trick individuals into revealing personal information online.",
    "what is a firewall?": "A network security device that monitors and controls incoming and outgoing network traffic.",
    "what is bandwidth?": "The maximum rate of data transfer across a network.",
    "what is the purpose of a network switch?": "To connect devices within a local area network and manage data traffic.",
    "what is an IP address?": "A unique string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a network.",
    "what is open-source software?": "Software with source code that anyone can inspect, modify, and enhance.",
    "what is the function of a graphics card?": "To render images and video for display on a computer screen.",
    "what does SaaS stand for?": "Software as a Service, a cloud-based service where instead of downloading software on your desktop PC or business network, you instead access an application via the Internet.",
    
    #Health and Fitness
    "what is the largest organ in the human body?": "The skin.",
    "how many calories are in a pound of body fat?": "Approximately 3,500 calories.",
    "what is the recommended daily intake of water?": "About 2 liters or 8 cups, though individual needs may vary.",
    "what is a healthy body mass index (bmi) range?": "A bmi of 18.5 to 24.9.",
    "what is the benefit of cardiovascular exercise?": "It improves heart health and increases endurance.",
    "what nutrient is most important for muscle repair?": "Protein.",
    "how much sleep do adults need?": "7 to 9 hours per night.",
    "what is the role of fiber in the diet?": "To aid digestion and prevent constipation.",
    "what does bmi stand for?": "Body Mass Index.",
    "what is the protein content in chicken breast (cooked)?": "Approximately 31 grams of protein per 100 grams.",
    "how much protein is in canned tuna?": "About 30 grams of protein per 100 grams.",
    "what is the protein content in Greek yogurt?": "Around 10 grams of protein per 100 grams.",
    "how much protein does a boiled egg contain?": "Roughly 13 grams of protein per 100 grams.",
    "what is the protein content in lentils (cooked)?": "Approximately 9 grams of protein per 100 grams.",
    "how much protein is in almonds?": "About 21 grams of protein per 100 grams.",
    "what is the protein content in cottage cheese?": "Approximately 11 grams of protein per 100 grams.",
    "how much protein is in quinoa (cooked)?": "About 4 grams of protein per 100 grams.",
    "what is the protein content in black beans (cooked)?": "Roughly 8 grams of protein per 100 grams.",
    "how much protein is in a protein shake?": "Varies by brand, but typically around 20-25 grams of protein per serving (approximately 30 grams).",

    
    #Science
    "what is the powerhouse of the cell?": "The mitochondria.",
    "what is newton's second law of motion?": "Force equals mass times acceleration (F = ma).",
    "what is the most common element in the universe?": "Hydrogen.",
    "what is a habitat?": "The natural environment in which an organism lives.",
    "what is the process of water changing from liquid to gas?": "Evaporation.",
    "what is the speed of light?": "Approximately 299,792 kilometers per second (186,282 miles per second).",
    "what are the three states of matter?": "Solid, liquid, and gas.",
    "what is the atomic number of carbon?": "6.",
    "what is DNA?": "Deoxyribonucleic acid, the molecule that carries genetic information.",
    "what is a supernova?": "The explosion of a star at the end of its life cycle.",
    
    #History
    "who was the first man to fly in space?": "Yuri Gagarin.",
    "what event started the french revolution?": "The Storming of the Bastille in 1789.",
    "who was the first female pharaoh of ancient egypt?": "Hatshepsut.",
    "what was the significance of the magna carta?": "It limited the powers of the king and established legal rights.",
    "who was the first president of the united states?": "George Washington.",
    "what ancient civilization built the pyramids?": "The Egyptians.",
    "what year did world war ii end?": "1945.",
    "who was the leader of the soviet union during world war ii?": "Joseph Stalin.",
    "what was the cold war?": "A period of political tension between the Soviet Union and the United States.",
    "what was the renaissance?": "A period of cultural revival in Europe from the 14th to the 17th century.",
    
    #Geography
    "which country has the longest coastline in the world?": "Canada.",
    "what is the capital of china?": "Beijing.",
    "which desert is the largest in the world?": "The Antarctic Desert.",
    "what is the tallest mountain in africa?": "Mount Kilimanjaro.",
    "what is the largest island in the world?": "Greenland.",
    "what river flows through egypt?": "The Nile.",
    "which continent is known as the 'dark continent'?": "Africa.",
    "what is the smallest continent?": "Australia.",
    "which country is known as the Land of the Rising Sun?": "Japan.",
    "what is the capital city of australia?": "Canberra.",
    
    #Fun and Trivia
    "what is the name of the fictional bear created by a.a. milne?": "Winnie the Pooh.",
    "what is the most popular sport in the world?": "Soccer (football).",
    "what animal is known as the king of the jungle?": "The lion.",
    "what is the longest river in the united states?": "The Missouri River.",
    "what is the capital of the united states?": "Washington, D.C.",
    "what do you call a baby kangaroo?": "A joey.",
    "what is the hardest rock?": "Diamond.",
    "what fruit is known for having its seeds on the outside?": "Strawberry.",
    "how many colors are in a rainbow?": "Seven.",
    "what is the tallest building in the world?": "Burj Khalifa.",
    
    #Random Questions
    "what do you call a group of wolves?": "A pack.",
    "what is the smallest bone in the human body?": "The stapes (in the ear).",
    "what is the primary function of the liver?": "To filter blood and produce bile.",
    "what is the name of the longest river in europe?": "The Volga.",
    "what is a palindrome?": "A word, phrase, or number that reads the same forward and backward.",
    "what is the most spoken language in the world?": "Mandarin Chinese.",
    "what is the name of the first artificial satellite launched into space?": "Sputnik.",
    "who invented the telephone?": "Alexander Graham Bell.",
    "what does the acronym nasa stand for?": "National Aeronautics and Space Administration.",
    "what is the largest desert in the world?": "The Antarctic Desert.",
    "what is the most commonly used letter in the English alphabet?": "E.",
    "what is the fastest land animal?": "The cheetah.",
    "what is the capital city of iceland?": "Reykjavik.",
    "what is the primary ingredient in guacamole?": "Avocado.",
    "what year did the titanic sink?": "1912.",
}

def chatbot_response(user_input):
    greetings = re.compile(r'\b(hello|hi|hey|howdy|hiya|greetings)\b', re.IGNORECASE)
    goodbyes = re.compile(r'\b(bye|goodbye|see you|take care|farewell)\b', re.IGNORECASE)
    user_input_lower = user_input.lower()
    
    if greetings.search(user_input_lower):
        return "Hi there! How can I help you today?"
    elif goodbyes.search(user_input_lower):
        return "Goodbye! Have a nice day."
    else:
        #Checks if the user inputs matches any question that are written
        response = qa_pairs.get(user_input_lower.strip(), "I'm not sure I understand. Can you rephrase?")
        return response

#Tests the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Vedish:", chatbot_response(user_input))

#This is the First task assigned by CodSoft to Vedish. Task has been completed
#Run the tool and you will be able to chat with the Chatbot named Vedish.
#The Chatbot has 100 questions and answers gathered from the web and me.    