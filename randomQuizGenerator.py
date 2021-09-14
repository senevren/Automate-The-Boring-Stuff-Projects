{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09204068",
   "metadata": {},
   "outputs": [],
   "source": [
    "#! python3\n",
    "# randomQuizGenerator.py - Creates quizzes with questions and answers in\n",
    "# random order, along with the answer key.\n",
    "\n",
    "import random\n",
    "\n",
    "# The quiz data. Keys are states and values are their capitals.\n",
    "capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}\n",
    "capitalsItems = list(capitals.items())\n",
    "\n",
    "# Generate 35 quiz files.\n",
    "for quizNum in range(35): \n",
    "    # Create the quiz and answer key files.\n",
    "    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')\n",
    "    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')\n",
    "\n",
    "    # Write out the header for the quiz.\n",
    "    quizFile.write('Name:\\n\\nDate:\\n\\nPeriod:\\n\\n')\n",
    "    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')\n",
    "    quizFile.write('\\n\\n')\n",
    "\n",
    "    # Shuffle the order of the states.\n",
    "    states = list(capitals.keys()) # get all states in a list\n",
    "    random.shuffle(states) # randomize the order of the states\n",
    "\n",
    "    # Loop through all 50 states, making a question for each.\n",
    "    for questionNum in range(50):\n",
    "\n",
    "        # Get right and wrong answers.\n",
    "        correctAnswer = capitals[states[questionNum]]\n",
    "        wrongAnswers = list(capitals.values()) # get a complete list of answers\n",
    "        del wrongAnswers[wrongAnswers.index(correctAnswer)] # remove the right answer\n",
    "        wrongAnswers = random.sample(wrongAnswers, 3) # pick 3 random ones\n",
    "\n",
    "        answerOptions = wrongAnswers + [correctAnswer]\n",
    "        random.shuffle(answerOptions) # randomize the order of the answers\n",
    "\n",
    "        # Write the question and answer options to the quiz file.\n",
    "        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\\n')\n",
    "        for i in range(4):\n",
    "            quizFile.write(f\"    {'ABCD'[i]}.{answerOptions[i]}\\n\")\n",
    "        quizFile.write('\\n')\n",
    "\n",
    "        # Write out the answer key to a file.\n",
    "        answerKeyFile.write(f\"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\")\n",
    "    quizFile.close()\n",
    "    answerKeyFile.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c76b7ced",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88bc3e8f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
