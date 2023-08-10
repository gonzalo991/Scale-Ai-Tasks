import java.util.*;

public class WordFrequency {

// Function to calculate word frequency in a given input string
public static Map<String, Integer> calculateWordFrequency(String input) {
Map<String, Integer> frequencyMap = new HashMap<>();
String[] words = input.split("\\s+"); // Split the input string into words using spaces as delimiters

for (String word : words) {
word = word.toLowerCase(); // Convert word to lowercase to count words case-insensitively
frequencyMap.put(word, frequencyMap.getOrDefault(word, 0) + 1); // Count occurrences of each word
}

return frequencyMap;
}

// Function to find the most frequent word in the given frequency map
public static Map.Entry<String, Integer> mostFrequentWord(Map<String, Integer> frequencyMap) {
Map.Entry<String, Integer> mostFrequentEntry = null;

for (Map.Entry<String, Integer> entry : frequencyMap.entrySet()) {
if (mostFrequentEntry == null || entry.getValue() > mostFrequentEntry.getValue()) {
mostFrequentEntry = entry; // Update mostFrequentEntry if a higher frequency is found
}
}

return mostFrequentEntry;
}

public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);

System.out.print("Enter a string: ");
String input = scanner.nextLine(); // Read user input

Map<String, Integer> frequencyMap = calculateWordFrequency(input); // Calculate word frequency

System.out.println("Frequency Map: " + frequencyMap); // Print word frequency map

Map.Entry<String, Integer> mostFrequent = mostFrequentWord(frequencyMap); // Find most frequent word
System.out.println("Most Frequent Word: " + mostFrequent.getKey());
System.out.println("Frequency of Most Frequent Word: " + mostFrequent.getValue());
}
}