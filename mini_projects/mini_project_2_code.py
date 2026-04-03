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
print(words)
stopwords = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "is", "it", "this", "said", "that", "are", "was","we", "our", "you", "thats","every", "your", "be", "bananas","even", "as", "its", "by", "from","have", "has", "not", "made","so", "all", "their","going", "they", "will","at", "make","more", "up", "out", "about", "into", "than", "can", "throughout", "get","what", "when", "which", "who", "how", "if", "us", "also","just", "been", "do", "did", "were", "him", "her", "his","march", "wednesday", "baskinrobbins", "baskin-robbins", "baskin", "robbins", "participating", "locations", "nationwide","limited", "time", "beginning", "available", "members", "member",
"rewards", "br", "app", "access", "deal", "unlock", "exclusive","benefits", "invited", "celebrate", "throughout", "join", "added",
"treat", "introducing", "sure", "send", "anyone", "totally","keeps", "coming", "back", "nicole", "boutwell", "vice", "president","culinary", "marketing", "enjoy", "de"}
clean_words = [word for word in words if word not in stopwords]
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
top_10 = sorted_words[:10] #only gets tuples from index 0-9
print("\nTop 10 words:")
for word, count in top_10:
    print(f"  {word}: {count}")

#Unique Words 
#Use a set bcz gets rid of duplicates and can see uniqueness 
#If a brand uses a lot of different words i.e. high unique word count, a lot of variety
#If a brand uses the same words over and over again, low unique word count 
unique_words = set(clean_words)
print(f"Total words:{len(clean_words)}")
print(f"Unique words: {len(unique_words)}")
print(sorted(unique_words))