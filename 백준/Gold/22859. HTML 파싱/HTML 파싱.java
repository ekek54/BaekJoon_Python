import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    static String HTML;

    public static void main(String[] args) throws IOException {
        init();
        Body body = new Body(HTML);
        System.out.print(body);
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HTML = br.readLine();
    }

    static class Body {
        private final String content;

        Body(String content) {
            this.content = content;
        }

        public List<Paragraph> parseContent() {
            return Arrays.stream(content.replaceAll("</?main>", "").split("</div>")).map(Paragraph::new).collect(Collectors.toList());
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            List<Paragraph> paragraphs = parseContent();
            for (Paragraph paragraph : paragraphs) {
                sb.append("title : ").append(paragraph);
            }
            return sb.toString();
        }
    }

    static class Paragraph {
        private final String content;
        private final String title;

        public Paragraph(String paragraph) {
            this.content = paragraph.replaceFirst("<div title=\"[a-zA-Z_0-9 ]+\">", "");
            this.title = paragraph.split("\"")[1];
            if (title.length() == 0) throw new NullPointerException();
            ;
        }

        public List<Sentence> parseContent() {
            return Arrays.stream(content.split("</?p>")).filter(s -> s.length() > 0).map(Sentence::new).collect(Collectors.toList());
        }

        @Override
        public String toString() {
            List<Sentence> sentences = parseContent();
            StringBuilder sb = new StringBuilder();
            sb.append(title).append("\n");
            for (Sentence sentence : sentences) {
                sb.append(sentence).append("\n");
            }
            return sb.toString();
        }
    }

    static class Sentence {
        private final String content;

        public Sentence(String content) {
            this.content = content;
        }

        public String parseContent() {
            return content.replaceAll("<[a-z/ ]*>", "") // 내부 태그 제거
                    .strip()                                            // 문장 시작과 끝 공백 제거
                    .replaceAll(" +", " ");           // 연속 공백 하나로
        }

        @Override
        public String toString() {
            return parseContent();
        }
    }
}
