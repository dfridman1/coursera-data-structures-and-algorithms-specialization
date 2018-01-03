#include <iostream>
#include <vector>


const int p = 1000000007;
const int x = 263;


int polynomial_hash(std::string::const_iterator start, std::string::const_iterator end) {
    unsigned long long hash = 0;
    while (start != end) {
        hash = (*(--end) + x*hash) % p;
    }
    return (int)hash;
}


std::vector<int> precompute_hashes(const std::string &s, int n) {
    int k = (int)s.size()-n+1;
    std::vector<int> hashes(k, 0);
    if (k < 1) return hashes;
    int i = k-1;
    hashes[i] = polynomial_hash(s.begin()+i, s.begin()+i+n);
    long long y = 1;
    for (int j = 0; j < n; j++) {
        y = (y*x) % p;
    }
    while (--i >= 0) {
        hashes[i] = (p + (s[i] + x*(long long)hashes[i+1] - s[i+n]*y) % p) % p;
    }
    return hashes;
}


void show_vector(const std::vector<int> &v) {
    for (int x : v) {
        printf("%d ", x);
    }
    printf("\n");
}


std::vector<int> robin_karp(const std::string &pattern, const std::string &text) {
    std::vector<int> shifts;
    std::vector<int> hashes = precompute_hashes(text, (int)pattern.size());
    int pattern_hash = polynomial_hash(pattern.begin(), pattern.end());
    for (int i = 0; i < text.size()-pattern.size()+1; i++) {
      if ((hashes[i] == pattern_hash) & std::equal(text.begin()+i, text.begin()+i+pattern.size(), pattern.begin())) {
        shifts.push_back(i);
      }
    }
    return shifts;
}


int main() {
    std::string pattern, text;
    std::cin >> pattern >> text;
    show_vector(robin_karp(pattern, text));
    return 0;
}
