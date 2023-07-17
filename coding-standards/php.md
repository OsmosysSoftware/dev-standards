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
| SlevomatCodingStandard.TypeHints.UselessConstantTypeHint                                                                      | Checks for useless constant type hints in function and method signatures.                                                                           | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/type-hints.md#slevomatcodingstandardtypehintsuselessconstanttypehint-)                                                                                         |
| SlevomatCodingStandard.Arrays.DisallowImplicitArrayCreation                                                                   | Disallows implicit array creation using the short syntax `[]` and requires using the explicit `array()` syntax.                                   | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/arrays.md#slevomatcodingstandardarraysdisallowimplicitarraycreation)                                                                                         |
| SlevomatCodingStandard.ControlStructures.RequireNullCoalesceOperator                                                          | Enforces the use of the null coalesce operator (`??`) instead of the ternary operator (`?:`) when checking for null values.                     | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/control-structures.md#slevomatcodingstandardcontrolstructuresrequirenullcoalesceoperator-)                                                                     |
| SlevomatCodingStandard.PHP.UselessSemicolon                                                                                 | Detects and removes useless semicolons in PHP code.                                                                                               | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/php.md#slevomatcodingstandardphpuselesssemicolon-)                                                                                                               |
| SlevomatCodingStandard.Variables.UnusedVariable                                                                              | Detects unused variables and raises warnings to encourage their removal.                                                                           | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/variables.md#slevomatcodingstandardvariablesunusedvariable)                                                                                                     |
| SlevomatCodingStandard.Variables.UselessVariable                                                                             | Detects and removes useless variables that are assigned but never used.                                                                            | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/variables.md#slevomatcodingstandardvariablesuselessvariable-)                                                                                                   |
| SlevomatCodingStandard.Exceptions.DeadCatch                                                                                   | Detects dead catch blocks in try-catch statements where an exception type is caught but not used.                                                  | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/exceptions.md#slevomatcodingstandardexceptionsdeadcatch)                                                                                                         |
| SlevomatCodingStandard.Classes.MethodSpacing                                                                                  | Enforces a consistent spacing between methods in PHP classes.                                                                                      | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/classes.md#slevomatcodingstandardclassesmethodspacing-)                                                                                                         |
| SlevomatCodingStandard.Classes.PropertySpacing                                                                                | Enforces a consistent spacing between properties in PHP classes.                                                                                    | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/classes.md#slevomatcodingstandardclassespropertyspacing-)                                                                                                       |
| SlevomatCodingStandard.Namespaces.UnusedUses                                                                                  | Detects unused import statements (`use` statements) in PHP namespaces and suggests their removal.                                                  | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/namespaces.md#slevomatcodingstandardnamespacesunuseduses-)                                                                                                     |
| SlevomatCodingStandard.Namespaces.AlphabeticallySortedUses                                                                    | Enforces alphabetically sorted import statements (`use` statements) in PHP namespaces.                                                             | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/namespaces.md#slevomatcodingstandardnamespacesalphabeticallysorteduses-)                                                                                     |
| SlevomatCodingStandard.Whitespaces.DuplicateSpaces                                                                            | Detects duplicate spaces in PHP code and suggests their removal.                                                                                  | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/whitespaces.md#slevomatcodingstandardwhitespacesduplicatespaces-)                                                                                               |
| SlevomatCodingStandard.TypeHints.ReturnTypeHintSpacing                                                                        | Enforces a consistent spacing around the return type hints in PHP function and method signatures.                                                 | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/type-hints.md#slevomatcodingstandardtypehintsreturntypehintspacing-)                                                                                             |
| SlevomatCodingStandard.Commenting.DisallowCommentAfterCode                                                                    | Disallows comments placed after code statements and encourages placing comments on a separate line.                                               | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/commenting.md#slevomatcodingstandardcommentingdisallowcommentaftercode-)                                                                                         |
| SlevomatCodingStandard.Commenting.EmptyComment                                                                                | Detects and removes empty comments in PHP code.                                                                                                   | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/commenting.md#slevomatcodingstandardcommentingemptycomment-)                                                                                                     |
| SlevomatCodingStandard.Commenting.RequireOneLineDocComment                                                                    | Enforces the use of one-line doc comments for properties, constants, and methods in PHP classes.                                                 | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/commenting.md#slevomatcodingstandardcommentingrequireonelinedoccomment-)                                                                                         |
| SlevomatCodingStandard.ControlStructures.UselessIfConditionWithReturn                                                        | Detects and removes unnecessary if conditions in PHP code where a return statement follows immediately.                                           | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/control-structures.md#slevomatcodingstandardcontrolstructuresuselessifconditionwithreturn-)                                                                   |
| SlevomatCodingStandard.ControlStructures.UselessTernaryOperator                                                              | Detects and suggests removing unnecessary ternary operators in PHP code where the condition is redundant.                                         | [Link](https://github.com/slevomat/coding-standard/blob/master/doc/control-structures.md#slevomatcodingstandardcontrolstructuresuselessternaryoperator-)                                                                         |

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