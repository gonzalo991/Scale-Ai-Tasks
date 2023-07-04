/**
 ### **Concept to cover**  (this is what your task must be about):

**High Level**: Algorithms and Data Structures

**Category**:  
Hashing

**Topic**:  
Chaining
 */

// 1.  can you explain this code ?  

import java.util.ArrayList;  
import java.util.HashMap;  
import java.util.List;  
import java.util.Map;

public class SpellChecker {  
private Map<String, List> dictionary;


public SpellChecker() {
    dictionary = new HashMap<>();
}

public void addToDictionary(String word) {
    String key = getHashKey(word);
    if (!dictionary.containsKey(key)) {
        dictionary.put(key, new ArrayList<>());
    }
    dictionary.get(key).add(word);
}

public List<String> getSuggestions(String prefix) {
    String key = getHashKey(prefix);
    if (dictionary.containsKey(key)) {
        return dictionary.get(key);
    }
    return new ArrayList<>();
}

private String getHashKey(String word) {
    return String.valueOf(word.charAt(0)).toLowerCase();
}

public static void main(String[] args) {
    SpellChecker spellChecker = new SpellChecker();

    // Add some words to the dictionary
    spellChecker.addToDictionary("apple");
    spellChecker.addToDictionary("banana");
    spellChecker.addToDictionary("cat");
    spellChecker.addToDictionary("dog");
    spellChecker.addToDictionary("elephant");
    spellChecker.addToDictionary("fish");

    // Get suggestions for a prefix
    String prefix = "a";
    List<String> suggestions = spellChecker.getSuggestions(prefix);
    System.out.println("Suggestions for prefix '" + prefix + "': " + suggestions);
}
}

/**
Here’s an explanation of the code snippet for a spell checking and auto-complete system in Java:
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpellChecker {
    private Map<String, List<String>> dictionary;

    public SpellChecker() {
        dictionary = new HashMap<>();
    }

    public void addToDictionary(String word) {
        String key = getHashKey(word);
        if (!dictionary.containsKey(key)) {
            dictionary.put(key, new ArrayList<>());
        }
        dictionary.get(key).add(word);
    }

    public List<String> getSuggestions(String prefix) {
        String key = getHashKey(prefix);
        if (dictionary.containsKey(key)) {
            return dictionary.get(key);
        }
        return new ArrayList<>();
    }

    private String getHashKey(String word) {
        return String.valueOf(word.charAt(0)).toLowerCase();
    }

    public static void main(String[] args) {
        SpellChecker spellChecker = new SpellChecker();

        // Add some words to the dictionary
        spellChecker.addToDictionary("apple");
        spellChecker.addToDictionary("banana");
        spellChecker.addToDictionary("cat");
        spellChecker.addToDictionary("dog");
        spellChecker.addToDictionary("elephant");
        spellChecker.addToDictionary("fish");

        // Get suggestions for a prefix
        String prefix = "a";
        List<String> suggestions = spellChecker.getSuggestions(prefix);
        System.out.println("Suggestions for prefix '" + prefix + "': " + suggestions);
    }
}

/**
Description:

1.  The SpellChecker class represents a system for checking spelling and autocompleting. To store words, 
it uses a HashMap called a dictionary.
2.  An empty dictionary is initialised by the constructor.
3.  The method addToDictionary takes a word as input. It adds the word to the dictionary. 
It uses the getHashKey method to calculate the hash key for the word.
4.  A new entry is created with an empty list if the hash key does not exist in the dictionary. Then the 
word is added to the list that corresponds to the hash key of the word.
5.  getSuggestions takes a prefix and returns a list of suggestions for words beginning with that prefix. It uses 
the getHashKey method to calculate the hash key for the prefix.
6.  The method returns the corresponding list of words if the dictionary contains the hash key. If not, it will 
return an empty list.
7.  The getHashKey method takes a word as input. It returns its hash key. The hash key is the first lowercase 
character of the word in this code.
8.  We create an instance of SpellChecker called spellChecker in the main method.
9.  Using the addToDictionary method, we add some words to the dictionary.
10.  To get a list of suggestions for words that begin with that prefix, we specify a prefix, “a”, and call 
the getSuggestions method.
11.  Lastly, we print the suggestions to the console.

Using chaining in hashing, this code provides a basic implementation of a spell-checking and autocomplete 
system. It is important to note that real spellchecking and autocomplete systems are typically more complex, involving 
additional components such as language models, efficient data structures, and advanced algorithms for improved accuracy 
and performance.
*/

// 2.  What data structure is used to implement the dictionary in this code?

/*
The dictionary is implemented using a HashMap<String, List> in the SpellChecker class.

A HashMap is a data structure in which the elements are stored as pairs of keys and values. The key is a 
character string representing the hashkey for each word, and the value is a list of character strings representing 
the word associated with each hashkey.

The HashMap provides an efficient way of searching for and retrieving values on the basis of their keys. Internally, 
hashing techniques are used to determine the location of each key/value pair, allowing fast access to the value by its key.

In code it is declared as a HashMap with a key type string and a value type list. Each tag represents one hashtag 
for words, while the corresponding values are lists of words that share the same hashtag.

When you add a word to the dictionary using the addToDictionary method, it computes the hashed key of the word, 
and if the hashed key doesn’t exist in the hashmap, it creates a new entry with an empty list as its values. The 
word is appended to the existing list of words associated with that key if the hash key already exists.

This implementation allows effective storage and recall of words based on their hashed key, allowing quick access 
to words with similar first letters.
*/



// 3.  How are words added to the dictionary in the code?


/*
The words are added to the dictionary using the addToDictionary method. The addToDictionary method takes a 
word as input and adds the word to the dictionary.

The method first computes the hash key of the word using the getHashKey method. The hash key is the first 
lowercase character of the word.

Next, the method checks if the hash key exists in the dictionary. If the hash key does not exist in the dictionary, 
the method creates a new list for the hash key and adds the word to the list. If the hash key already exists in the 
dictionary, the method appends the word to the list of words already associated with that hash key.

Finally, the method returns void.
*/
public void addToDictionary(String word) {
    String key = getHashKey(word);
    if (!dictionary.containsKey(key)) {
        dictionary.put(key, new ArrayList<>());
    }
    dictionary.get(key).add(word);
}

/*

In the addToDictionary method of the SpellChecker class, words are added to the dictionary using the following steps:

1.  The method takes a word as input.
2.  The getHashKey method is called, passing the word as an argument, to calculate the hash key for the word. The 
hash key represents the initial character of the word.
3.  The method checks if the dictionary contains the calculated hash key.
4.  If the hash key is not present in the dictionary, it means there are no words associated with that hash key yet. In 
this case, a new entry is created in the dictionary with the hash key as the key and an empty ArrayList as the value.
*/

if (!dictionary.containsKey(key)) {
    dictionary.put(key, new ArrayList<>());
}
/*

5.  If the hash key is already present in the dictionary, it means there are words associated with that hash key. In this case, the method retrieves the existing list of words associated with the hash key from the dictionary.
6.  The word is then added to the retrieved list of words.

*/
dictionary.get(key).add(word);

/*

7.  Finally, the updated list of words is put back into the dictionary with the hash key as the key, effectively 
updating the entry in the dictionary with the new word added.

By following these steps, words are added to the dictionary using the chaining technique in hashing. Words with
 the same hash key are stored in the same list, allowing for efficient retrieval and organization of words based 
 on their initial characters.
*/

// 4.  How does the getSuggestions method retrieve suggestions in this code?


/*
The getSuggestions method uses the hash key of the prefix to retrieve suggestions from the dictionary.

The getSuggestions method takes a prefix as input and returns a list of suggestions for words that begin with that prefix.

The method first computes the hash key of the prefix using the getHashKey method. The hash key is the first lowercase character of the prefix.

Next, the method checks if the hash key exists in the dictionary. If the hash key exists in the dictionary, the method returns the list of words associated with the hash key as suggestions.

If the hash key does not exist in the dictionary, the method returns an empty list.
*/

public List<String> getSuggestions(String prefix) {
    String key = getHashKey(prefix);
    if (dictionary.containsKey(key)) {
        return dictionary.get(key);
    }
    return new ArrayList<>();
}

/*
The getHashKey method is used to calculate the hash key of the prefix, which is the first lowercase character of the prefix.

The containsKey method is called on the dictionary, passing in the hash key as an argument, to check if the hash key exists in the dictionary.

If the hash key exists in the dictionary, the get method is called on the dictionary, passing in the hash key as an argument, to retrieve the list of words associated with the hash key. This list is then returned as suggestions.

If the hash key does not exist in the dictionary, an empty list is returned.

The SpellChecker’s getSuggestions method retrieves suggestions for a given prefix as follows:

1.  The getSuggestions method takes a prefix and initialises an empty ArrayList called suggestions for storing suggestions.
2.  To calculate the hash key for the prefix, the getHashKey method is called with the prefix as an argument. The first character of the prefix is represented by this hash key.
3.  Using the containsKey method, the method checks whether the dictionary contains the calculated hash key.
4.  If the hashkey is present in the dictionary, it means that there are words associated with that hashkey that might have the same prefix.
5.  Using the get method, the method retrieves the list of words associated with the hash key.
6.  Each word in the list of words associated with the hash key is iterated over in a loop.
7.  For each word, the method uses the startsWith method to check whether the word starts with the prefix that was given. If the word starts with the given prefix, it is considered as suggested and is added to the suggested list using the add method.
8.  Finally, the suggestion list will be returned with the list of suggestion words.

In summary, the getSuggestions method uses the hash key of the prefix to retrieve suggestions from the dictionary. If the hash key exists in the dictionary, the method returns the list of words associated with the hash key as suggestions. If the hash key does not exist in the dictionary, the method returns an empty list.
*/


// 5.  How is the getHashKey method implemented to calculate the hash key for a word in the code?


//The getHashKey method is implemented using the following code:

private String getHashKey(String word) {
    if (word.isEmpty()) {
        return "";
    }
    return String.valueOf(word.charAt(0)).toLowerCase();
}

/*
The method takes a word as input and returns its hash key. The hash key is the first lowercase character of the word.

The String.valueOf method is used to convert the character to a string. The lowercase method is used to convert the first character of the word to lowercase to make it consistent with the other keys in the dictionary.

Explanation of the method:

1.  A word is taken as input to the getHashKey method.
2.  Using the isEmpty method, the method first checks whether the word is empty. An empty string is returned as the hash key if the word is empty.
3.  The charAt(0) method is used to extract the first character of the word if the word is not empty.
4.  To ensure case-insensitive hashing, the first character is then converted to lowercase using the toLowerCase method.
5.  The valueOf method is used to convert the first lowercase character to a string.
6.  Finally, the hash key is returned as the lowercase first character, now represented as a string.

With this procedure, the getHashKey method computes the hash key for a given word, extracting its first character, converting it to lowercase and returning it as a string. This hash key represents the first character of the word. It is used to organise words in the dictionary according to their first characters.
*/