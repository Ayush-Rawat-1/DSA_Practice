import java.io.*;
import java.util.*;

public class Main {
    public static void solve(int n, int m, int[][] edges, PrintWriter out) {
        ArrayList<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        int[][] dis = new int[n][2];
        for (int i = 0; i < m; i++) {
            int o = edges[i][0];
            int u = edges[i][1];
            int v = edges[i][2];
            
            graph[u].add(new int[]{v, o});
            graph[v].add(new int[]{u, o});
            
            dis[u][o]++;
            dis[v][o]++;
        }

        ArrayDeque<Integer> q = new ArrayDeque<>();
        boolean[] vis = new boolean[n];
        for (int u = 0; u < n; u++) {
            if (dis[u][0] == 0 || dis[u][1] == 0) {
                vis[u] = true;
                q.offer(u);
            }
        }

        int[][] order = new int[n][2];
        int idx = 0;

        while (!q.isEmpty()) {
            int u = q.pollFirst();
            order[idx][0] = u;
            
            if (dis[u][0] == 0) {
                order[idx][1] = -1;
            } else {
                order[idx][1] = 1;
            }
            idx++;

            for (int i = 0; i < graph[u].size(); i++) {
                int[] edge = graph[u].get(i);
                int v = edge[0];
                int o = edge[1];
                
                if (--dis[v][o] == 0 && !vis[v]) {
                    vis[v] = true;
                    q.offer(v);
                }
            }
        }

        if (idx != n) {
            out.println("NO");
            return;
        }

        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            int revIdx = n - i - 1;
            res[order[revIdx][0]] = (i + 1) * order[revIdx][1];
        }
        
        out.println("YES");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(res[i]).append(i == n - 1 ? "" : " ");
        }
        out.println(sb.toString());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        
        while (t-- > 0) {
            while (!st.hasMoreTokens()) {
                st = new StringTokenizer(br.readLine());
            }
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            
            int[][] edges = new int[m][3];
            for (int i = 0; i < m; i++) {
                while (!st.hasMoreTokens()) {
                    st = new StringTokenizer(br.readLine());
                }
                edges[i][0] = Integer.parseInt(st.nextToken()) - 1; // o
                edges[i][1] = Integer.parseInt(st.nextToken()) - 1; // u
                edges[i][2] = Integer.parseInt(st.nextToken()) - 1; // v
            }
            solve(n, m, edges, out);
        }
        out.flush();
    }
}
