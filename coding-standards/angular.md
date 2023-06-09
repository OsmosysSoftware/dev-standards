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

#### **1. Add angular linting Schematics**

> ng add @angular-eslint/schematics

This will create a .eslintrc file where you can create rules according to your wishes.

#### **2. Install a Style Guide Plugin for Typescript linting: AirBnB**

> pm install eslint-plugin-import eslint-config-airbnb-typescript --save-dev

#### **3. Install & add Prettier extension**

> npm i prettier eslint-config-prettier eslint-plugin-prettier --save-dev

#### **4. Create Prettier config file if not already created**

Prettier can format files with no configuration but for AirBnB code guide we need to specify some settings. Create `.prettierrc.js` in app root folder

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

This configuration will be used by ESLint and by Prettier if you want to run it separately. You can format your code with Prettier itself with prettier --write . or with Prettier Plugin for VS Code.

#### **5. Install additional eslint plugins - jasmine**

If you want to install another plugin for ESLint, for example, to lint Jasmine spec files, install appropriate npm-package

> npm install eslint-plugin-jasmine --save-dev

#### **6. Get a list of errors**

Use the following command in your working tree to get a list of linting errors in your project.

> ng lint

Your IDE will automatically show errors in the file if configured to do so.

### **.eslintrc.json**

```json
{
  "root": true,
  "ignorePatterns": [
    "projects/**/*"
  ],
  "overrides": [
    // Angular Rules
    {
      "files": [
        "*.ts"
      ],
      "parserOptions": {
        "project": [
          "tsconfig.*?.json",
          "e2e/tsconfig.json"
        ],
        "createDefaultProgram": true
      },
      "extends": [
        "plugin:@angular-eslint/recommended"
      ],
      "rules": {}
    },
    {
      "files": [
        "*.component.html"
      ],
      "extends": [
        "plugin:@angular-eslint/template/recommended"
      ],
      "rules": {
        "max-len": [
          "error",
          {
            "code": 140
          }
        ]
      }
    },
    {
      "files": [
        "*.component.ts"
      ],
      "extends": [
        "plugin:@angular-eslint/template/process-inline-templates"
      ]
    },
    // ESlint for typescript using AirBnB Style
    {
      "files": [
        "*.ts"
      ],
      "parserOptions": {
        "project": [
          "tsconfig.*?.json",
          "e2e/tsconfig.json"
        ],
        "createDefaultProgram": true
      },
      "extends": [
        "plugin:@angular-eslint/recommended",
        // AirBnB Styleguide rules
        "airbnb-typescript/base"
      ],
      "rules": {
      }
    },
    // Default overrides using @angular-eslint/schematics
    {
      "files": [
        "*.ts"
      ],
      "extends": [
        "eslint:recommended",
        "plugin:@typescript-eslint/recommended",
        "plugin:@angular-eslint/recommended",
        "plugin:@angular-eslint/template/process-inline-templates"
      ],
      "rules": {
        "@angular-eslint/directive-selector": [
          "error",
          {
            "type": "attribute",
            "prefix": "app",
            "style": "camelCase"
          }
        ],
        "@angular-eslint/component-selector": [
          "error",
          {
            "type": "element",
            "prefix": "app",
            "style": "kebab-case"
          }
        ]
      }
    },
    {
      "files": [
        "*.html"
      ],
      "extends": [
        "plugin:@angular-eslint/template/recommended",
        "plugin:@angular-eslint/template/accessibility"
      ],
      "rules": {
      }
    },
    // Jasmine linting
    {
      "files": [
        "src/**/*.spec.ts",
        "src/**/*.d.ts"
      ],
      "parserOptions": {
        "project": "./src/tsconfig.spec.json"
      },
      // Jasmine rules
      "extends": [
        "plugin:jasmine/recommended"
      ],
      // Plugin to run Jasmine rules
      "plugins": [
        "jasmine"
      ],
      "env": {
        "jasmine": true
      },
      "rules": {
        // Custom rules
      }
    }
  ]
}
```
