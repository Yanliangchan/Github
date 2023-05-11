import random

# initialisation of words bank
wordList = ["biodiversity", "deforestation", "reuse", "reduce","recycle", "pollution", "climate", "biodegradable",
            "desertification", "extinction", "environment"]

hintDict = {"biodiversity":"the number and variety of living things in a particular environmental area.",
            "deforestation":"the cutting down of trees in a large area; the destruction of forests by people.",
            "reuse":" taking old items that you might consider throwing away and finding a new use for them.",
            "reduce":"to minimise the amount of waste we create.",
            "recycle":"uses old products in new ways.",
            "pollution":"damage caused to water, air.... by harmful substances or waste.",
            "climate":"the general weather conditions usually found in a particular place.",
            "biodegradable":"able to decay naturally and harmlessly.",
            "desertification":"the process by which land changes into desert.",
            "extinction":"being destroyed so that they no longer exist.",
            "environment":"the air, water and land in or on which people, animals and plants live."}

random.shuffle(wordList)
numOfLive = 5
winningScore = 5
score = 0
# setup screen
print("Welcome to the game Environment Unscramble")
print("Try to Unscramble the following Words")

for word in wordList:

    shuffledWord = "".join(random.sample(word, len(word)))

    if numOfLive == 0:
        print("Asians are suppose to be smart, You lose")
        break

    if score == winningScore:
        print("Well done english prof, You win")
        break

    print("SCORE = " + str(score))
    print("LIVES = " + str(numOfLive))
    print(shuffledWord)
    print("hint: " + hintDict.get(word))

    guess = input("What is your guess?:")

    if guess == word:
        score += 1
        print("Yaaaayy You got it right")
    else:
        numOfLive -= 1
        print("Haizzz You got it wrong")