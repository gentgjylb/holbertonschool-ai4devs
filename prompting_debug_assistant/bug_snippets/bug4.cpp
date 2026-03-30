#include <iostream>
#include <vector>

int sumUpTo(const std::vector<int>& values) {
    int sum = 0;
    for (size_t i = 0; i <= values.size(); ++i) {
        sum += values[i];
    }
    return sum;
}

int main() {
    std::vector<int> data = {1, 2, 3, 4};
    std::cout << "Sum: " << sumUpTo(data) << std::endl;
    return 0;
}
