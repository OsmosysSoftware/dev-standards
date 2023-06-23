# Angular Coding Standards

## Coding Style Guide

We at osmosys follow all the conding standards mentioned here - https://angular.io/guide/styleguide

## Security 

These are the standard built in protections we should be practicing against common web-application vulnerabilities and attacks such as cross-Standard scripting attacks - https://angular.io/guide/security

## Standard Enforcing Tools

ESLint, Prettier

## **Set up ESlint for Angular, Typescript(AirBnB rules), Prettier**

### **Base Requirements:**

1. Node.js & npm
2. Angular CLI
3. Visual Studio Code

### **Pre-requisite Visual Studio Extensions**

1. ESlint: [Download Eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
2. Prettier: [Download Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

### **npm commands**

In root directory of project:

1. npx install-peerdeps --dev eslint-config-airbnb-base
2. npm install eslint-config-airbnb-typescript @typescript-eslint/eslint-plugin@^5.13.0 @typescript-eslint/parser@^5.0.0 --save-dev
3. npm init @eslint/config
4. npm install eslint-plugin-import --save-dev
5. npm i prettier eslint-config-prettier --save-dev
9. ng add @angular-eslint/schematics
10. ng lint

### **`.eslintrc.json`**

```json
{
  "root": true,
  "ignorePatterns": [
    "projects/**/*"
  ],
  "overrides": [
    // Angular ESLint for Typescript files
    {
      "files": [
        "*.ts"
      ],
      "env": {
        "browser": true,
        "es2021": true,
        "node": true
      },
      "extends": [
        // Airbnb's typescript rules
        "airbnb-base",
        "airbnb-typescript/base",
        // Prettier Latest
        "prettier",
        // import file to remove errors
        "plugin:import/recommended",
        // Angular rules
        "plugin:@angular-eslint/recommended"
      ],
      "overrides": [],
      "parserOptions": {
        "parser": "@typescript-eslint/parser",
        "ecmaVersion": "latest",
        "project": [
          "./tsconfig.eslint.json",
          "e2e/tsconfig.json",
          "./tsconfig.json"
        ]
      },
      "rules": {
        // Custom rules for typescript by Osmosys
        "@typescript-eslint/no-explicit-any": "error",
        "arrow-body-style": [
          "error",
          "as-needed",
          {
            "requireReturnForObjectLiteral": false
          }
        ],
        "@typescript-eslint/prefer-function-type": "error",
        "@typescript-eslint/naming-convention": "error",
        "capitalized-comments": [
          "off",
          "never",
          {
            "line": {
              "ignorePattern": ".*",
              "ignoreInlineComments": true,
              "ignoreConsecutiveComments": true
            },
            "block": {
              "ignorePattern": ".*",
              "ignoreInlineComments": true,
              "ignoreConsecutiveComments": true
            }
          }
        ],
        "spaced-comment": [
          "error",
          "always",
          {
            "line": {
              "exceptions": [
                "-",
                "+"
              ],
              "markers": [
                "=",
                "!",
                "/"
              ]
            },
            "block": {
              "exceptions": [
                "-",
                "+"
              ],
              "markers": [
                "=",
                "!",
                ":",
                "::"
              ],
              "balanced": true
            }
          }
        ],
        "eol-last": [
          "error",
          "always"
        ],
        "guard-for-in": "error",
        "no-restricted-imports": [
          "off",
          {
            "paths": [],
            "patterns": []
          }
        ],
        "indent": [
          "error",
          2,
          {
            "SwitchCase": 1,
            "VariableDeclarator": 1,
            "outerIIFEBody": 1,
            "FunctionDeclaration": {
              "parameters": 1,
              "body": 1
            },
            "FunctionExpression": {
              "parameters": 1,
              "body": 1
            },
            "CallExpression": {
              "arguments": 1
            },
            "ArrayExpression": 1,
            "ObjectExpression": 1,
            "ImportDeclaration": 1,
            "flatTernaryExpressions": false,
            "ignoredNodes": [
              "JSXElement",
              "JSXElement > *",
              "JSXAttribute",
              "JSXIdentifier",
              "JSXNamespacedName",
              "JSXMemberExpression",
              "JSXSpreadAttribute",
              "JSXExpressionContainer",
              "JSXOpeningElement",
              "JSXClosingElement",
              "JSXFragment",
              "JSXOpeningFragment",
              "JSXClosingFragment",
              "JSXText",
              "JSXEmptyExpression",
              "JSXSpreadChild"
            ],
            "ignoreComments": false
          }
        ],
        "@typescript-eslint/consistent-type-definitions": "error",
        "@typescript-eslint/explicit-member-accessibility": "off",
        "@typescript-eslint/member-ordering": [
          "error",
          {
            "default": [
              "static-field",
              "instance-field",
              "static-method",
              "instance-method"
            ]
          }
        ],
        "no-empty-function": [
          "error",
          {
            "allow": [
              "arrowFunctions",
              "functions",
              "methods"
            ]
          }
        ],
        "no-bitwise": "error",
        "no-console": "warn",
        "no-new-wrappers": "error",
        "no-debugger": "error",
        "constructor-super": "error",
        "no-empty": "error",
        "@typescript-eslint/no-empty-interface": "error",
        "no-eval": "error",
        "@typescript-eslint/no-inferrable-types": "error",
        "@typescript-eslint/no-misused-new": "error",
        "@typescript-eslint/no-non-null-assertion": "error",
        "no-shadow": "error",
        "dot-notation": [
          "error",
          {
            "allowKeywords": true
          }
        ],
        "no-throw-literal": "error",
        "no-fallthrough": "error",
        "no-trailing-spaces": [
          "error",
          {
            "skipBlankLines": false,
            "ignoreComments": false
          }
        ],
        "no-undef-init": "error",
        "no-unused-expressions": [
          "error",
          {
            "allowShortCircuit": false,
            "allowTernary": false,
            "allowTaggedTemplates": false
          }
        ],
        "no-var": "error",
        "sort-keys": [
          "off",
          "asc",
          {
            "caseSensitive": false,
            "natural": true
          }
        ],
        "brace-style": [
          "error",
          "1tbs",
          {
            "allowSingleLine": true
          }
        ],
        "prefer-const": [
          "error",
          {
            "destructuring": "any",
            "ignoreReadBeforeAssign": true
          }
        ],
        "quotes": [
          "error",
          "single",
          {
            "avoidEscape": true
          }
        ],
        "radix": "error",
        "eqeqeq": [
          "error",
          "always",
          {
            "null": "ignore"
          }
        ],
        "@typescript-eslint/type-annotation-spacing": "error",
        "@typescript-eslint/unified-signatures": "error",
        "no-multi-spaces": [
          "error",
          {
            "ignoreEOLComments": false
          }
        ],
        "@angular-eslint/no-output-on-prefix": "error",
        "@angular-eslint/no-inputs-metadata-property": "error",
        "@angular-eslint/no-outputs-metadata-property": "error",
        "@angular-eslint/no-host-metadata-property": "error",
        "@angular-eslint/use-lifecycle-interface": "error",
        "@angular-eslint/use-pipe-transform-interface": "error",
        "@angular-eslint/component-class-suffix": "error",
        "@angular-eslint/directive-class-suffix": "error",
        "import/no-extraneous-dependencies": [
          "error",
          {
            "devDependencies": false,
            "optionalDependencies": false,
            "peerDependencies": false
          }
        ]
      }
    },
    // Eslint for HTML files
    {
      "files": [
        "*.html", "*.component.html"
      ],
      "extends": [
        "plugin:@angular-eslint/template/recommended",
        "plugin:@angular-eslint/template/accessibility"
      ],
      "rules": {
        // Custom rules for HTML by Osmosys
      }
    }
  ]
}

```
