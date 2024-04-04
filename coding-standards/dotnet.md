# .NET coding standards

## C# coding standards
We adopted the standards for programming in C# from [the official coding standards supplied by Microsoft](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)

## ASP.NET WebAPI best practices
We follow the best practices [compiled by Microsoft](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices?view=aspnetcore-7.0) when building API projects using ASP.NET Core.

## .NET security best practices
We adopted the security practices provided by [OWASP Cheat Series](https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html) while building applications using .NET.

## EditorConfig
We use EditorConfig to enforce the coding style standards. The following is the configuration file for C#.
The EditorConfig rules are categorized into two types
- [Coding style](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/)
- [Coding analysis](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/)

<details>
<summary><b>Editor config for .NET Core</b></summary>

```
# Naming rules

dotnet_naming_rule.interface_should_be_begins_with_i.severity = suggestion
dotnet_naming_rule.interface_should_be_begins_with_i.symbols = interface
dotnet_naming_rule.interface_should_be_begins_with_i.style = begins_with_i

dotnet_naming_rule.types_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.types_should_be_pascal_case.symbols = types
dotnet_naming_rule.types_should_be_pascal_case.style = pascal_case

dotnet_naming_rule.non_field_members_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.non_field_members_should_be_pascal_case.symbols = non_field_members
dotnet_naming_rule.non_field_members_should_be_pascal_case.style = pascal_case

# Symbol specifications

dotnet_naming_symbols.interface.applicable_kinds = interface
dotnet_naming_symbols.interface.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.interface.required_modifiers =

dotnet_naming_symbols.types.applicable_kinds = class, struct, interface, enum
dotnet_naming_symbols.types.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.types.required_modifiers =

dotnet_naming_symbols.non_field_members.applicable_kinds = property, event, method
dotnet_naming_symbols.non_field_members.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.non_field_members.required_modifiers =

# Naming styles

dotnet_naming_style.begins_with_i.required_prefix = I
dotnet_naming_style.begins_with_i.required_suffix =
dotnet_naming_style.begins_with_i.word_separator =
dotnet_naming_style.begins_with_i.capitalization = pascal_case

dotnet_naming_style.pascal_case.required_prefix =
dotnet_naming_style.pascal_case.required_suffix =
dotnet_naming_style.pascal_case.word_separator =
dotnet_naming_style.pascal_case.capitalization = pascal_case

dotnet_naming_style.pascal_case.required_prefix =
dotnet_naming_style.pascal_case.required_suffix =
dotnet_naming_style.pascal_case.word_separator =
dotnet_naming_style.pascal_case.capitalization = pascal_case
dotnet_style_operator_placement_when_wrapping = beginning_of_line
tab_width = 4
indent_size = 4
end_of_line = crlf
dotnet_style_coalesce_expression = true:suggestion
dotnet_style_null_propagation = true:warning
dotnet_style_prefer_is_null_check_over_reference_equality_method = true:warning
dotnet_style_prefer_auto_properties = true:silent
dotnet_style_object_initializer = true:silent
dotnet_style_collection_initializer = true:silent
dotnet_style_prefer_simplified_boolean_expressions = true:suggestion
dotnet_style_prefer_conditional_expression_over_assignment = true:suggestion
dotnet_style_prefer_conditional_expression_over_return = true:suggestion
dotnet_style_explicit_tuple_names = true:warning
dotnet_style_prefer_inferred_tuple_names = false:suggestion
dotnet_style_prefer_inferred_anonymous_type_member_names = false:suggestion
dotnet_style_prefer_compound_assignment = true:silent
dotnet_style_prefer_simplified_interpolation = true:suggestion
dotnet_style_namespace_match_folder = true:suggestion
dotnet_style_readonly_field = true:suggestion
dotnet_style_predefined_type_for_locals_parameters_members = true:silent
dotnet_style_predefined_type_for_member_access = true:silent
dotnet_style_require_accessibility_modifiers = always:warning
dotnet_style_allow_multiple_blank_lines_experimental = true:silent
dotnet_style_allow_statement_immediately_after_block_experimental = true:silent
dotnet_code_quality_unused_parameters = non_public:error
dotnet_style_parentheses_in_arithmetic_binary_operators = always_for_clarity:silent
dotnet_style_parentheses_in_other_binary_operators = always_for_clarity:silent
dotnet_style_parentheses_in_relational_binary_operators = always_for_clarity:silent
dotnet_style_parentheses_in_other_operators = never_if_unnecessary:silent
dotnet_style_qualification_for_field = true:warning
dotnet_style_qualification_for_property = true:warning
dotnet_style_qualification_for_method = true:warning
dotnet_style_qualification_for_event = true:warning

[*.{cs}]

# Define the 'private_fields' symbol group:
dotnet_naming_symbols.private_fields.applicable_kinds = field
dotnet_naming_symbols.private_fields.applicable_accessibilities = private

# Define the 'private_static_fields' symbol group
dotnet_naming_symbols.private_static_fields.applicable_kinds = field
dotnet_naming_symbols.private_static_fields.applicable_accessibilities = private
dotnet_naming_symbols.private_static_fields.required_modifiers = static

# Define the 'underscored' naming style
dotnet_naming_style.underscored.capitalization = camel_case
dotnet_naming_style.underscored.required_prefix = _

# Define the 'private_fields_underscored' naming rule
dotnet_naming_rule.private_fields_underscored.symbols = private_fields
dotnet_naming_rule.private_fields_underscored.style = underscored
dotnet_naming_rule.private_fields_underscored.severity = error

# Define the 'private_static_fields_none' naming rule
dotnet_naming_rule.private_static_fields_none.symbols = private_static_fields
dotnet_naming_rule.private_static_fields_none.style = underscored
dotnet_naming_rule.private_static_fields_none.severity = none

[*.cs]
csharp_using_directive_placement = outside_namespace:silent
csharp_prefer_simple_using_statement = true:suggestion
csharp_prefer_braces = true:error
csharp_style_namespace_declarations = file_scoped:error
csharp_style_prefer_method_group_conversion = true:suggestion
csharp_style_prefer_top_level_statements = true:silent
csharp_style_expression_bodied_methods = when_on_single_line:suggestion
csharp_style_expression_bodied_constructors = when_on_single_line:suggestion
csharp_style_expression_bodied_operators = when_on_single_line:suggestion
csharp_style_expression_bodied_properties = when_on_single_line:suggestion
csharp_style_expression_bodied_indexers = when_on_single_line:suggestion
csharp_indent_labels = one_less_than_current
csharp_style_expression_bodied_accessors = when_on_single_line:suggestion
csharp_style_expression_bodied_lambdas = when_on_single_line:suggestion
csharp_style_expression_bodied_local_functions = when_on_single_line:suggestion
csharp_style_throw_expression = true:suggestion
csharp_style_prefer_null_check_over_type_check = true:suggestion
csharp_prefer_simple_default_expression = true:suggestion
csharp_style_prefer_local_over_anonymous_function = true:suggestion
csharp_style_prefer_index_operator = true:suggestion
csharp_style_prefer_range_operator = true:suggestion
csharp_style_implicit_object_creation_when_type_is_apparent = true:suggestion
csharp_style_prefer_tuple_swap = true:suggestion
csharp_style_prefer_utf8_string_literals = true:suggestion
csharp_style_inlined_variable_declaration = false:suggestion
csharp_style_deconstructed_variable_declaration = true:suggestion
csharp_style_unused_value_assignment_preference = discard_variable:suggestion
csharp_style_unused_value_expression_statement_preference = discard_variable:silent
csharp_prefer_static_local_function = true:warning
csharp_style_prefer_readonly_struct = true:suggestion
csharp_style_allow_embedded_statements_on_same_line_experimental = true:silent
csharp_style_allow_blank_lines_between_consecutive_braces_experimental = true:silent
csharp_style_allow_blank_line_after_colon_in_constructor_initializer_experimental = true:silent
csharp_style_allow_blank_line_after_token_in_conditional_expression_experimental = true:silent
csharp_style_allow_blank_line_after_token_in_arrow_expression_clause_experimental = true:silent
csharp_style_conditional_delegate_call = true:suggestion
csharp_style_prefer_switch_expression = true:suggestion
csharp_style_prefer_pattern_matching = true:silent
csharp_style_pattern_matching_over_is_with_cast_check = true:suggestion
csharp_style_pattern_matching_over_as_with_null_check = true:suggestion
csharp_style_prefer_not_pattern = true:suggestion
csharp_style_prefer_extended_property_pattern = true:suggestion
csharp_style_var_for_built_in_types = false:error
csharp_style_var_when_type_is_apparent = false:error
csharp_style_var_elsewhere = false:error

csharp_space_around_binary_operators = before_and_after

# Code analysis rules

# The cref tag in an XML documentation comment uses a prefix.
dotnet_diagnostic.CA1200.severity = none

# Do not pass literals as localized parameters
dotnet_diagnostic.CA1303.severity = none

dotnet_diagnostic.CA1304.severity = suggestion

dotnet_diagnostic.CA1305.severity = suggestion

# Specify StringComparison for clarity when comparing string
dotnet_diagnostic.CA1307.severity = suggestion

# Normalize strings to uppercase
dotnet_diagnostic.CA1308.severity = none

# Use ordinal StringComparison when comparing string
dotnet_diagnostic.CA1309.severity = suggestion

# Specify StringComparison for correctness when comparing string
dotnet_diagnostic.CA1310.severity = suggestion

# Specify a culture or use an invariant version for string to upper or to lower
dotnet_diagnostic.CA1311.severity = none

# Platform Invocation Services related method should not be exposed
dotnet_diagnostic.CA1401.severity = error

# The analyzer is enabled by default only for projects that target .NET 5 or later and have an AnalysisLevel of 5 or higher. It can be enabled for target frameworks lower than net5.0 by adding the following config
dotnet_code_quality.enable_platform_analyzer_on_pre_net5_target = true

# Validate platform compatibility for obsoleted APIs
dotnet_diagnostic.CA1422.severity = suggestion

# Avoid excessive inheritance (5 or more levels)
dotnet_diagnostic.CA1501.severity = suggestion

# Avoid excessive cyclomatic complexity
dotnet_diagnostic.CA1502.severity = warning

# Avoid low maintainability index value code
dotnet_diagnostic.CA1505.severity = suggestion

# Avoid excessive class coupling
dotnet_diagnostic.CA1506.severity = suggestion

# Avoid dead conditional code
dotnet_diagnostic.CA1508.severity = warning

# Invalid entry in code metrics configuration file
dotnet_diagnostic.CA1509.severity = error

# Avoid redundant length argument
dotnet_diagnostic.CA1514.severity = warning

# Do not name enum values 'Reserved'
dotnet_diagnostic.CA1700.severity = warning

# Identifiers should not contain underscores
dotnet_diagnostic.CA1707.severity = warning

# Identifiers should differ by more than case
dotnet_diagnostic.CA1708.severity = warning

# Identifiers should have correct suffix
dotnet_diagnostic.CA1710.severity = none

# Identifiers should not have incorrect suffix
dotnet_diagnostic.CA1711.severity = none

# Do not prefix enum values with type name
dotnet_diagnostic.CA1712.severity = warning

# Events should not have before or after prefix
dotnet_diagnostic.CA1713.severity = warning

# Flags enums should have plural names
dotnet_diagnostic.CA1714.severity = none

# Identifiers should not match keywords
dotnet_diagnostic.CA1716.severity = warning

# Only FlagsAttribute enums should have plural names
dotnet_diagnostic.CA1717.severity = none

# Identifiers should not contain type names
dotnet_diagnostic.CA1718.severity = suggestion

# Use PascalCase for named placeholders with ILogger
dotnet_diagnostic.CA1727.severity = none

# Call GC.SuppressFinalize correctly
dotnet_diagnostic.CA1816.severity = warning

# Rethrow to preserve stack details
dotnet_diagnostic.CA2200.severity = warning

# Disposable fields should be disposed
dotnet_diagnostic.CA2213.severity = suggestion

# Do not call overridable methods in constructors
dotnet_diagnostic.CA2214.severity = error

# Dispose methods should call base class dispose
dotnet_diagnostic.CA2215.severity = warning

# Disposable types should declare finalizer
dotnet_diagnostic.CA2216.severity = warning

# Operator overloads have named alternates
dotnet_diagnostic.CA2225.severity = none

# Collection properties should be read only
dotnet_diagnostic.CA2227.severity = none

# Overload operator equals on overriding ValueType.Equals
dotnet_diagnostic.CA2231.severity = none

# Pass System.Uri objects instead of strings
dotnet_diagnostic.CA2234.severity = none

# Mark ISerializable types with SerializableAttribute
dotnet_diagnostic.CA2237.severity = warning

# Attribute string literals should parse correctly
dotnet_diagnostic.CA2243.severity = none

# Do not assign a property to itself
dotnet_diagnostic.CA2245.severity = error

# Argument passed to TaskCompletionSource constructor should be TaskCreationOptions enum instead of TaskContinuationOptions enum
dotnet_diagnostic.CA2247.severity = warning

# Consider using String.Contains instead of String.IndexOf
dotnet_diagnostic.CA2249.severity = error

# Use ThrowIfCancellationRequested
dotnet_diagnostic.CA2250.severity = suggestion

# Use String.Equals over String.Compare
dotnet_diagnostic.CA2251.severity = error

# Template should be a static expression
dotnet_diagnostic.CA2254.severity = suggestion

# The ModuleInitializer attribute should not be used in libraries
dotnet_diagnostic.CA2255.severity = none

# Dispose objects before losing scope
dotnet_diagnostic.CA2000.severity = warning

# Do not directly await a Task
dotnet_diagnostic.CA2007.severity = warning

# Do not call ToImmutableCollection on an ImmutableCollection value
dotnet_diagnostic.CA2009.severity = warning

# Do not assign property within its setter
dotnet_diagnostic.CA2011.severity = error

# Do not use ReferenceEquals with value types
dotnet_diagnostic.CA2013.severity = error

# Do not use stackalloc in loops
dotnet_diagnostic.CA2014.severity = error

# Forward the CancellationToken parameter to methods that take one
dotnet_diagnostic.CA2016.severity = suggestion

# Parameter count mismatch
dotnet_diagnostic.CA2017.severity = error

# Types that own disposable fields should be disposable
dotnet_diagnostic.CA1001.severity = warning

# Define accessors for attribute arguments
dotnet_diagnostic.CA1019.severity = warning

# Avoid out parameters
dotnet_diagnostic.CA1021.severity = none

# Use properties where appropriate
dotnet_diagnostic.CA1024.severity = none

# Mark enums with FlagsAttribute
dotnet_diagnostic.CA1027.severity = none

# Do not catch general exception types
dotnet_diagnostic.CA1031.severity = suggestion

# Implement standard exception constructors
dotnet_diagnostic.CA1032.severity = warning

# Avoid empty interfaces
dotnet_diagnostic.CA1040.severity = suggestion

# Declare types in namespaces
dotnet_diagnostic.CA1050.severity = warning

# Static holder types should be Static or NotInheritable
dotnet_diagnostic.CA1052.severity = suggestion

# URI parameters should not be strings
dotnet_diagnostic.CA1054.severity = none

# URI return values should not be strings
dotnet_diagnostic.CA1055.severity = none

# URI properties should not be strings
dotnet_diagnostic.CA1056.severity = none

# Enums should not have duplicate values
dotnet_diagnostic.CA1069.severity = error
```
</details>

<details>
<summary><b>Editor config for .NET Framework</b></summary>

```
# Naming rules

dotnet_naming_rule.interface_should_be_begins_with_i.severity = suggestion
dotnet_naming_rule.interface_should_be_begins_with_i.symbols = interface
dotnet_naming_rule.interface_should_be_begins_with_i.style = begins_with_i

dotnet_naming_rule.types_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.types_should_be_pascal_case.symbols = types
dotnet_naming_rule.types_should_be_pascal_case.style = pascal_case

dotnet_naming_rule.non_field_members_should_be_pascal_case.severity = suggestion
dotnet_naming_rule.non_field_members_should_be_pascal_case.symbols = non_field_members
dotnet_naming_rule.non_field_members_should_be_pascal_case.style = pascal_case

# Symbol specifications

dotnet_naming_symbols.interface.applicable_kinds = interface
dotnet_naming_symbols.interface.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.interface.required_modifiers =

dotnet_naming_symbols.types.applicable_kinds = class, struct, interface, enum
dotnet_naming_symbols.types.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.types.required_modifiers =

dotnet_naming_symbols.non_field_members.applicable_kinds = property, event, method
dotnet_naming_symbols.non_field_members.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.non_field_members.required_modifiers =

# Naming styles

dotnet_naming_style.begins_with_i.required_prefix = I
dotnet_naming_style.begins_with_i.required_suffix =
dotnet_naming_style.begins_with_i.word_separator =
dotnet_naming_style.begins_with_i.capitalization = pascal_case

dotnet_naming_style.pascal_case.required_prefix =
dotnet_naming_style.pascal_case.required_suffix =
dotnet_naming_style.pascal_case.word_separator =
dotnet_naming_style.pascal_case.capitalization = pascal_case

dotnet_naming_style.pascal_case.required_prefix =
dotnet_naming_style.pascal_case.required_suffix =
dotnet_naming_style.pascal_case.word_separator =
dotnet_naming_style.pascal_case.capitalization = pascal_case
dotnet_style_operator_placement_when_wrapping = beginning_of_line
tab_width = 4
indent_size = 4
end_of_line = crlf
dotnet_style_coalesce_expression = true:suggestion
dotnet_style_null_propagation = true:warning
dotnet_style_prefer_is_null_check_over_reference_equality_method = true:warning
dotnet_style_prefer_auto_properties = true:silent
dotnet_style_object_initializer = true:silent
dotnet_style_collection_initializer = true:silent
dotnet_style_prefer_simplified_boolean_expressions = true:suggestion
dotnet_style_prefer_conditional_expression_over_assignment = true:suggestion
dotnet_style_prefer_conditional_expression_over_return = true:suggestion
dotnet_style_explicit_tuple_names = true:warning
dotnet_style_prefer_inferred_tuple_names = false:suggestion
dotnet_style_prefer_inferred_anonymous_type_member_names = false:suggestion
dotnet_style_prefer_compound_assignment = true:silent
dotnet_style_prefer_simplified_interpolation = true:suggestion
dotnet_style_namespace_match_folder = true:suggestion
dotnet_style_readonly_field = true:suggestion
dotnet_style_predefined_type_for_locals_parameters_members = true:silent
dotnet_style_predefined_type_for_member_access = true:silent
dotnet_style_require_accessibility_modifiers = always:warning
dotnet_style_allow_multiple_blank_lines_experimental = true:silent
dotnet_style_allow_statement_immediately_after_block_experimental = true:silent
dotnet_code_quality_unused_parameters = non_public:error
dotnet_style_parentheses_in_arithmetic_binary_operators = always_for_clarity:silent
dotnet_style_parentheses_in_other_binary_operators = always_for_clarity:silent
dotnet_style_parentheses_in_relational_binary_operators = always_for_clarity:silent
dotnet_style_parentheses_in_other_operators = never_if_unnecessary:silent
dotnet_style_qualification_for_field = true:warning
dotnet_style_qualification_for_property = true:warning
dotnet_style_qualification_for_method = true:warning
dotnet_style_qualification_for_event = true:warning

[*.{cs}]

# Define the 'private_fields' symbol group:
dotnet_naming_symbols.private_fields.applicable_kinds = field
dotnet_naming_symbols.private_fields.applicable_accessibilities = private

# Define the 'private_static_fields' symbol group
dotnet_naming_symbols.private_static_fields.applicable_kinds = field
dotnet_naming_symbols.private_static_fields.applicable_accessibilities = private
dotnet_naming_symbols.private_static_fields.required_modifiers = static

# Define the 'underscored' naming style
dotnet_naming_style.underscored.capitalization = camel_case
dotnet_naming_style.underscored.required_prefix = _

# Define the 'private_fields_underscored' naming rule
dotnet_naming_rule.private_fields_underscored.symbols = private_fields
dotnet_naming_rule.private_fields_underscored.style = underscored
dotnet_naming_rule.private_fields_underscored.severity = error

# Define the 'private_static_fields_none' naming rule
dotnet_naming_rule.private_static_fields_none.symbols = private_static_fields
dotnet_naming_rule.private_static_fields_none.style = underscored
dotnet_naming_rule.private_static_fields_none.severity = none

[*.cs]
csharp_using_directive_placement = outside_namespace:silent
csharp_prefer_simple_using_statement = true:suggestion
csharp_prefer_braces = true:error
csharp_style_namespace_declarations = file_scoped:error
csharp_style_prefer_method_group_conversion = true:suggestion
csharp_style_prefer_top_level_statements = true:silent
csharp_style_expression_bodied_methods = when_on_single_line:suggestion
csharp_style_expression_bodied_constructors = when_on_single_line:suggestion
csharp_style_expression_bodied_operators = when_on_single_line:suggestion
csharp_style_expression_bodied_properties = when_on_single_line:suggestion
csharp_style_expression_bodied_indexers = when_on_single_line:suggestion
csharp_indent_labels = one_less_than_current
csharp_style_expression_bodied_accessors = when_on_single_line:suggestion
csharp_style_expression_bodied_lambdas = when_on_single_line:suggestion
csharp_style_expression_bodied_local_functions = when_on_single_line:suggestion
csharp_style_throw_expression = true:suggestion
csharp_style_prefer_null_check_over_type_check = true:suggestion
csharp_prefer_simple_default_expression = true:suggestion
csharp_style_prefer_local_over_anonymous_function = true:suggestion
csharp_style_prefer_index_operator = true:suggestion
csharp_style_prefer_range_operator = true:suggestion
csharp_style_implicit_object_creation_when_type_is_apparent = true:suggestion
csharp_style_prefer_tuple_swap = true:suggestion
csharp_style_prefer_utf8_string_literals = true:suggestion
csharp_style_inlined_variable_declaration = false:suggestion
csharp_style_deconstructed_variable_declaration = true:suggestion
csharp_style_unused_value_assignment_preference = discard_variable:suggestion
csharp_style_unused_value_expression_statement_preference = discard_variable:silent
csharp_prefer_static_local_function = true:warning
csharp_style_prefer_readonly_struct = true:suggestion
csharp_style_allow_embedded_statements_on_same_line_experimental = true:silent
csharp_style_allow_blank_lines_between_consecutive_braces_experimental = true:silent
csharp_style_allow_blank_line_after_colon_in_constructor_initializer_experimental = true:silent
csharp_style_allow_blank_line_after_token_in_conditional_expression_experimental = true:silent
csharp_style_allow_blank_line_after_token_in_arrow_expression_clause_experimental = true:silent
csharp_style_conditional_delegate_call = true:suggestion
csharp_style_prefer_switch_expression = true:suggestion
csharp_style_prefer_pattern_matching = true:silent
csharp_style_pattern_matching_over_is_with_cast_check = true:suggestion
csharp_style_pattern_matching_over_as_with_null_check = true:suggestion
csharp_style_prefer_not_pattern = true:suggestion
csharp_style_prefer_extended_property_pattern = true:suggestion
csharp_style_var_for_built_in_types = false:error
csharp_style_var_when_type_is_apparent = false:error
csharp_style_var_elsewhere = false:error

csharp_space_around_binary_operators = before_and_after

# Code analysis rules

# The cref tag in an XML documentation comment uses a prefix.
dotnet_diagnostic.CA1200.severity = none

# Do not pass literals as localized parameters
dotnet_diagnostic.CA1303.severity = none

dotnet_diagnostic.CA1304.severity = suggestion

dotnet_diagnostic.CA1305.severity = suggestion

# Specify StringComparison for clarity when comparing string
dotnet_diagnostic.CA1307.severity = suggestion

# Normalize strings to uppercase
dotnet_diagnostic.CA1308.severity = none

# Use ordinal StringComparison when comparing string
dotnet_diagnostic.CA1309.severity = suggestion

# Specify StringComparison for correctness when comparing string
dotnet_diagnostic.CA1310.severity = suggestion

# Specify a culture or use an invariant version for string to upper or to lower
dotnet_diagnostic.CA1311.severity = none

# Platform Invocation Services related method should not be exposed
dotnet_diagnostic.CA1401.severity = error

# The analyzer is enabled by default only for projects that target .NET 5 or later and have an AnalysisLevel of 5 or higher. It can be enabled for target frameworks lower than net5.0 by adding the following config
dotnet_code_quality.enable_platform_analyzer_on_pre_net5_target = true

# Validate platform compatibility for obsoleted APIs
dotnet_diagnostic.CA1422.severity = suggestion

# Avoid excessive inheritance (5 or more levels)
dotnet_diagnostic.CA1501.severity = suggestion

# Avoid excessive cyclomatic complexity
dotnet_diagnostic.CA1502.severity = warning

# Avoid low maintainability index value code
dotnet_diagnostic.CA1505.severity = suggestion

# Avoid excessive class coupling
dotnet_diagnostic.CA1506.severity = suggestion

# Avoid dead conditional code
dotnet_diagnostic.CA1508.severity = warning

# Invalid entry in code metrics configuration file
dotnet_diagnostic.CA1509.severity = error

# Avoid redundant length argument
dotnet_diagnostic.CA1514.severity = warning

# Do not name enum values 'Reserved'
dotnet_diagnostic.CA1700.severity = warning

# Identifiers should not contain underscores
dotnet_diagnostic.CA1707.severity = warning

# Identifiers should differ by more than case
dotnet_diagnostic.CA1708.severity = warning

# Identifiers should have correct suffix
dotnet_diagnostic.CA1710.severity = none

# Identifiers should not have incorrect suffix
dotnet_diagnostic.CA1711.severity = none

# Do not prefix enum values with type name
dotnet_diagnostic.CA1712.severity = warning

# Events should not have before or after prefix
dotnet_diagnostic.CA1713.severity = warning

# Flags enums should have plural names
dotnet_diagnostic.CA1714.severity = none

# Identifiers should not match keywords
dotnet_diagnostic.CA1716.severity = warning

# Only FlagsAttribute enums should have plural names
dotnet_diagnostic.CA1717.severity = none

# Identifiers should not contain type names
dotnet_diagnostic.CA1718.severity = suggestion

# Use PascalCase for named placeholders with ILogger
dotnet_diagnostic.CA1727.severity = none

# Call GC.SuppressFinalize correctly
dotnet_diagnostic.CA1816.severity = warning

# Rethrow to preserve stack details
dotnet_diagnostic.CA2200.severity = warning

# Disposable fields should be disposed
dotnet_diagnostic.CA2213.severity = suggestion

# Do not call overridable methods in constructors
dotnet_diagnostic.CA2214.severity = error

# Dispose methods should call base class dispose
dotnet_diagnostic.CA2215.severity = warning

# Disposable types should declare finalizer
dotnet_diagnostic.CA2216.severity = warning

# Operator overloads have named alternates
dotnet_diagnostic.CA2225.severity = none

# Collection properties should be read only
dotnet_diagnostic.CA2227.severity = none

# Overload operator equals on overriding ValueType.Equals
dotnet_diagnostic.CA2231.severity = none

# Pass System.Uri objects instead of strings
dotnet_diagnostic.CA2234.severity = none

# Mark ISerializable types with SerializableAttribute
dotnet_diagnostic.CA2237.severity = warning

# Attribute string literals should parse correctly
dotnet_diagnostic.CA2243.severity = none

# Do not assign a property to itself
dotnet_diagnostic.CA2245.severity = error

# Argument passed to TaskCompletionSource constructor should be TaskCreationOptions enum instead of TaskContinuationOptions enum
dotnet_diagnostic.CA2247.severity = warning

# Consider using String.Contains instead of String.IndexOf
dotnet_diagnostic.CA2249.severity = error

# Use ThrowIfCancellationRequested
dotnet_diagnostic.CA2250.severity = suggestion

# Use String.Equals over String.Compare
dotnet_diagnostic.CA2251.severity = error

# Template should be a static expression
dotnet_diagnostic.CA2254.severity = suggestion

# The ModuleInitializer attribute should not be used in libraries
dotnet_diagnostic.CA2255.severity = none

# Dispose objects before losing scope
dotnet_diagnostic.CA2000.severity = warning

# Do not directly await a Task
dotnet_diagnostic.CA2007.severity = warning

# Do not call ToImmutableCollection on an ImmutableCollection value
dotnet_diagnostic.CA2009.severity = warning

# Do not assign property within its setter
dotnet_diagnostic.CA2011.severity = error

# Do not use ReferenceEquals with value types
dotnet_diagnostic.CA2013.severity = error

# Do not use stackalloc in loops
dotnet_diagnostic.CA2014.severity = error

# Forward the CancellationToken parameter to methods that take one
dotnet_diagnostic.CA2016.severity = suggestion

# Parameter count mismatch
dotnet_diagnostic.CA2017.severity = error

# Types that own disposable fields should be disposable
dotnet_diagnostic.CA1001.severity = warning

# Define accessors for attribute arguments
dotnet_diagnostic.CA1019.severity = warning

# Avoid out parameters
dotnet_diagnostic.CA1021.severity = none

# Use properties where appropriate
dotnet_diagnostic.CA1024.severity = none

# Mark enums with FlagsAttribute
dotnet_diagnostic.CA1027.severity = none

# Do not catch general exception types
dotnet_diagnostic.CA1031.severity = suggestion

# Implement standard exception constructors
dotnet_diagnostic.CA1032.severity = warning

# Avoid empty interfaces
dotnet_diagnostic.CA1040.severity = suggestion

# Declare types in namespaces
dotnet_diagnostic.CA1050.severity = warning

# Static holder types should be Static or NotInheritable
dotnet_diagnostic.CA1052.severity = suggestion

# URI parameters should not be strings
dotnet_diagnostic.CA1054.severity = none

# URI return values should not be strings
dotnet_diagnostic.CA1055.severity = none

# URI properties should not be strings
dotnet_diagnostic.CA1056.severity = none

# Enums should not have duplicate values
dotnet_diagnostic.CA1069.severity = error

dotnet_diagnostic.CA1000.severity = warning
dotnet_diagnostic.CA1002.severity = warning
dotnet_diagnostic.CA1003.severity = warning
dotnet_diagnostic.CA1005.severity = warning
dotnet_diagnostic.CA1008.severity = warning
dotnet_diagnostic.CA1010.severity = warning
dotnet_diagnostic.CA1012.severity = warning
dotnet_diagnostic.CA1014.severity = warning
dotnet_diagnostic.CA1016.severity = warning
dotnet_diagnostic.CA1017.severity = warning
dotnet_diagnostic.CA1018.severity = warning
dotnet_diagnostic.CA1028.severity = warning
dotnet_diagnostic.CA1030.severity = warning
dotnet_diagnostic.CA1033.severity = warning
dotnet_diagnostic.CA1034.severity = warning
dotnet_diagnostic.CA1036.severity = warning
dotnet_diagnostic.CA1041.severity = warning
dotnet_diagnostic.CA1043.severity = warning
dotnet_diagnostic.CA1044.severity = warning
dotnet_diagnostic.CA1045.severity = warning
dotnet_diagnostic.CA1046.severity = warning
dotnet_diagnostic.CA1047.severity = warning
dotnet_diagnostic.CA1051.severity = warning
dotnet_diagnostic.CA1053.severity = warning
dotnet_diagnostic.CA1058.severity = warning
dotnet_diagnostic.CA1060.severity = warning
dotnet_diagnostic.CA1061.severity = warning
dotnet_diagnostic.CA1062.severity = warning
dotnet_diagnostic.CA1063.severity = warning
dotnet_diagnostic.CA1064.severity = warning
dotnet_diagnostic.CA1065.severity = warning
dotnet_diagnostic.CA1066.severity = warning
dotnet_diagnostic.CA1067.severity = warning
dotnet_diagnostic.CA1068.severity = warning
dotnet_diagnostic.CA1070.severity = warning
dotnet_diagnostic.CA2101.severity = warning
dotnet_diagnostic.CA1417.severity = warning
dotnet_diagnostic.CA1418.severity = warning
dotnet_diagnostic.CA1419.severity = warning
dotnet_diagnostic.CA1420.severity = warning
dotnet_diagnostic.CA1421.severity = warning
dotnet_diagnostic.CA1507.severity = warning
dotnet_diagnostic.CA1715.severity = warning
dotnet_diagnostic.CA1721.severity = warning
dotnet_diagnostic.CA1724.severity = warning
dotnet_diagnostic.CA1725.severity = warning
dotnet_diagnostic.CA1802.severity = warning
dotnet_diagnostic.CA1805.severity = warning
dotnet_diagnostic.CA1806.severity = warning
dotnet_diagnostic.CA1810.severity = warning
dotnet_diagnostic.CA1812.severity = warning
dotnet_diagnostic.CA1813.severity = warning
dotnet_diagnostic.CA1814.severity = warning
dotnet_diagnostic.CA1815.severity = warning
dotnet_diagnostic.CA1819.severity = warning
dotnet_diagnostic.CA1820.severity = warning
dotnet_diagnostic.CA1821.severity = warning
dotnet_diagnostic.CA1822.severity = warning
dotnet_diagnostic.CA1823.severity = warning
dotnet_diagnostic.CA1824.severity = warning
dotnet_diagnostic.CA1825.severity = warning
dotnet_diagnostic.CA1826.severity = warning
dotnet_diagnostic.CA1827.severity = warning
dotnet_diagnostic.CA1828.severity = warning
dotnet_diagnostic.CA1829.severity = warning
dotnet_diagnostic.CA1830.severity = warning
dotnet_diagnostic.CA1831.severity = warning
dotnet_diagnostic.CA1832.severity = warning
dotnet_diagnostic.CA1833.severity = warning
dotnet_diagnostic.CA1834.severity = warning
dotnet_diagnostic.CA1835.severity = warning
dotnet_diagnostic.CA1836.severity = warning
dotnet_diagnostic.CA1837.severity = warning
dotnet_diagnostic.CA1838.severity = warning
dotnet_diagnostic.CA1839.severity = warning
dotnet_diagnostic.CA1840.severity = warning
dotnet_diagnostic.CA1841.severity = warning
dotnet_diagnostic.CA1842.severity = warning
dotnet_diagnostic.CA1843.severity = warning
dotnet_diagnostic.CA1844.severity = warning
dotnet_diagnostic.CA1845.severity = warning
dotnet_diagnostic.CA1846.severity = warning
dotnet_diagnostic.CA1847.severity = warning
dotnet_diagnostic.CA1848.severity = warning
dotnet_diagnostic.CA1849.severity = warning
dotnet_diagnostic.CA1850.severity = warning
dotnet_diagnostic.CA1851.severity = warning
dotnet_diagnostic.CA1852.severity = warning
dotnet_diagnostic.CA1853.severity = warning
dotnet_diagnostic.CA1854.severity = warning
dotnet_diagnostic.CA1855.severity = warning
dotnet_diagnostic.CA1858.severity = warning
dotnet_diagnostic.CA1859.severity = warning
dotnet_diagnostic.CA1860.severity = warning
dotnet_diagnostic.CA1861.severity = warning
dotnet_diagnostic.CA1864.severity = warning
dotnet_diagnostic.CA1865.severity = warning
dotnet_diagnostic.CA1868.severity = warning
dotnet_diagnostic.CA1869.severity = warning
dotnet_diagnostic.CA1870.severity = warning
dotnet_diagnostic.IL3000.severity = warning
dotnet_diagnostic.IL3001.severity = warning
dotnet_diagnostic.IL3002.severity = warning
dotnet_diagnostic.IL3003.severity = warning
dotnet_diagnostic.CA2002.severity = warning
dotnet_diagnostic.CA2008.severity = warning
dotnet_diagnostic.CA2012.severity = warning
dotnet_diagnostic.CA2015.severity = warning
dotnet_diagnostic.CA2018.severity = warning
dotnet_diagnostic.CA2019.severity = warning
dotnet_diagnostic.CA2020.severity = warning
dotnet_diagnostic.CA2100.severity = warning
dotnet_diagnostic.CA2109.severity = warning
dotnet_diagnostic.CA2119.severity = warning
dotnet_diagnostic.CA2153.severity = warning
dotnet_diagnostic.CA2300.severity = warning
dotnet_diagnostic.CA2301.severity = warning
dotnet_diagnostic.CA2302.severity = warning
dotnet_diagnostic.CA2305.severity = warning
dotnet_diagnostic.CA2310.severity = warning
dotnet_diagnostic.CA2311.severity = warning
dotnet_diagnostic.CA2312.severity = warning
dotnet_diagnostic.CA2315.severity = warning
dotnet_diagnostic.CA2321.severity = warning
dotnet_diagnostic.CA2322.severity = warning
dotnet_diagnostic.CA2326.severity = warning
dotnet_diagnostic.CA2327.severity = warning
dotnet_diagnostic.CA2328.severity = warning
dotnet_diagnostic.CA2329.severity = warning
dotnet_diagnostic.CA2330.severity = warning
dotnet_diagnostic.CA2350.severity = warning
dotnet_diagnostic.CA2351.severity = warning
dotnet_diagnostic.CA2352.severity = warning
dotnet_diagnostic.CA2353.severity = warning
dotnet_diagnostic.CA2354.severity = warning
dotnet_diagnostic.CA2355.severity = warning
dotnet_diagnostic.CA2356.severity = warning
dotnet_diagnostic.CA2361.severity = warning
dotnet_diagnostic.CA2362.severity = warning
dotnet_diagnostic.CA3001.severity = warning
dotnet_diagnostic.CA3002.severity = warning
dotnet_diagnostic.CA3003.severity = warning
dotnet_diagnostic.CA3004.severity = warning
dotnet_diagnostic.CA3005.severity = warning
dotnet_diagnostic.CA3006.severity = warning
dotnet_diagnostic.CA3007.severity = warning
dotnet_diagnostic.CA3008.severity = warning
dotnet_diagnostic.CA3009.severity = warning
dotnet_diagnostic.CA3010.severity = warning
dotnet_diagnostic.CA3011.severity = warning
dotnet_diagnostic.CA3012.severity = warning
dotnet_diagnostic.CA3061.severity = warning
dotnet_diagnostic.CA3075.severity = warning
dotnet_diagnostic.CA3076.severity = warning
dotnet_diagnostic.CA3077.severity = warning
dotnet_diagnostic.CA3147.severity = warning
dotnet_diagnostic.CA5350.severity = warning
dotnet_diagnostic.CA5351.severity = warning
dotnet_diagnostic.CA5358.severity = warning
dotnet_diagnostic.CA5359.severity = warning
dotnet_diagnostic.CA5360.severity = warning
dotnet_diagnostic.CA5361.severity = warning
dotnet_diagnostic.CA5362.severity = warning
dotnet_diagnostic.CA5363.severity = warning
dotnet_diagnostic.CA5364.severity = warning
dotnet_diagnostic.CA5365.severity = warning
dotnet_diagnostic.CA5366.severity = warning
dotnet_diagnostic.CA5367.severity = warning
dotnet_diagnostic.CA5368.severity = warning
dotnet_diagnostic.CA5369.severity = warning
dotnet_diagnostic.CA5370.severity = warning
dotnet_diagnostic.CA5371.severity = warning
dotnet_diagnostic.CA5372.severity = warning
dotnet_diagnostic.CA5373.severity = warning
dotnet_diagnostic.CA5374.severity = warning
dotnet_diagnostic.CA5375.severity = warning
dotnet_diagnostic.CA5376.severity = warning
dotnet_diagnostic.CA5377.severity = warning
dotnet_diagnostic.CA5378.severity = warning
dotnet_diagnostic.CA5379.severity = warning
dotnet_diagnostic.CA5380.severity = warning
dotnet_diagnostic.CA5381.severity = warning
dotnet_diagnostic.CA5382.severity = warning
dotnet_diagnostic.CA5383.severity = warning
dotnet_diagnostic.CA5384.severity = warning
dotnet_diagnostic.CA5385.severity = warning
dotnet_diagnostic.CA5386.severity = warning
dotnet_diagnostic.CA5387.severity = warning
dotnet_diagnostic.CA5388.severity = warning
dotnet_diagnostic.CA5389.severity = warning
dotnet_diagnostic.CA5390.severity = warning
dotnet_diagnostic.CA5391.severity = warning
dotnet_diagnostic.CA5392.severity = warning
dotnet_diagnostic.CA5393.severity = warning
dotnet_diagnostic.CA5394.severity = warning
dotnet_diagnostic.CA5395.severity = warning
dotnet_diagnostic.CA5396.severity = warning
dotnet_diagnostic.CA5397.severity = warning
dotnet_diagnostic.CA5398.severity = warning
dotnet_diagnostic.CA5399.severity = warning
dotnet_diagnostic.CA5400.severity = warning
dotnet_diagnostic.CA5401.severity = warning
dotnet_diagnostic.CA5402.severity = warning
dotnet_diagnostic.CA5403.severity = warning
dotnet_diagnostic.CA5404.severity = warning
dotnet_diagnostic.CA5405.severity = warning
dotnet_diagnostic.CA2201.severity = warning
dotnet_diagnostic.CA2207.severity = warning
dotnet_diagnostic.CA2208.severity = warning
dotnet_diagnostic.CA2211.severity = warning
dotnet_diagnostic.CA2217.severity = warning
dotnet_diagnostic.CA2218.severity = warning
dotnet_diagnostic.CA2219.severity = warning
dotnet_diagnostic.CA2224.severity = warning
dotnet_diagnostic.CA2226.severity = warning
dotnet_diagnostic.CA2229.severity = warning
dotnet_diagnostic.CA2235.severity = warning
dotnet_diagnostic.CA2241.severity = warning
dotnet_diagnostic.CA2242.severity = warning
dotnet_diagnostic.CA2244.severity = warning
dotnet_diagnostic.CA2246.severity = warning
dotnet_diagnostic.CA2248.severity = warning
dotnet_diagnostic.CA2252.severity = warning
dotnet_diagnostic.CA2253.severity = warning
dotnet_diagnostic.CA2256.severity = warning
dotnet_diagnostic.CA2257.severity = warning
dotnet_diagnostic.CA2258.severity = warning
dotnet_diagnostic.CA2259.severity = warning
dotnet_diagnostic.CA2260.severity = warning
```
</details>

### Configuring Maintainability Code Analysis rules

The .NET code-quality analyzers include several code metrics analyzer rules:
- [CA1501](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1501)
- [CA1502](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1502)
- [CA1505](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1505)
- [CA1506](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1505)

These rules use a threshold value for managing codebase, which can be configured in the project as per the requirements, in a `txt` file to be included as an additional file in the project.

Basic configuration:
- Create a text file named ```CodeMetricsConfig.txt```.
- Add the desired threshold to the text file in the following format:

```
CA1502: 10
```

- In the project file (`.csproj`), mark the build action of the configuration file as AdditionalFiles. For example:
```xml
<ItemGroup>
  <AdditionalFiles Include="CodeMetricsConfig.txt" />
</ItemGroup>
```

Note: For more details on configuring the thresholds for a specific analysis rule, please check the official rule document included above.
