#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> books(n);
  map<int, int> aux;
  for (int i = 0; i < n; i++) {
    cin >> books[i];
    aux[books[i]] = i;
  }
  vector<int> order(n);
  for (int i = 0; i < n; i++) {
    cin >> order[i];
  }
  stack<int> s;
  for (int i = n - 1; i > -1; i--) {
    s.push(books[i]);
  }
  for (int i = 0; i < n; i++) {
    int cnt = 0;
    while (!s.empty()) {
      if (aux[order[i]] < aux[s.top()]) {
        break;
      }
      s.pop();
      cnt++;
    }
    cout << cnt << " ";
  }
  cout << endl;
  return 0;
}
