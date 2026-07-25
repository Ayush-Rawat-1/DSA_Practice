import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {

    public static void solve(BufferedReader br) throws IOException {
        String[] line1 = br.readLine().trim().split("\\s+");
        int n = Integer.parseInt(line1[0]);
        int q = Integer.parseInt(line1[1]);

        String[] arrStr = br.readLine().trim().split("\\s+");
        
        // nums[i][0] = value, nums[i][1] = original_index
        int[][] nums = new int[n][2];
        for (int i = 0; i < n; i++) {
            nums[i][0] = Integer.parseInt(arrStr[i]);
            nums[i][1] = i;
        }

        // Read and ignore the queries
        for (int i = 0; i < q; i++) {
            br.readLine();
        }

        // Sort 2D array based on values (first column)
        Arrays.sort(nums, (a, b) -> Integer.compare(a[0], b[0]));

        int res = 0;
        for (int i = 0; i < n; i++) {
            int j = nums[i][1];
            if (i == j) continue;

            for (int b = 20; b >= 0; b--) {
                int x = 1 << b;
                if ((i & x) != (j & x)) {
                    res = Math.max(res, x);
                    break;
                }
            }
        }

        System.out.println(res);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;

        int t = Integer.parseInt(line.trim());
        while (t-- > 0) {
            solve(br);
        }
    }
}
