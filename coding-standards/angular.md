# Angular Coding Standards

- [Angular Coding Standards](#angular-coding-standards)
  - [Coding Style Guide](#coding-style-guide)
  - [Security](#security)
  - [Standard Enforcing Tools](#standard-enforcing-tools)
  - [Setting up ESLint, TypeScript (Airbnb rules), and Prettier](#setting-up-eslint-typescript-airbnb-rules-and-prettier)
    - [Prerequisites](#prerequisites)
    - [Visual Studio Code Extensions](#visual-studio-code-extensions)
    - [NPM Commands](#npm-commands)
    - [Files to be created/modified in root directory](#files-to-be-createdmodified-in-root-directory)
    - [Testing and Commands](#testing-and-commands)
  
## Coding Style Guide

At Osmosys, we adhere to a comprehensive set of coding standards to ensure consistency and maintainability in our Angular projects. Our coding style is based on the guidelines provided by the [Angular Style Guide](https://angular.io/guide/styleguide).

For TypeScript development, we follow the TypeScript guidelines established by Airbnb. You can find detailed TypeScript rules in the [Airbnb TypeScript Style Guide](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb-base).

For the complete list of TypeScript rules from Airbnb, please refer to this [link](https://osmosysasia-my.sharepoint.com/:x:/g/personal/rajkumar_p_osmosys_co/EcSnDteKjvhGr-6jgmdIRDEBVsW7hjqfXs7o8NwUTea7oQ?e=QQAVfR).

[Back to top](#angular-coding-standards)
## Security 

Security is a top priority in our development process. We implement security practices outlined in the [Angular Security Guide](https://angular.io/guide/security) to safeguard our applications against common web application vulnerabilities and attacks, including cross-site scripting (XSS) attacks.

[Back to top](#angular-coding-standards)
## Standard Enforcing Tools

To ensure consistent code quality and adherence to our standards, we utilize the following tools:

- [ESLint](https://eslint.org/)
- [Prettier](https://prettier.io/)

[Back to top](#angular-coding-standards)
## Setting up ESLint, TypeScript (Airbnb rules), and Prettier

Follow these steps to set up ESLint, TypeScript (based on Airbnb rules), and Prettier for your Angular projects:

### Prerequisites

Before you begin, make sure you have the following software installed:

1. [Node.js](https://nodejs.org/en)
2. [npm](https://www.npmjs.com/)
3. [Angular CLI](https://angular.io/cli)
4. [Visual Studio Code](https://code.visualstudio.com/)

[Back to top](#angular-coding-standards)
### Visual Studio Code Extensions

Install the following extensions in Visual Studio Code:

1. [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
2. [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

**Note**: Make sure these pluggins are installed in your code editor and enabled for your current workspace.

[Back to top](#angular-coding-standards)
### NPM Commands

Navigate to the root directory of your project and execute the following npm commands:

1. **Initialize ESLint configuration**

    ```sh
    npm init @eslint/config
    ```
    Choose the following options:
    - Usage: To check syntax, find problems, and enforce code style
    - Modules: JavaScript (import/export)
    - Frameworks: Other
    - Typescript: No (Airbnb does not have support for TS, it is defined for JS and we will add additional TS support for it later)
    - Environment: Browser
    - Style: Popular Guide
    - Style guide: Airbnb
    - Format: JSON

2. **Install dependencies to support typescript**

    ```sh
    npm install eslint-config-airbnb-typescript @typescript-eslint/eslint-plugin @typescript-eslint/parser --save-dev
    ```

3. **Install Prettier and related ESLint configurations**

    ```sh
    npm install prettier eslint-config-prettier eslint-plugin-prettier --save-dev
    ```

4. **Integrate Angular ESLint schematics**

    ```sh
    ng add @angular-eslint/schematics
    ```

[Back to top](#angular-coding-standards)
### Files to be created/modified in root directory

To ensure proper setup, add the following configuration files to your project's root directory:

1. **`.eslintrc.json`**  
  Replace all data in `.eslintrc.json` with the following

    ```json
    {
      "env": {
        "es6": true,
        "browser": true,
        "node": true
      },
      "extends": ["plugin:@angular-eslint/recommended"],
      "rules": {},
      // Eslint for HTML files
      "overrides": [
        {
          "files": ["*.html", "*.component.html"],
          // We set parserOptions.project for the project to allow TypeScript to create the type-checker behind the scenes when we run linting
          "parserOptions": {
            "project": ["tsconfig.(app|spec).json"]
          },
          "extends": [
            "plugin:@angular-eslint/template/recommended",
            "plugin:@angular-eslint/template/accessibility"
          ],
          "rules": {
            // Custom rules for HTML by Osmosys
            "max-len": "warn"
          }
        },
        // Custom rules for TypeScript
        {
          "files": ["*.ts"],
          "extends": [
            // Added base
            "airbnb-base",
            "airbnb-typescript/base",
            // Added modern prettier
            "prettier"
          ],
          "parser": "@typescript-eslint/parser",
          "parserOptions": {
            "parser": "@typescript-eslint/parser",
            "ecmaVersion": "latest",
            "project": ["./tsconfig.eslint.json", "./tsconfig.json"]
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
                  "exceptions": ["-", "+"],
                  "markers": ["=", "!", "/"]
                },
                "block": {
                  "exceptions": ["-", "+"],
                  "markers": ["=", "!", ":", "::"],
                  "balanced": true
                }
              }
            ],
            "eol-last": ["error", "always"],
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
                "default": ["static-field", "instance-field", "static-method", "instance-method"]
              }
            ],
            "no-empty-function": [
              "error",
              {
                "allow": ["arrowFunctions", "functions", "methods"]
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
            ],

            // Additional Custom Rules

            "camelcase": [
              "error",
              {
                "properties": "never",
                "ignoreDestructuring": false
              }
            ],
            "comma-dangle": [
              "error",
              {
                "arrays": "always-multiline",
                "objects": "always-multiline",
                "imports": "always-multiline",
                "exports": "always-multiline",
                "functions": "always-multiline"
              }
            ],
            "comma-spacing": [
              "error",
              {
                "before": false,
                "after": true
              }
            ],
            "default-param-last": "error",

            "func-call-spacing": ["error", "never"],

            "keyword-spacing": [
              "error",
              {
                "before": true,
                "after": true,
                "overrides": {
                  "return": {
                    "after": true
                  },
                  "throw": {
                    "after": true
                  },
                  "case": {
                    "after": true
                  }
                }
              }
            ],
            "lines-between-class-members": [
              "error",
              "always",
              {
                "exceptAfterSingleLine": false
              }
            ],
            "no-array-constructor": "error",
            "no-dupe-class-members": "error",

            "no-extra-parens": [
              "off",
              "all",
              {
                "conditionalAssign": true,
                "nestedBinaryExpressions": false,
                "returnAssign": false,
                "ignoreJSX": "all", // delegate to eslint-plugin-react
                "enforceForArrowConditionals": false
              }
            ],
            "no-extra-semi": "error",
            "no-implied-eval": "error",
            "no-new-func": "error",
            "no-loss-of-precision": "error",
            "no-loop-func": "error",
            "no-magic-numbers": [
              "off",
              {
                "ignore": [],
                "ignoreArrayIndexes": true,
                "enforceConst": true,
                "detectObjects": false
              }
            ],
            "no-redeclare": "error",
            "space-before-blocks": "error",

            "no-unused-vars": [
              "error",
              {
                "vars": "all",
                "args": "after-used",
                "ignoreRestSiblings": true
              }
            ],
            "no-use-before-define": [
              "error",
              {
                "functions": true,
                "classes": true,
                "variables": true
              }
            ],
            "no-useless-constructor": "error",
            "semi": ["error", "always"],
            "space-before-function-paren": [
              "error",
              {
                "anonymous": "always",
                "named": "never",
                "asyncArrow": "always"
              }
            ],
            "require-await": "off",
            "no-return-await": "error",
            "space-infix-ops": "error",
            "object-curly-spacing": ["error", "always"]
          }
        },
        // Configuration for unit and e2e spec files
        {
          "files": ["*.spec.ts"],
          "rules": {
            "@typescript-eslint/no-unused-vars": "off"
          }
        },
        /**
        * This extra piece of configuration is only necessary if you make use of inline
        * templates within Component metadata, e.g.:
        */
        {
          "files": ["*.component.ts"],
          "parser": "@typescript-eslint/parser",
          "parserOptions": {
            "ecmaVersion": 2020,
            "sourceType": "module"
          },
          "plugins": ["@angular-eslint/template"],
          "processor": "@angular-eslint/template/extract-inline-html"
        }
      ]
    }
    ```

2. **`tsconfig.eslint.json`**  
  Create a `tsconfig.eslint.json` file with the following content:

    ```json
    {
      "extends": "./tsconfig.json",
      "compilerOptions": {
        "noEmit": true
      },
      "include": ["src/**/*.ts", "src/**/*.js", "test/**/*.ts", "src", "e2e", ".eslintrc.json"]
    }

    ```


3. **`.prettierrc.json`**  
  Create a `.prettierrc.json` file with the following content:

    ```js
    {
      "trailingComma": "all",
      "tabWidth": 2,
      "semi": true,
      "singleQuote": true,
      "bracketSpacing": true,
      "printWidth": 100
    }
    ```

4. **`.package.json`**  
  Update `.package.json`. Add the following line under "scripts" to enable Prettier formatting:

    ```json
    // package.json
    {
      // ...
      "scripts": {
        // Other Commands
        // Add the following line under "scripts"
        "prettier-format": "prettier --ignore-path .gitignore --write \"**/*.+(js|ts|json)\""
      }
      // ...
    }
    ```
1. **`settings.json`**   
  In your project root directory, look for `.vscode` folder and create or edit `settings.json` file inside it with the following:

    ```json
      {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": true,
        "[javascript]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode"
        },
        "[typescript]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode"
        },
        "[css]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode"
        },
        "[html]": {
          "editor.defaultFormatter": "esbenp.prettier-vscode"
        }
      }
    ```

[Back to top](#angular-coding-standards)
### Testing and Commands

1. **Linting: Check for Code Issues**  
   Use the following command to analyze your code for potential issues:

    ```sh
    ng lint
    ```

    This command generates a comprehensive report highlighting any problems present in your current codebase.

2. **Auto-fix Linting Issues**  
   If the ng lint command detects fixable issues, you can automatically resolve some of them using:

    ```sh
    ng lint --fix
    ```

    By running this command, you allow the linter to automatically address certain issues reported by eslint

3. **Formatting: Prettier Rules Enforcement**  
   To ensure consistent code formatting according to Prettier rules, utilize the command:

    ```sh
    npm run prettier-format
    ```

    Executing this command will format your entire codebase in alignment with the specified Prettier configuration (this is based on the files mentioned in your package.json). This is only recommended for the first time your are enforcing prettier rules and want to format all your code according to specified rules. 

4. **Formatting on Save**  
   Upon completing the mentioned steps, your files will be automatically formatted to adhere to the guidelines outlined in `.prettierrc.json` whenever you save them. This integration streamlines the process of maintaining a uniform code style.  

[Back to top](#angular-coding-standards)