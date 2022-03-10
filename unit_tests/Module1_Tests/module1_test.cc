#include "module1.hpp"

#include "gtest/gtest.h"

using namespace std;
using namespace gcc10_failure;

TEST(Module1Test, can_sayHello) {
  auto expected = string("Hello World!");
  auto tested = sayHello();

  EXPECT_EQ(tested, expected);
}