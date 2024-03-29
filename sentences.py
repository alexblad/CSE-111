import random

def main():
    """Store different grammatical parts as variables for the sentces."""
    det1=get_determiner(1)
    det2=get_determiner(2)
    noun1=get_noun(1)
    noun2=get_noun(2)
    verb1=get_verb(0,'past')
    verb2=get_verb(1,'present')
    verb3=get_verb(2,'present')
    verb4=get_verb(0,'future')
    phrase1=get_prepositional_phrase(1)
    phrase2=get_prepositional_phrase(2)

    print(det1.capitalize()+' ' + noun1+' ' + verb1+' '+phrase1+'.')

    """Run get_determiner, get_noun and get_prepositional_phrase again for more randomness, store new variables"""
    det1=get_determiner(1)
    noun1=get_noun(1)
    phrase1=get_prepositional_phrase(1)
    
    print(det1.capitalize()+' ' + noun1+' ' + verb2+' ' +phrase1+'.')

    det1=get_determiner(1)
    noun1=get_noun(1)
    phrase1=get_prepositional_phrase(1)

    print(det1.capitalize()+' ' + noun1+' ' + verb4+' '+phrase1+'.')
    print(det2.capitalize()+' ' + noun2+' ' + verb1+' '+phrase2+'.')

    """Run get_determiner, get_noun again and get_prepositional_phrase again for more randomness, store new variables"""

    det2=get_determiner(2)
    noun2=get_noun(2)
    phrase2=get_prepositional_phrase(2)
    print(det2.capitalize()+' ' + noun2+' ' + verb3+' '+phrase2+'.')

    det2=get_determiner(2)
    noun2=get_noun(2)
    phrase2=get_prepositional_phrase(2)
    print(det2.capitalize()+' ' + noun2+' ' + verb4+' '+phrase2+'.')


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity==1:
        words=["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words=["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    word=random.choice(words)
    return(word)

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense=='past':
        verbs=["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense=='present' and quantity==1:
        verbs=["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense=='present' and quantity !=1:
        verbs=["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    else:
        verbs=[ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    verb=random.choice(verbs)
    return(verb)

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    preps=["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    prep=random.choice(preps)
    return(prep)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """

    if quantity==1:
        det=get_determiner(1)
        noun=get_noun(1)
        prep=get_preposition()

    else:
        det=get_determiner(2)
        noun=get_noun(2)
        prep=get_preposition()
    
    phrase=str(prep)+' '+str(det)+ ' '+str(noun)
    return(phrase)

main()
    