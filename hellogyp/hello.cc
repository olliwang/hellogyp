// Copyright 2014 Ollix
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// ---
// Author: olliwang@ollix.com (Olli Wang)

#include "hellogyp/hello.h"

namespace hellogyp {

Hello::Hello() {}

Hello::~Hello() {}

std::string Hello::GetGreetingMessage() const {
  // Uses the `auto` keyword to make sure C++11 is supported.
  auto greetings = std::string("Hello GYP!");
  return greetings;
}

}  // namespace hellogyp
