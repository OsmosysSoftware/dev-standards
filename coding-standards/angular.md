# Angular Coding Standards

## Coding Style Guide

We at osmosys follow all the conding standards mentioned here - https://angular.io/guide/styleguide

For Typescript, we follow AirBnb's typescript guidelines - https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb-base

List of All AirBnB's typescript rules - [Click here](https://osmosysasia-my.sharepoint.com/:x:/g/personal/rajkumar_p_osmosys_co/EcSnDteKjvhGr-6jgmdIRDEBVsW7hjqfXs7o8NwUTea7oQ?e=QQAVfR)

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
5. npm i prettier eslint-config-prettier eslint-plugin-prettier --save-dev
6. ng add @angular-eslint/schematics

### **Files to be added in root directory**

### Replace all data in `.eslintrc.json` with the following

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
        "prettier",
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

        "func-call-spacing": [
          "error",
          "never"
        ],

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
        "semi": [
          "error",
          "always"
        ],
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
        "object-curly-spacing": [
          "error",
          "always"
        ]
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

### Create `tsconfig.eslint.json`

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "noEmit": true
  },
  "include": ["src/**/*.ts", "src/**/*.js", "test/**/*.ts", "src", "e2e", ".eslintrc.json"]
}

```

### Create `.prettierrc.js`

```js
module.exports = {
  trailingComma: "all",
  tabWidth: 2,
  semi: true,
  singleQuote: true,
  bracketSpacing: true,
  printWidth: 100
};

```

### **Add an extra line under `"scripts"` in `package.json` for Prettier run command**

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

### **Test Files using terminal commands**

1. For linting

> ng lint

2. To automatically fix formatting issues as per Prettier rules

> npm run prettier-format
    }
  ]
}

```
