# PHP development standards
This contains PHP standards. 

## Coding Conventions
https://github.com/slevomat/coding-standard#alphabetical-list-of-sniffs

## Naming Conventions
https://www.php-fig.org/psr/psr-12/

## Security Standards
[https://cheatsheetseries.owasp.org/cheatsheets/Laravel_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/PHP_Configuration_Cheat_Sheet.html)

## Enforcing tools and config

### PHPCS
#### Installation 

```sh
composer require squizlabs/php_codesniffer --dev
```
PHPCS by default comes with a set of rules which can snif your code against popular standards like PSR1, PSR12 etc. Among the default rules, we use the following rules 

| Rule                              | Description                                     | URL                                                                                                       |
|-----------------------------------|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| PSR12                             | Checks for PSR standards                        | [Link](https://github.com/squizlabs/PHP_CodeSniffer/blob/master/src/Standards/PSR12/ruleset.xml)         |
| PSR12.Files.FileHeader.SpacingAfterBlock | To exclude checking the format of the file header. | [Link](https://github.com/squizlabs/PHP_CodeSniffer/blob/master/src/Standards/PSR12/Sniffs/Files/FileHeaderSniff.php) |
| Generic.WhiteSpace.DisallowTabIndent | To allow tab (mostly to avoid conflicts with the external sniff that we are going to use) | [Link](https://github.com/squizlabs/PHP_CodeSniffer/blob/master/src/Standards/Generic/Docs/WhiteSpace/DisallowTabIndentStandard.xml) |
| Generic.PHP.RequireStrictTypes     | Checks for strict type on each file            | [Link](https://github.com/squizlabs/PHP_CodeSniffer/blob/master/src/Standards/Generic/Sniffs/PHP/RequireStrictTypesSniff.php) |
| Generic.WhiteSpace.ScopeIndent     | Defines number of spaces that each indent takes | [Link](https://github.com/squizlabs/PHP_CodeSniffer/blob/master/src/Standards/PEAR/Docs/WhiteSpace/ScopeIndentStandard.xml) |


To install and include external snifs which are created by reliable resources such as [slemovat](https://github.com/slevomat/coding-standard#sniffs-included-in-this-standard), add the following to the config -

```sh
composer require slevomat/coding-standard --dev
```

```xml
<config name="installed_paths" value="../../slevomat/coding-standard"/>

````


| Rule                                                                                                                          | Description                                                                                                                                      | URL                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SlevomatCodingStandard.TypeHints.UselessConstantTypeHint`                                                                      | Checks for useless constant type hints in function and method signatures.                                                                           | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/type-hints.md#slevomatcodingstandardtypehintsuselessconstanttypehint-)                                                                                         |
| `SlevomatCodingStandard.Arrays.DisallowImplicitArrayCreation`                                                                   | Disallows implicit array creation using the short syntax `[]` and requires using the explicit `array()` syntax.                                   | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/arrays.md#slevomatcodingstandardarraysdisallowimplicitarraycreation)                                                                                         |
| `SlevomatCodingStandard.ControlStructures.RequireNullCoalesceOperator`                                                          | Enforces the use of the null coalesce operator (`??`) instead of the ternary operator (`?:`) when checking for null values.                     | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/control-structures.md#slevomatcodingstandardcontrolstructuresrequirenullcoalesceoperator-)                                                                     |
| `SlevomatCodingStandard.PHP.UselessSemicolon`                                                                                 | Detects and removes useless semicolons in PHP code.                                                                                               | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/php.md#slevomatcodingstandardphpuselesssemicolon-)                                                                                                               |
| `SlevomatCodingStandard.Variables.UnusedVariable`                                                                              | Detects unused variables and raises warnings to encourage their removal.                                                                           | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/variables.md#slevomatcodingstandardvariablesunusedvariable)                                                                                                     |
| `SlevomatCodingStandard.Variables.UselessVariable`                                                                             | Detects and removes useless variables that are assigned but never used.                                                                            | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/variables.md#slevomatcodingstandardvariablesuselessvariable-)                                                                                                   |
| `SlevomatCodingStandard.Exceptions.DeadCatch`                                                                                   | Detects dead catch blocks in try-catch statements where an exception type is caught but not used.                                                  | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/exceptions.md#slevomatcodingstandardexceptionsdeadcatch)                                                                                                         |
| `SlevomatCodingStandard.Classes.MethodSpacing`                                                                                  | Enforces a consistent spacing between methods in PHP classes.                                                                                      | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/classes.md#slevomatcodingstandardclassesmethodspacing-)                                                                                                         |
| `SlevomatCodingStandard.Classes.PropertySpacing`                                                                                | Enforces a consistent spacing between properties in PHP classes.                                                                                    | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/classes.md#slevomatcodingstandardclassespropertyspacing-)                                                                                                       |
| `SlevomatCodingStandard.Namespaces.UnusedUses`                                                                                  | Detects unused import statements (`use` statements) in PHP namespaces and suggests their removal.                                                  | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/namespaces.md#slevomatcodingstandardnamespacesunuseduses-)                                                                                                     |
| `SlevomatCodingStandard.Namespaces.AlphabeticallySortedUses`                                                                    | Enforces alphabetically sorted import statements (`use` statements) in PHP namespaces.                                                             | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/namespaces.md#slevomatcodingstandardnamespacesalphabeticallysorteduses-)                                                                                     |
| `SlevomatCodingStandard.Whitespaces.DuplicateSpaces`                                                                            | Detects duplicate spaces in PHP code and suggests their removal.                                                                                  | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/whitespaces.md#slevomatcodingstandardwhitespacesduplicatespaces-)                                                                                               |
| `SlevomatCodingStandard.TypeHints.ReturnTypeHintSpacing`                                                                        | Enforces a consistent spacing around the return type hints in PHP function and method signatures.                                                 | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/type-hints.md#slevomatcodingstandardtypehintsreturntypehintspacing-)                                                                                             |
| `SlevomatCodingStandard.Commenting.DisallowCommentAfterCode`                                                                    | Disallows comments placed after code statements and encourages placing comments on a separate line.                                               | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/commenting.md#slevomatcodingstandardcommentingdisallowcommentaftercode-)                                                                                         |
| `SlevomatCodingStandard.Commenting.EmptyComment`                                                                                | Detects and removes empty comments in PHP code.                                                                                                   | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/commenting.md#slevomatcodingstandardcommentingemptycomment-)                                                                                                     |
| `SlevomatCodingStandard.Commenting.RequireOneLineDocComment`                                                                    | Enforces the use of one-line doc comments for properties, constants, and methods in PHP classes.                                                 | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/commenting.md#slevomatcodingstandardcommentingrequireonelinedoccomment-)                                                                                         |
| `SlevomatCodingStandard.ControlStructures.UselessIfConditionWithReturn`                                                        | Detects and removes unnecessary if conditions in PHP code where a return statement follows immediately.                                           | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/control-structures.md#slevomatcodingstandardcontrolstructuresuselessifconditionwithreturn-)                                                                   |
| `SlevomatCodingStandard.ControlStructures.UselessTernaryOperator`                                                              | Detects and suggests removing unnecessary ternary operators in PHP code where the condition is redundant.                                         | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/control-structures.md#slevomatcodingstandardcontrolstructuresuselessternaryoperator-)                                                                         |

#### Configuration

```xml
<?xml version="1.0"?>
<ruleset name="PHP_CodeSniffer">
    <!-- Include the following directories for violation check-->
    <file>app</file>
    <file>config</file>
    <file>database</file>
    <file>resources</file>
    <file>routes</file>
    <file>tests</file>

    <!-- Exclude our migrations directory from the violation check-->
    <exclude-pattern>*/migrations/*</exclude-pattern>

	<arg name="tab-width" value="4"/>
	<rule ref="PSR12">
		<exclude name="Generic.WhiteSpace.DisallowTabIndent"/>
        <exclude name="PSR12.Files.FileHeader.SpacingAfterBlock"/>
	</rule>
	<rule ref="Generic.WhiteSpace.DisallowSpaceIndent"/>
    <rule ref="Generic.PHP.RequireStrictTypes" />
	<rule ref="Generic.WhiteSpace.ScopeIndent">
		<properties>
			<property name="indent" value="4"/>
			<property name="tabIndent" value="true"/>
		</properties>
	</rule>

	<!-- See https://github.com/slevomat/coding-standard#sniffs-included-in-this-standard -->
	<config name="installed_paths" value="../../slevomat/coding-standard"/>
	<rule ref="SlevomatCodingStandard.TypeHints.UselessConstantTypeHint" />
	<rule ref="SlevomatCodingStandard.Arrays.DisallowImplicitArrayCreation" />
	<rule ref="SlevomatCodingStandard.ControlStructures.RequireNullCoalesceOperator" />
	<rule ref="SlevomatCodingStandard.PHP.UselessSemicolon" />
	<rule ref="SlevomatCodingStandard.Variables.UnusedVariable">
		<properties>
			<property name="ignoreUnusedValuesWhenOnlyKeysAreUsedInForeach" value="true" />
		</properties>
	</rule>
	<rule ref="SlevomatCodingStandard.Variables.UselessVariable" />
	<rule ref="SlevomatCodingStandard.Exceptions.DeadCatch" />
	<rule ref="SlevomatCodingStandard.Classes.MethodSpacing" >
		<properties>
			<property name="minLinesCount" value="1"/>
			<property name="maxLinesCount" value="1"/>
		</properties>
	</rule>
	<rule ref="SlevomatCodingStandard.Classes.PropertySpacing">
		<properties>
			<property name="minLinesCountBeforeWithComment" value="0"/>
			<property name="maxLinesCountBeforeWithComment" value="0"/>
			<property name="minLinesCountBeforeWithoutComment" value="0"/>
			<property name="maxLinesCountBeforeWithoutComment" value="0"/>
		</properties>
	</rule>
	<rule ref="SlevomatCodingStandard.Namespaces.UnusedUses">
		<properties>
			<property name="searchAnnotations" value="true"/>
		</properties>
	</rule>
	<rule ref="SlevomatCodingStandard.Namespaces.AlphabeticallySortedUses" />
	<rule ref="SlevomatCodingStandard.Whitespaces.DuplicateSpaces" />
	<rule ref="SlevomatCodingStandard.TypeHints.ReturnTypeHintSpacing">
		<properties>
			<property name="spacesCountBeforeColon" value="0"/>
		</properties>
	</rule>
	<rule ref="SlevomatCodingStandard.Commenting.DisallowCommentAfterCode" />
	<rule ref="SlevomatCodingStandard.Commenting.EmptyComment" />
	<rule ref="SlevomatCodingStandard.Commenting.RequireOneLineDocComment" />
	<rule ref="SlevomatCodingStandard.ControlStructures.UselessIfConditionWithReturn" />
	<rule ref="SlevomatCodingStandard.ControlStructures.UselessTernaryOperator" />

    <!-- disable useless function comment -->
    <rule ref="SlevomatCodingStandard.Commenting.UselessFunctionDocComment" />
</ruleset>
```
#### Usage

Add couple of script commands to run `phpcs` and `phpcbf` in `composer.json` file.

```json
"scripts": {
    // ..<existing scripts>
    "lint": "vendor/bin/phpcs --standard=.phpcs.xml",
    "lint:fix": "vendor/bin/phpcbf --standard=.phpcs.xml",
  },
```

**`composer run lint`**

This command will tokenize PHP, JavaScript and CSS files to detect violations of a defined coding standard.

**`composer run lint:fix`**

This command will automatically correct coding standard violations.

### PHP PHAN
#### Installation 

```json
composer require phan/phan --dev
```
Inorder to let your project use php phan, you have to create a folder `.phan` and a file in it `config.php`. All the settings for phan are placed there. 
Here are some key settings to be added -

| Setting                          | Description                                                        | URL                                                                                                       |
|----------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `target_php_version`               | Set the PHP version of your project.                                | [Link](https://github.com/phan/phan/wiki/Phan-Config-Settings#target_php_version)                      |
| `directory_list`                   | Directory list that should be checked for violations.              | [Link](https://github.com/phan/phan/wiki/Phan-Config-Settings#directory_list)                          |
| `exclude_analysis_directory_list`  | Directory list that will be skipped to check violations.           | [Link](https://github.com/phan/phan/wiki/Phan-Config-Settings#exclude_analysis_directory_list)         |
| `plugins`                          | A list of plugin files to execute.                                 | [Link](https://github.com/phan/phan/wiki/Phan-Config-Settings#plugins)                                  |
| `suppress_issue_types`             | Inhibits some issues which don't matter much.                      | [Link](https://github.com/phan/phan/wiki/Phan-Config-Settings#suppress_issue_types)                     |
| `backward_compatibility_checks`    | Backwards Compatibility Checking. It consumes a lot of memory, do only if necessary. | [Link](https://github.com/phan/phan/wiki/Phan-Config-Settings#backward_compatibility_checks)       |
| `unused_variable_detection`        | Set to true in order to attempt to detect unused variables.         | [Link](https://github.com/phan/phan/wiki/Phan-Config-Settings#unused_variable_detection)               |


All the phan settings can be found [here](https://github.com/phan/phan/wiki/Phan-Config-Settings)


PHP Phan works with plugins which comes along while installing it. Here are some plugins that we use

| Plugin                           | Description                                                                   | URL                                                                                                      |
|----------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| `AlwaysReturnPlugin`               | Checks if a function or method with a non-void return type will unconditionally return or throw | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#alwaysreturnpluginphp)                |
| `DollarDollarPlugin`               | Checks for complex variable access expressions `$$x`                           | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#dollardollarpluginphp)                |
| `DuplicateArrayKeyPlugin`          | Warns about common errors in PHP array keys and switch statements             | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#duplicatearraykeypluginphp)           |
| `DuplicateExpressionPlugin`        | Checks for duplicate expressions in a statement that are likely to be a bug  | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#duplicateexpressionpluginphp)         |
| `PregRegexCheckerPlugin`           | This plugin checks for invalid regexes                                        | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#pregregexcheckerplugin)                |
| `PrintfCheckerPlugin`              | Checks for invalid format strings, incorrect argument counts, and unused arguments in printf calls | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#printfcheckerplugin)            |
| `SleepCheckerPlugin`               | Warn about returning non-arrays in `__sleep`, as well as about returning array values with invalid property names in `__sleep` | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#printfcheckerplugin)         |
| `UnreachableCodePlugin`            | Checks for syntactically unreachable statements in the global scope or function bodies | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#unreachablecodepluginphp)          |
| `UseReturnValuePlugin`             | This warns when code fails to use the return value of internal functions/methods | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#unreachablecodepluginphp)      |
| `EmptyStatementListPlugin`         | Checks for empty statement lists in loops/branches                            | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#emptystatementlistpluginphp)          |
| `LoopVariableReusePlugin`          | This plugin detects reuse of loop variables                                  | [Link](https://github.com/phan/phan/tree/v5/.phan/plugins#loopvariablereusepluginphp)            |


All the php phan plugins are documented [here](https://github.com/phan/phan/tree/v5/.phan/plugins#readme)

#### Configuration

```php
<?php

/**
 * This configuration will be read and overlaid on top of the
 * default configuration. Command line arguments will be applied
 * after this file is read.
 */
return [

    // Supported values: `'5.6'`, `'7.0'`, `'7.1'`, `'7.2'`, `'7.3'`, `'7.4'`,
    // `'8.0'`, `'8.1'`, `null`.
    // If this is set to `null`,
    // then Phan assumes the PHP version which is closest to the minor version
    // of the php executable used to execute Phan.
    "target_php_version" => '8.1',

    // A list of directories that should be parsed for class and
    // method information. After excluding the directories
    // defined in exclude_analysis_directory_list, the remaining
    // files will be statically analyzed for errors.
    //
    // Thus, both first-party and third-party code being used by
    // your application should be included in this list.
    
    // Note - Keep adding to the vendor section below as we add more dependencies
    // based on the errors you encounter when you run phan. 
    
    'directory_list' => [
        'app',
        'config',
        'database',
        'public',
        'resources',
        'routes',
        'storage',
        'tests',
        'bootstrap',
        'vendor/laravel',
        'vendor/fakerphp'
        'vendor/fruitcake',
        'vendor/monolog',
        'vendor/nesbot',
        'vendor/ramsey',
        'vendor/psr'
        'vendor/symfony',        
    ],

    // A directory list that defines files that will be excluded
    // from static analysis, but whose class and method
    // information should be included.
    //
    // Generally, you'll want to include the directories for
    // third-party code (such as "vendor/") in this list.
    //
    // n.b.: If you'd like to parse but not analyze 3rd
    //       party code, directories containing that code
    //       should be added to the `directory_list` as
    //       to `exclude_analysis_directory_list`.
    "exclude_analysis_directory_list" => [
        'vendor'
    ],

    // A list of plugin files to execute.
    // Plugins which are bundled with Phan can be added here by providing their name
    // (e.g. 'AlwaysReturnPlugin')
    //
    // Documentation about available bundled plugins can be found
    // at https://github.com/phan/phan/tree/v5/.phan/plugins
    //
    // Alternately, you can pass in the full path to a PHP file
    // with the plugin's implementation.
    // (e.g. 'vendor/phan/phan/.phan/plugins/AlwaysReturnPlugin.php')
    'plugins' => [
        // checks if a function, closure or method unconditionally returns.
        // can also be written as 'vendor/phan/phan/.phan/plugins/AlwaysReturnPlugin.php'
        'AlwaysReturnPlugin',
        'DollarDollarPlugin',
        'DuplicateArrayKeyPlugin',
        'DuplicateExpressionPlugin',
        'PregRegexCheckerPlugin',
        'PrintfCheckerPlugin',
        'SleepCheckerPlugin',
        // Checks for syntactically unreachable statements in
        // the global scope or function bodies.
        'UnreachableCodePlugin',
        'UseReturnValuePlugin',
        'EmptyStatementListPlugin',
        'LoopVariableReusePlugin',
    ],
    'suppress_issue_types' => [
		// The following two have been added to not highlight issues
		// raised due to variables added for interface methods that are
		// then not used by the interface implementation
		'PhanUnusedPublicMethodParameter',
		'PhanUnusedProtectedMethodParameter',
		'PhanUnusedPrivateMethodParameter',
		// Allow unused values in foreach
		'PhanUnusedVariableValueOfForeachWithKey'		
	],
	// Backwards Compatibility Checking
	// (Disable this if the application no longer supports php 5,
	// or use a different tool.
	// Phan's checks are currently slow)
	// Set it to false or omit it.
	'backward_compatibility_checks' => false,
	'unused_variable_detection' => true
];

```
### Usage
Add script command to run `phan` in `composer.json` file.

```json
"scripts": {
    // ..<existing scripts>
    "phan": "vendor/bin/phan --config-file .phan/config.php",
  },
```
**`composer run phan`**

This command will analyze and display all the issues if any.
