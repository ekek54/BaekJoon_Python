import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<File> files = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            files.add(new File(br.readLine()));
        }
        files.sort(File::compareTo);
        for (int i = 0; i < N; i++) {
            System.out.println(files.get(i));
        }
    }
    static class Number implements Comparable<Number>{
        public int[] nums;
        public String numStr = "";
        public int prefixZeroCnt;

        public Number(String numStr) {
            prefixZeroCnt = 0;
            boolean isPrefix = true;
            int startIdx = 0;
            for (int i = 0; i < numStr.length(); i++) {
                if (isPrefix) {
                    if (numStr.charAt(i) == '0') {
                        prefixZeroCnt++;
                    } else {
                        isPrefix = false;
                        startIdx = i;
                        nums = new int[numStr.length() - i];
                        this.numStr = numStr.substring(i);
                    }
                }
                if (!isPrefix) {
                    nums[i - startIdx] = Character.getNumericValue(numStr.charAt(i));
                }
            }
            if (isPrefix) {
                nums = new int[1];
                nums[0] = 0;
                this.numStr = "0";
            }
        }

        @Override
        public int compareTo(Number n) {
            if (nums.length != n.nums.length) {
                return this.nums.length - n.nums.length;
            }
            if (numStr.equals(n.numStr)) {
                return prefixZeroCnt - n.prefixZeroCnt;
            }
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == n.nums[i]) continue;
                return nums[i] - n.nums[i];
            }
            return 0;
        }

        @Override
        public String toString() {
            return numStr;
        }
    }

    static class Alphabet implements Comparable<Alphabet> {
        public char value;

        public Alphabet(char value) {
            this.value = value;
        }

        @Override
        public int compareTo(Alphabet a) {
            if (Character.toLowerCase(value) == Character.toLowerCase(a.value)) {
                return value - a.value;
            }
            return Character.toLowerCase(value) - Character.toLowerCase(a.value);
        }
    }

    static class Word implements Comparable<Word> {
        private Number numberValue = null;
        private Alphabet alphabetValue = null;

        public Word(Number value) {
            this.numberValue = value;
        }

        public Word(Alphabet value) {
            this.alphabetValue = value;
        }

        public boolean isNumber() {
            return alphabetValue == null;
        }

        public boolean isAlphabet() {
            return numberValue == null;
        }

        public Number getNumberValue() {

            return numberValue;
        }

        public Alphabet getAlphabetValue() {
            return alphabetValue;
        }

        @Override
        public int compareTo(Word w) {
            if (this.isNumber()) {
                if (w.isAlphabet()) return -1;
                return numberValue.compareTo(w.numberValue);
            }
            if (this.isAlphabet()) {
                if (w.isNumber()) return 1;
                return alphabetValue.compareTo(w.alphabetValue);
            }
            return 0;
        }
    }

    static class File implements Comparable<File>{
        public List<Word> words = new ArrayList<>();
        public String file = "";

        public File(String file) {
            this.file = file;
            StringBuilder nums = new StringBuilder();
            for (int i = 0; i < file.length(); i++) {
                if (Character.isAlphabetic(file.charAt(i))) {
                    if (nums.length() != 0) {
                        words.add(new Word(new Number(nums.toString())));
                        nums = new StringBuilder();
                    }
                    words.add(new Word(new Alphabet(file.charAt(i))));
                    continue;
                }
                nums.append(file.charAt(i));
            }
            if (nums.length() != 0) {
                words.add(new Word(new Number(nums.toString())));
            }
        }

        @Override
        public int compareTo(File f) {
            for (int i = 0; i < Math.min(words.size(), f.words.size()); i++) {
                int compared = words.get(i).compareTo(f.words.get(i));
                if (compared == 0) continue;
                return compared;
            }
            return words.size() - f.words.size();
        }

        @Override
        public String toString() {
            return file;
        }
    }
}
