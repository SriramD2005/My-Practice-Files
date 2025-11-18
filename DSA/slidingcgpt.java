
    import java.util.*;
class slidingcgpt {
    public static int characterReplacement(String s, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        int l = 0, r = 0, res = 0, maxFreq = 0;

        while (r < s.length()) {
            int nch = s.charAt(r) - 'A';
            freq.put(nch, 1 + freq.getOrDefault(nch, 0)); // Update frequency map
            maxFreq = Math.max(maxFreq, freq.get(nch)); // Track the max frequency of any character

            // Check if the window is valid
            if ((r - l + 1) - maxFreq > k) {
                int leftChar = s.charAt(l) - 'A';
                freq.put(leftChar, freq.get(leftChar) - 1); // Decrement frequency of the left character
                l++; // Shrink the window
            }

            res = Math.max(res, r - l + 1); // Update the result with the maximum valid window size
            r++; // Expand the window
        }

        return res;
    }

    public static void main(String[] args) {
        String s = "AABABBA";
        System.out.println(slidingcgpt.characterReplacement(s, 1)); // Output: 4
    }
}

