#Indulgent Brands
#Baskin Robbins
#Cleaning
#Cleaning Steps: 
#1. Take the first line of text in the text file and replace em dash w/ space
#2. Split into indvl items that don't have emdash
#3. Clean word takes indvl terms and gets rid of any symbols/etc
#4. Adds final items into word list 

def split_line(line):
    return line.replace('—', ' ').split()
def clean_word(word):
    return ''.join(char for char in word if char.isalpha() or char == '-').lower()

words = [] #final list that contains all cleaned text
file_name = r"C:\Users\rhan1\Documents\OIM3640\oim3640\mini_projects\baskin_robbins.txt"
with open(file_name, encoding="utf-8") as f:
    for line in f: #line in this case is the entire block of text in text file bcz no breaks in space
        for word in split_line(line): #this loop is saying for each indvl item in the list w/o the emdash, clean the items
            word = clean_word(word)
            if word:
                 words.append(word) 
print("ORIGINAL:")
print(words)
stopwords = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "is", "it", "this", "said", "that", "are", "was","we", "our", "you", "thats","every", "your", "be", "bananas","even", "as", "its", "by", "from","have", "has", "not", "made","so", "all", "their","going", "they", "will","at", "make","more", "up", "out", "about", "into", "than", "can", "throughout", "get","what", "when", "which", "who", "how", "if", "us", "also","just", "been", "do", "did", "were", "him", "her", "his","march", "wednesday", "baskinrobbins", "baskin-robbins", "baskin", "robbins", "participating", "locations", "nationwide","limited", "time", "beginning", "available", "members", "member",
"rewards", "br", "app", "access", "deal", "unlock", "exclusive","benefits", "invited", "celebrate", "throughout", "join", "added",
"treat", "introducing", "sure", "send", "anyone", "totally","keeps", "coming", "back", "nicole", "boutwell", "vice", "president","culinary", "marketing", "enjoy", "de","twist", "un-peel-ievably", 'wednesdays','base', 'brand', 'british','midweek', 'moments', 'month','ice', 'inspired', 'leche', 'lovers'}
clean_words = [word for word in words if word not in stopwords]
print("CLEANED:")
print(clean_words)

#Word Freq
word_freq = {}
for word in clean_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)

#Top 10
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True) #.items() transforms dictionary key and value pairs into a tuple #x[1] grabs the second value of the tuple+sorts that and the actual tuple by desc. order 
top_10_banana = sorted_words[:10] #only gets tuples from index 0-9
print("\nTop 10 words:")
for word, count in top_10_banana:
    print(f"  {word}: {count}")

# Unique Words 
# Use a set bcz gets rid of duplicates and can see uniqueness 
# If a brand uses a lot of different words i.e. high unique word count, a lot of variety
# If a brand uses the same words over and over again, low unique word count 
unique_words_banana = set(clean_words)
print(f"Total words:{len(clean_words)}")
print(f"Unique words: {len(unique_words_banana)}")
print(sorted(unique_words_banana))


#Baskin Robbins - Dubai Chocolate 
#Cleaning
def split_line(line):
    return line.replace('—', ' ').split()
def clean_word(word):
    return ''.join(char for char in word if char.isalpha() or char == '-').lower()

words = [] #final list that contains all cleaned text
file_name = r"C:\Users\rhan1\Documents\OIM3640\oim3640\mini_projects\baskin_robbins_2.txt"
with open(file_name, encoding="utf-8") as f:
    for line in f: #line in this case is the entire block of text in text file bcz no breaks in space
        for word in split_line(line): #this loop is saying for each indvl item in the list w/o the emdash, clean the items
            word = clean_word(word)
            if word:
                 words.append(word) 
print("ORIGINAL:")
print(words)

stopwords = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "is", "it", "this", "said", "that", "are", "was","we", "our", "you", "thats","every", "your", "be", "bananas","even", "as", "its", "by", "from","have", "has", "not", "made","so", "all", "their","going", "they", "will","at", "make","more", "up", "out", "about", "into", "than", "can", "throughout", "get","what", "when", "which", "who", "how", "if", "us", "also","just", "been", "do", "did", "were", "him", "her", "his","march", "wednesday", "baskinrobbins", "baskin-robbins", "baskin", "robbins", "participating", "locations", "nationwide","limited", "time", "beginning", "available", "members", "member","rewards", "br", "app", "access", "deal", "unlock", "exclusive","benefits", "invited", "celebrate", "throughout", "join", "added","treat", "introducing", "sure", "send", "anyone", "totally","keeps", "coming", "back", "nicole", "boutwell", "vice", "president","culinary", "marketing", "enjoy","inspired", "collection", "lineup", "featuring",
"including", "brand", "new", "plus", "full", "learn", "visit", "follow",
"download", "instagram", "tiktok", "facebook", "www","seeing", "knew",
"around", "giving", "another", "way", "perfect", "experience", "again",
"time", "april", "may", "fall", "past", "debut","best", "three", "loaded", "finished","mixed", "packed", "layers", "true", "quickly", "became","guests", "want", "could", "return", "returns", "ultimate","chopped", "garnish", "repeat", "combination", "every", "pure", "even", "premium", "frozen", "enjoy","delivers","here","making", "mix", "much", "n","scoop","ways","worlds","wwwbaskinrobbinscom", "x", "yet","sippistachio","bar","ice","had","only","enough","along","bring","then","after","form", "cup", "recloseable", "convenient", "along","beverages", "desserts", "flavors", "spring", "demand",
"popular", "cant", "couldnt", "brandnew","chocolateinspired"}
clean_words = [word for word in words if word not in stopwords]
print("CLEANED:")
print(clean_words)

#Word Freq
word_freq = {}
for word in clean_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)

#Top 10
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True) 
top_10_dubai = sorted_words[:10] 
print("\nTop 10 words:")
for word, count in top_10_dubai:
    print(f"{word}: {count}")

#Unique Words 
unique_words_dubai = set(clean_words)
print(f"Total words:{len(clean_words)}")
print(f"Unique words: {len(unique_words_dubai)}")
print(sorted(unique_words_dubai))


#McDonalds
#Cleaning
def split_line(line):
    return line.replace('—', ' ').split()

def clean_word(word):
    return ''.join(char for char in word if char.isalpha() or char == '-').lower()

words = [] 
file_name = r"C:\Users\rhan1\Documents\OIM3640\oim3640\mini_projects\mcdonalds.txt"
with open(file_name, encoding="utf-8") as f:
    for line in f: 
        for word in split_line(line):
            word = clean_word(word)
            if word:
                words.append(word) 

print("ORIGINAL:")
print(words)

stopwords = {
    # basic english stopwords
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of","adds",
    "with", "is", "it", "this", "that", "are", "was", "we", "our", "you",
    "be", "as", "its", "by", "from", "have", "has", "not", "so", "all",
    "they", "will", "more", "up", "out", "than", "can", "get", "do", "did",
    "were", "also", "just", "been", "which", "who", "how", "if", "us",
    "what", "when", "any", "make", "made", "going", "even", "their", "them",
    "these", "those", "some", "no", "too", "very", "there", "where", "would",
    "could", "should", "said", "only", "both", "much", "most", "own", "every",
    "each", "here", "while", "though", "whether", "thats", "its", "dont",
    "weve", "im", "id", "new", "one", "two", "three", "four", "five",
    # mcdonalds specific
    "mcdonalds", "mcdonald", "mccrispy", "arch", "burger", "sandwich",
    "wrap", "strip", "strips", "jan", "nov", "starting", "ready", "head",
    "grab", "let", "take", "level", "order", "item", "items", "restaurants",
    "across", "like", "go", "path", "choose", "lasso", "quite", "simply",
    "really", "something", "know", "needed", "lovin", "relationship", "season",
    "day", "dropping", "roses", "red", "violets", "blue", "saddle", "cowboys",
    "cowgirls", "city-slickers", "aficionados", "carte", "la", "town", "hands",
    "heart", "beat", "skip", "letter", "love", "language", "thought", "deserved",
    "created", "thatll", "theres", "youll", "lets", "were", "want", "explore",
    "decide", "gives", "builds", "lend", "blueintroducing", "version", "profile",
    "features", "packed", "topped", "wrapped", "served", "toasted", "shredded",
    "thick", "folded", "drizzled", "infused", "coated", "delivering", "altogether",
    "packing", "perfectly", "golden-brown", "fan-favorites", "limited-edition",
    "limited-time", "go-to", "grab-and-go", "late-night", "mild-meets-wild",
    "game-changing", "crinkle-cut", "valentines", "afternoon", "daytime",
    "breakfast", "quarter", "pound", "slices", "seeds", "buns", "patties",
    "patty", "filet", "making", "alongside", "atop", "pairs", "with", "worlds",
    "yet", "you", "your", "big", "hot", "honey", "buffalo", "ranch", "sauce",
    "bacon", "snack", "biscuit", "egg", "sausage", "pork", "dip", "cup",
    "deluxe", "makeover", "menu", "addition", "welcome", "source", "updates",
    "returning", "offers", "spotted", "limited", "available", "nationwide",
    "participating", "march", "premium", "ultimate", "experience", "way",
    "enjoy", "perfect", "match", "best", "dream", "team", "fix", "note",
    "notes", "whole", "white", "poppy", "sesame", "potato", "roll", "tortilla",
    "breading", "protein", "treat", "introducing", "time", "g", "oz", "u", "s",
    "x", "their", "right", "side", "golden", "brown", "signature", "beats","adds", "consider", "giving", "didnt", "enough", "cant","finish", "gentle", "subtle", "featuring", "offerings","delivers", "things", "spice", "boldest", "crisp","flavors", "ingredients", "balanced", "balance", "blend"
}

clean_words = [word for word in words if word not in stopwords]
print("CLEANED:")
print(clean_words)

# Word Freq
word_freq = {}
for word in clean_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)

#Top 10
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True) 
top_10_mcd = sorted_words[:10] 
print("\nTop 10 words:")
for word, count in top_10_mcd:
    print(f"{word}: {count}")

#Unique Words 
unique_words_mcd = set(clean_words)
print(f"Total words: {len(clean_words)}")
print(f"Unique words: {len(unique_words_mcd)}")
print(sorted(unique_words_mcd))



#Sweetgreen 1 
#Cleaning
def split_line(line):
    return line.replace('—', ' ').split()

def clean_word(word):
    return ''.join(char for char in word if char.isalpha() or char == '-').lower()

words = []
file_name = r"C:\Users\rhan1\Documents\OIM3640\oim3640\mini_projects\sweetgreen_1.txt"
with open(file_name, encoding="utf-8") as f:
    for line in f:
        for word in split_line(line):
            word = clean_word(word)
            if word:
                words.append(word)

print("ORIGINAL:")
print(words)

stopwords = {
    # basic english
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of",
    "with", "is", "it", "this", "that", "are", "was", "we", "our", "you",
    "be", "as", "its", "by", "from", "have", "has", "not", "so", "all",
    "they", "will", "more", "up", "out", "than", "can", "get", "do", "did",
    "were", "also", "just", "been", "which", "who", "how", "if", "us",
    "what", "when", "any", "make", "made", "going", "even", "their", "them",
    "these", "those", "some", "no", "too", "very", "there", "where", "would",
    "could", "should", "said", "only", "both", "much", "most", "own", "every",
    "each", "here", "while", "new", "one", "two", "three", "now", "across",
    "about", "into", "while", "through", "without", "about", "between",
    # sweetgreen specific
    "sweetgreen", "wraps", "wrap", "brand", "format", "test", "market",
    "locations", "location", "participating", "available", "guests", "guest",
    "menu", "item", "items", "order", "app", "visit", "find", "information",
    "launched", "launching", "introducing", "entering", "chapter", "lineup",
    "line-up", "includes", "included", "including", "priced", "prices",
    "price", "point", "starting", "start", "select", "full", "future",
    "potential", "expansion", "expand", "expands", "nationwide", "restaurants",
    "restaurant", "through", "allows", "allow", "explore", "inform",
    "represents", "significant", "evolution", "zipporah", "allen", "chief",
    "commercial", "officer", "ability", "occasions", "occasion", "routines",
    "routine", "everyday", "post", "work", "lunches", "lunch", "people",
    "expect", "define", "defines", "staying", "true", "rooted", "commitment",
    "insights", "insight", "standards", "standard", "cooking", "scratch",
    "upgraded", "upgrade", "choose", "reasons", "reason", "bigger", "giving",
    "deliver", "delivers", "delivery", "portability", "satisfaction",
    "accessible", "variety", "support", "go", "fits", "fit", "base",
    "customer", "known", "introduced", "introducing", "relevance", "remaining","york", "los", "midwest", "angeles", "city", "sweetgreens","sweetgreencom", "below", "limited", "newest", "featuring","flavors", "familiar", "favorites", "fan-favorite", "takes","elevated", "designed", "expanding", "compromising", "unlocking","vary", "packed", "meals", "plates", "bowls", "salads", "chips","grams","classic","in-restaurants","white", "chopped", "crumbled","shaved", "layered", "lemon", "squeeze", "dressing", "salsa","rice", "crisps", "breadcrumbs","ingredients","club","food","bolder", "corn", "tortilla", "ranch", "salad", "green", "goddess","cheddar", "bacon","handheld", "portable"
}

clean_words = [word for word in words if word not in stopwords]
print("CLEANED:")
print(clean_words)

#Word Freq
word_freq = {}
for word in clean_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

#Top 10
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
top_10_sg_1 = sorted_words[:10]
print("\nTop 10 words:")
for word, count in top_10_sg_1:
    print(f"{word}: {count}")

#Unique Words
unique_words_sg_1 = set(clean_words)
print(f"Total words: {len(clean_words)}")
print(f"Unique words: {len(unique_words_sg_1)}")
print(sorted(unique_words_sg_1))



#SG 2
#Cleaning
def split_line(line):
    return line.replace('—', ' ').split()

def clean_word(word):
    return ''.join(char for char in word if char.isalpha() or char == '-').lower()

words = []
file_name = r"C:\Users\rhan1\Documents\OIM3640\oim3640\mini_projects\sweetgreen_2.txt"

with open(file_name, encoding="utf-8") as f:
    for line in f:
        for word in split_line(line):
            word = clean_word(word)
            if word:
                words.append(word)

print("ORIGINAL:")
print(words)

stopwords = {
    # basic english
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of",
    "with", "is", "it", "this", "that", "are", "was", "we", "our", "you",
    "be", "as", "its", "by", "from", "have", "has", "not", "so", "all",
    "they", "will", "more", "up", "out", "than", "can", "get", "do", "did",
    "were", "also", "just", "been", "which", "who", "how", "if", "us",
    "what", "when", "any", "make", "made", "going", "even", "their", "them",
    "these", "those", "some", "no", "too", "very", "there", "where", "would",
    "could", "should", "said", "only", "both", "much", "most", "own", "every",
    "each", "here", "while", "new", "one", "two", "three", "now", "across",
    "about", "into", "through", "without", "between", "around", "never",
    "always", "many", "back", "way", "ways", "well", "feel", "feels",
    # sweetgreen specific
    "sweetgreen", "sweetgreens", "function", "dr", "hyman", "mark",
    "jonathan", "neman", "co-founder", "chief", "medical", "officer",
    "executive", "collaboration", "menu", "launching", "available",
    "nationwide", "beginning", "january", "offered", "exclusively",
    "exclusive", "online", "store", "pickup", "delivery", "channels",
    "markets", "market", "select", "including", "atlanta", "florida",
    "boston", "designed", "developed", "informed", "intentionally",
    "aimed", "announced", "partnership", "partnering", "belief",
    "believes", "embodies", "celebrates", "reframes", "transforming",
    "proving", "showing", "bringing", "making", "setting", "building",
    "extending", "receive", "access", "app", "credit", "membership",
    "members", "rewards", "tracker", "visibility", "data", "driven",
    "personalized", "experience", "beyond", "education", "written",
    "translating", "helping", "understand", "diners", "guests", "people",
    "tangible", "desirable", "accessible", "intuitive", "satisfying",
    "simple", "joyful", "something", "endure", "enjoy", "return",
    "pursuit", "changes", "start", "year", "today", "idea", "campaign",
    "result", "based", "shaped", "selected", "thoughtfully", "genuinely",
    "deep", "respect", "decades", "insight", "principles", "biological",
    "foundational", "population", "nutrition", "nutrient", "nutrients",
    "complex", "information", "signal", "powerful", "power", "tool",
    "philosophy", "broader", "standard", "kind", "better", "right",
    "plate", "bowl", "bowls", "salad", "salads", "entrees", "entree",
    "online", "offers", "offer", "channels", "channel", "partner","functions", "shredded", "your", "added", "again", "aims", "allowed",
"anchored", "believed", "builds", "built", "bring", "change", "co-creating",
"cooking", "creativity", "culinary", "deliver", "different", "dish",
"easy", "eat", "enjoyment", "everyday", "expertise", "extends", "feature",
"first-of-its-kind", "flavors", "focus","greater", "help", "human", "in-app", "in-store", "inside","intention","keep", "key", "language", "like", "lives",
"love", "loves", "md", "meal", "meals", "multi-channel",
"name", "offering", "overall", "packed", "pairs", "provide", "reset","support", "supports", "tasted", "team", "together", "tools", "toward","turns", "weve", "whole", "wild", "wisdom", "work", "x", "data-driven","online-exclusive","lemon",
"squeeze", "chopped", "golden", "warm", "baby", "bodies", "body",
"colorful", "carbs","base","day", "energy", "garlic", "goddess", "green", "greens", "ranch","-","send"
}

clean_words = [word for word in words if word not in stopwords]
print("CLEANED:")
print(clean_words)

#Word Freq
word_freq = {}
for word in clean_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

#Top 10
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
top_10_sg_2 = sorted_words[:10]
print("\nTop 10 words:")
for word, count in top_10_sg_2:
    print(f"{word}: {count}")

#Unique Words
unique_words_sg_2 = set(clean_words)
print(f"Total words: {len(clean_words)}")
print(f"Unique words: {len(unique_words_sg_2)}")
print(sorted(unique_words_sg_2))


#Chobani
#Cleaning
def split_line(line):
    return line.replace('—', ' ').split()

def clean_word(word):
    return ''.join(char for char in word if char.isalpha() or char == '-').lower()

words = []
file_name = r"C:\Users\rhan1\Documents\OIM3640\oim3640\mini_projects\chobani.txt"

with open(file_name, encoding="utf-8") as f:
    for line in f:
        for word in split_line(line):
            word = clean_word(word)
            if word:
                words.append(word)

print("ORIGINAL:")
print(words)

stopwords = {
    # basic english
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of",
    "with", "is", "it", "this", "that", "are", "was", "we", "our", "you",
    "be", "as", "its", "by", "from", "have", "has", "not", "so", "all",
    "they", "will", "more", "up", "out", "than", "can", "get", "do", "did",
    "were", "also", "just", "been", "which", "who", "how", "if", "us",
    "what", "when", "any", "make", "made", "going", "even", "their", "them",
    "these", "those", "some", "no", "too", "very", "there", "where", "would",
    "could", "should", "said", "only", "both", "much", "most", "own", "every",
    "each", "here", "while", "new", "one", "two", "three", "now", "across",
    "about", "into", "through", "without", "between", "around", "never",
    "always", "many", "back", "way", "ways", "well", "feel", "feels",
    "has", "had", "than", "then", "when", "where", "why", "how",
    # chobani specific
    "chobani", "protein", "greek", "yogurt", "drinks", "drink", "cups",
    "cup", "line", "products", "product", "srp", "oz", "fl", "g", "grams",
    "gram", "serving", "servings", "single", "serve", "pack", "packaging",
    "available", "nationwide", "november", "january", "october", "retailers",
    "retailer", "new", "berlin", "prnewswire", "niel", "sandfort", "chief",
    "innovation", "office", "officer", "introducing", "expands", "expand",
    "expanding", "including", "includes", "include", "followed", "follow",
    "found", "find", "offer", "offers", "offering", "offerings", "options",
    "option", "choose", "choosing", "suite", "includes", "included",
    "combination", "combines", "combine", "using", "used", "use", "uses",
    "made", "make", "making", "crafted", "craft", "known", "originally",
    "addressing", "address", "introduces", "introduced", "next-generation",
    "beverage", "company", "food", "consumer", "consumers", "demand",
    "studies", "study", "show", "shows", "recent", "half", "prioritizing",
    "looking", "increase", "intake", "diets", "diet", "routines", "routine",
    "time", "times", "first", "good", "thing", "way", "place", "meet",
    "goals", "goal", "levels", "level", "formats", "format", "variety",
    "dynamic", "affordable", "solution", "deliver", "delivers", "thanks",
    "never", "easier", "complete", "ideal", "unlocking", "helping",
    "supporting", "seeking", "seek", "moved", "beyond", "made", "mainstream",
    "mindset", "shift", "underneath", "namely", "taking", "desire",
    "hardcode", "hardcore", "community", "calorie", "deprivation",
     "strength", "positive", "functional", "customizable",
    "convenient", "approach", "alternatives", "alternative", "sources",
    "source", "portable", "complete", "pressed", "wakeups", "pick-me-ups", "post-work", "morning", "afternoon", "early","next-generation","--", "-pack", "ny", "b", "go", "like", "other", "growing",
"meets", "keep", "full", "everyday", "flavors", "lineup",
"foods", "category", "accessible","animal", "beef", "chicken", "butter", "peanut", "soy",
"concentrates", "powders","process",
"yogurt-making", "occurring", "traditionally", "traditional",
"time-pressed", "higher-quality", "low", "lower", "added", "mixed", "ice", "cookies",
"punch", "tropical", "lemon", "raspberry", "kiwi", "mango",
"cherry", "peaches", "strawberry", "strawberries", "vanilla",
"cream", "berry","high"
}

clean_words = [word for word in words if word not in stopwords]
print("CLEANED:")
print(clean_words)

# Word Freq
word_freq = {}
for word in clean_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Top 10
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
top_10_chobani = sorted_words[:10]
print("\nTop 10 words:")
for word, count in top_10_chobani:
    print(f"{word}: {count}")

# Unique Words
unique_words_chobani = set(clean_words)
print(f"Total words: {len(clean_words)}")
print(f"Unique words: {len(unique_words_chobani)}")
print(sorted(unique_words_chobani))


#Visualizations
import matplotlib.pyplot as plt

def plot_top_10(top_words, brand_name):
    words = [word for word, count in top_words]
    counts = [count for word, count in top_words]

    plt.figure()
    plt.bar(words, counts)
    plt.title(f"Top 10 Words - {brand_name}")
    plt.xticks(rotation=45)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

plot_top_10(top_10_banana, "Baskin Robbins - Banana")
plot_top_10(top_10_dubai, "Baskin Robbins - Dubai Chocolate")
plot_top_10(top_10_mcd, "McDonald's")
plot_top_10(top_10_sg_1, "Sweetgreen 1")
plot_top_10(top_10_sg_2, "Sweetgreen 2")
plot_top_10(top_10_chobani, "Chobani")

