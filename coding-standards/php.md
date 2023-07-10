# PHP development standards
This contains PHP standards. 

## Coding Conventions
https://github.com/slevomat/coding-standard#alphabetical-list-of-sniffs

## Naming Conventions
https://www.php-fig.org/psr/psr-12/

## Security Standards
[https://cheatsheetseries.owasp.org/cheatsheets/Laravel_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/PHP_Configuration_Cheat_Sheet.html)

## Enforcing tools and config
- PHPCS -
Create .phpcs.xml file in the root directory of your project.

Then add the below configuration in this file.

<?xml version="1.0"?>
<ruleset name="PHP_CodeSniffer">
    <file>app</file>
    <file>config</file>
    <file>database</file>
    <file>resources</file>
    <file>routes</file>
    <file>tests</file>

    <!-- exclude our migrations directory from the violation check-->
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

# Usage

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
  
- PHAN -


# Configuration

Create `.phan/config.php` file in the root directory of your project.

Then add the below configuration in this file.

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

# Usage

Add script command to run `phan` in `composer.json` file.

```json
"scripts": {
    // ..<existing scripts>
    "phan": "vendor/bin/phan --config-file .phan/config.php",
  },
```

**`composer run phan`**

This command will analyze and display all the issues if any.
