#include <bits/stdc++.h>

#define N 100005

using namespace std;

int n;
int lca[N][20], depth[N];

void gen_test_01() {
    ofstream fo("01");
    n = 100000;
    fo << n << "\n" << 0 << " ";
    for (int i = 2; i <= n; i++) {
        fo << 1LL * rand() * rand() % (i - 1) + 1 << " ";
    }
    fo << "\n" << n << "\n";
    for (int i = 0; i < n; i++) {
        int u = 1LL * rand() * rand() % n + 1;
        int v = 1LL * rand() * rand() % n + 1;
        while (u == v) {
            u = 1LL * rand() * rand() % n + 1;
            v = 1LL * rand() * rand() % n + 1;
        }
        fo << u << " " << v << "\n";
    }
    fo.close();
}

void gen_test_02() {
    ofstream fo("02");
    n = 100000;
    fo << n << "\n" << 0 << " ";
    for (int i = 2; i <= n; i++) {
        if (rand() % 500 == 0) {
            fo << 1LL * rand() * rand() % (i - 1) + 1 << " ";
        }
        else {
            fo << i - 1 << " ";
        }
    }
    fo << "\n" << n << "\n";
    for (int i = 0; i < n; i++) {
        int u = 1LL * rand() * rand() % n + 1;
        int v = 1LL * rand() * rand() % n + 1;
        while (u == v) {
            u = 1LL * rand() * rand() % n + 1;
            v = 1LL * rand() * rand() % n + 1;
        }
        fo << u << " " << v << "\n";
    }
    fo.close();
}

int getLCA(int u, int v) {
    if (depth[u] > depth[v]) {
        swap(u, v);
    }
    int d = depth[v] - depth[u];
    for (int i = 19; i >= 0; i--) {
        if ((d >> i) & 1) {
            v = lca[v][i];
        }
    }
    if (u == v) {
        return u;
    }
    for (int i = 19; i >= 0; i--) {
        if (lca[u][i] != lca[v][i]) {
            v = lca[v][i];
            u = lca[u][i];
        }
    }
    return lca[u][0];
}

int main() {
    // gen_test_02();
    // return 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> lca[i][0];
        depth[i] = depth[lca[i][0]] + 1;
    }
    for (int i = 1; i < 20; i++) {
        for (int u = 1; u <= n; u++) {
            lca[u][i] = lca[lca[u][i - 1]][i - 1]; 
        }
    }
    int q;
    cin >> q;
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << getLCA(u, v) << "\n";
    }
}
/*
8
0 1 1 2 2 2 3 3
2
4 7
4 6
    addEdge(1,2);
    addEdge(1,3);
    addEdge(2,4);
    addEdge(2,5);
    addEdge(2,6);
    addEdge(3,7);
    addEdge(3,8);
*/