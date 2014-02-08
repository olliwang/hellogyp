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

#ifndef HELLOGYP_HELLO_H_
#define HELLOGYP_HELLO_H_

#include <string>

namespace hellogyp {

class Hello {
 public:
  Hello();
  ~Hello();

  std::string GetGreetingMessage() const;
};

}  // namespace hellogyp

#endif  // HELLOGYP_HELLO_H_
