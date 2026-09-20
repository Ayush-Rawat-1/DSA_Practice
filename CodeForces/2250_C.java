import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        String line = reader.readLine();
        if (line == null) return;
        int t = Integer.parseInt(line.trim());

        StringBuilder out = new StringBuilder();

        while (t-- > 0) {
            line = reader.readLine();
            while (line != null && line.trim().isEmpty()) {
                line = reader.readLine();
            }
            if (line == null) break;

            int n = Integer.parseInt(line.trim());
            int[][] queries = new int[n][4];

            for (int i = 0; i < n; i++) {
                tokenizer = new StringTokenizer(reader.readLine());
                queries[i][0] = Integer.parseInt(tokenizer.nextToken()) - 1; // l
                queries[i][1] = Integer.parseInt(tokenizer.nextToken()) - 1; // r
                queries[i][2] = Integer.parseInt(tokenizer.nextToken()) - 1; // u
                queries[i][3] = Integer.parseInt(tokenizer.nextToken()) - 1; // v
            }

            solve(n, queries, out);
        }

        System.out.print(out);
    }

    private static void solve(int n, int[][] queries, StringBuilder out) {
        int res = 0;

        for (int i = n; i >= 1; i--) {
            if (go(i, n, queries)) {
                res = i;
                break;
            }
        }

        out.append(res).append("\n");
    }

    private static boolean go(int m, int n, int[][] queries) {
        int curr = 0;

        for (int i = 0; i < n; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            int u = queries[i][2];
            int v = queries[i][3];

            if ((l <= curr && curr <= r) || (u <= (m - 1 - curr) && (m - 1 - curr) <= v)) {
                continue;
            }

            curr++;
            if (curr == m) {
                return true;
            }
        }

        return curr >= m;
    }
}
