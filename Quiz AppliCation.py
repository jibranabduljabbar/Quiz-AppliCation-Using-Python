Quiz_AppliCation = [
    {
        "S no.": "Q_1",
        "Question": "Who was the first President of the Constitution Assembly of Pakistan?",
        "Options": ["Quaid-e-Azam","Sardar Abdur Rab Nishtar","Liaquat Ali Khan","Moulvi Tameez-ud-Din"],
        "Answer": "Quaid-e-Azam"
    },
    {
        "S no.": "Q_2",
        "Question": "After how many years did Pakistan got its first Constitution?",
        "Options": ["9 years","7 years","5 years","11 years"],
        "Answer": "9 years"
    },
    {
        "S no.": "Q_3",
        "Question": "Who was Mohammad Ali Bogra?",
        "Options": ["Prime Minister","Foreign Minister","Parliament Minister","Law Minister"],
        "Answer": "Prime Minister"
    },
    {
        "S no.": "Q_4",
        "Question": "When first constitution of Pakistan was enforced?",
        "Options": ["23rd March 1956","8th June 1956","14th August 1956","25th December 1956"],
        "Answer": "23rd March 1956"
    },
    {
        "S no.": "Q_5",
        "Question": "What official name was given to Pakistan in 1956 constitution?",
        "Options": ["Islamic Republic of Pakistan","United States of Pakistan","Islamic Pakistan","Republic of Pakistan"],
        "Answer": "Islamic Republic of Pakistan"
    },
    {
        "S no.": "Q_6",
        "Question": "What is the other name of Mohammad Ali Bogra Formula?",
        "Options": ["Constitutional Formula","New Law of Pakistan","Pakistan Report","Third Report"],
        "Answer": "Constitutional Formula"
    },
    {
        "S no.": "Q_7",
        "Question": "Who was the Prime Minister of Pakistan during enforcement of first constitution?",
        "Options": ["Choudhry Mohammad Ali","Mohammad Ali Bogra","Khwaja Nazim Uddin","Ibrahim Ismail Chundrigar"],
        "Answer": "Choudhry Mohammad Ali"
    },
    {
        "S no.": "Q_8",
        "Question": "What document was firstly drafted to give pace to constitution making process?",
        "Options": ["Objective Resolution","Pakistan Act","Independence Act","Representative Act"],
        "Answer": "Objective Resolution"
    },
    {
        "S no.": "Q_9",
        "Question": "What age was prescribed for President in 1956 constitution?",
        "Options": ["40 years","55 years","45 years","50 years"],
        "Answer": "40 years"
    },
    {
        "S no.": "Q_10",
        "Question": "In respect of religion what term was set for President and Prime Minister in 1956 constitution?",
        "Options": ["He must be a Muslim","He may be a Muslim","He must not be Christian","He must not be Hindu"],
        "Answer": "He must be a Muslim"
    }
]

Score = 0

for Quiz in Quiz_AppliCation :
    Data = Quiz["S no."] + ": " + Quiz["Question"] + "\n" +"\n" + "* Give your answer in the input field!" + "\n" + "\n" +"1): "+ Quiz["Options"][0] + "\n" +"2): "+ Quiz["Options"][1] + "\n" +"3): "+ Quiz["Options"][2] + "\n" + "4): "+ Quiz["Options"][3] + "\n" + "\n"
    User_Answer = input(Data)
    if User_Answer == Quiz["Answer"] :
        Score += 1
        
        print("Your Score Is: " + str(Score) + "\n")