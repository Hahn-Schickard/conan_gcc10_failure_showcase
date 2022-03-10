#include "module2.hpp"

#include "module1.hpp"

#include <iostream>

using namespace std;

namespace gcc10_failure {
void greet() { cout << sayHello() << endl; }
} // namespace gcc10_failure
