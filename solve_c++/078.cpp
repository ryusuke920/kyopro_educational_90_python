#include <vector>
#include <iostream>
using namespace std;
int main(){
    int n, m;
    cin >> n >> m;
    vector<vector<int> > graph(n);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        a -= 1;
        b -= 1;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        int cnt = 0;
        for (int j : graph[i]) {
            if (j < i){
                ++cnt;
            }
        }
        if (cnt == 1) {
            ++ans;
        }
    }
    cout << ans << endl;
    return 0;
}