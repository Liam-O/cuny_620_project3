import re
import string
from textstat.textstat import textstat

def get_features(name, feat_num = range(1,10)):
    '''
    Parameters:
        name - string of name to extract feature
        feat_num - itterable colleciton of integers specifying features. *Defaults to 1:9 inclusive
            1: last letter
            2: first letter
            3: Vowel counts
            4: Hard consonant count
            5: Soft consonant count
            6: Syllable Count
            7: Name length
            8: Last two chars
            9: Last three chars
            10: char count --> feature for all alpha chars
            11: char present --> feature for all alpha chars (boolean)
    Returns:
        features: a dictionary of extracted features
    '''
    features = {}
    
    # Converts feat_num to itterable if type is int
    if type(feat_num) is int:
        feat_num = (0, feat_num)        
   
    # Gender Feature 1: Last letter - book example
    if 1 in feat_num:
        features['last_letter'] = name[-1].lower()
        
    # Gender Feature 2: First letter - most names beginning with a vowel --> females
    if 2 in feat_num:
        features['first_letter'] = name[0].lower()
        
    # Gender Feature 3: Vowel Counts
    if 3 in feat_num:
        features['vowel_count'] = len(re.sub(r'[^aeiou]', '', name.lower()))
        
    # Gender Feature 4: Hard consonants using general rules of c and g
    if 4 in feat_num:
        features['hard_consts'] = len(re.findall(r'[cg][^eiy]', name.lower()))/2
        
    # Gender Feature 5: Soft consonants using general rules of c and g
    if 5 in feat_num:
        features['soft_consts'] = len(re.findall(r'[cg][eiy]', name.lower()))/2
        
    # Gender Feature 6: Syllable Count of names via textstat
    if 6 in feat_num:
        features['syllable_count'] = textstat.syllable_count(name.lower())

    # Gender Feature 7: Name length
    if 7 in feat_num:
        features["length"] = len(name)
    
    # Gender Feature 8: Last two chars
    if 8 in feat_num:
        features["last2letters"] = name[-2:].lower()
        
    # Gender Feature 9: Last three chars
    if 9 in feat_num:
        features["last3letters"] = name[-3:].lower()

    # Gender Feature 10: Char Counts (overfitts)
    if 10 in feat_num:
        for letter in string.ascii_lowercase:
            features["count_{0}".format(letter)] = name.lower().count(letter)
            
    # Gender Feature 11: Char Booleans (overfitts)
    if 11 in feat_num:
        for letter in string.ascii_lowercase:
            features["has_{0}".format(letter)] = letter in name.lower()
                                                       
    return features