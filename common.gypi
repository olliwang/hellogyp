# Copyright 2014 Ollix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
{
  'conditions': [
    ['OS=="mac" and "<(GENERATOR)"=="ninja"', {
      'make_global_settings': [
        ['CC', '/usr/bin/clang'],
        ['CXX', '/usr/bin/clang++'],
      ],
    }],  # OS=="mac" and "<(GENERATOR)"=="ninja"
    ['"<(GENERATOR)"=="xcode" and (OS=="mac" or OS=="ios")', {
      'conditions': [
        ['OS=="ios"', {
          'xcode_settings': {
            'CODE_SIGN_IDENTITY[sdk=iphoneos*]': 'iPhone Developer',
            'SDKROOT': 'iphoneos',  # -isysroot
            'TARGETED_DEVICE_FAMILY': '1,2',  # creates universal app
          },
        }],  # OS=="ios"
        ['OS=="mac"', {
          'xcode_settings': {
            'SDKROOT': 'macosx',  # -isysroot
          },
        }],  # OS=="mac"
      ],
      'xcode_settings': {
        'CLANG_ENABLE_OBJC_ARC': 'YES',  # enables ARC
        'CONFIGURATION_BUILD_DIR': 'build/Xcode',
      },  # xcode_settings
    }],  # OS=="mac" or OS="ios"
  ],  # conditions
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'cflags': [
          '-g',
          '-O0',
        ],
        'defines': [
          'DEBUG',
        ],
        'conditions': [
          ['"<(GENERATOR)"=="xcode"', {
            'xcode_settings': {
              'GCC_OPTIMIZATION_LEVEL': '0',
              'ONLY_ACTIVE_ARCH': 'YES',
            },
          }],
        ],  # "<(GENERATOR)"=="xcode"
      },  # Debug
      'Release': {
        'cflags': [
          '-Os',
        ],
        'defines': [
          'NDEBUG',
        ],
        'conditions': [
          ['"<(GENERATOR)"=="xcode"', {
            'xcode_settings': {
              'GCC_OPTIMIZATION_LEVEL': 's',
            },
          }],
        ],  # "<(GENERATOR)"=="xcode"
      }  # Release
    },  # configurations
  },  # target_defaults
}
