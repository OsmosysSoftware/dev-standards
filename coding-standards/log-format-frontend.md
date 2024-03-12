# Log format

## Requirements
To create a common log format that fits the most mobile technologies and aids in debugging:

- Include the severity of the log to understand its importance.
- Include the type of log to segregate between info, error, or warning.
- Include screen or controller where applicable.
- Include a unique ID to trace requests across different components or screens.
- Include source context, which could be a function name, module, or screen name.
- Include relevant data in JSON format, such as user information, activity details, performance metrics, and data changes.
- Facilitate debugging of production issues by providing sufficient information in logs, such as stack traces, error messages, and contextual details.

> **Warning**
> Going against GDPR regulations is an absolute NO

## Proposed solution

``` json
 {"timestamp": "[timestamp]","level": "[level]","severity": "[severity]","sessionId": "[token id]","screenName": "[screen or controller name]","source": "[function/module name]","deviceInfo":"[device name/browser/platform/OS]","data": "[httpMethod, endpoint and paramters]","message": "[log message]","stackTrace": "[stackTrace]"}
```

### Explanation of each component: 

| Component     | Description                                     |
| ------------- | ----------------------------------------------- |
| [timestamp]   | Represents the timestamp when the log entry was created. Use ISO 8601 format, which is widely recognized and provides a standardized representation of date and time (Mandatory) |
| [level]       | Represents the log level, such as INFO, WARN, ERROR, or FATAL (Mandatory) |
| [severity]    | Represents the severity level associated with the log entry (e.g., LOW, MEDIUM, HIGH) (Mandatory) |
| [sessionId]   | Can be logged in user's ID / token / Any unique identifier etc (Optional) |
| [screenName]  | Name of the screen or controller where the log originated (Optional) |
| [source]      | Function name, Module & Sub module names etc. (Mandatory) |
| [deviceInfo]  | For mobile apps, device, version, appVersion. For websites, browser, version and platform. (Mandatory) |
| [data]        | Data related to API such as endpoint, httpMethod and parameters(Optional) |
| [message]     | Contains the log message or description of the event (Mandatory) |
| [stackTrace]  | The stack trace of the exception, providing details about the method calls leading to the exception. It includes file names, line numbers, and method names (Optional) |

Here are some examples - 
``` json
{"timestamp": "2024-05-26T10:15:30.123Z", "level": "INFO", "severity": "LOW", "sessionId": "12345","screenName": "LoginScreen","source": "Authentication","deviceInfo": {"device": "iphone", "version": "17.0", "appVersion":"1.0"},"data": {"httpMethod": "GET", "ednPoint": "/api/example","param":{"email":"abc@example.com"}},"message": "This is an informational log."}
{"timestamp": "2024-05-26T10:15:30.123Z", "level": "WARN", "severity": "LOW", "sessionId": "12as4f5", "screenName": "LoginScreen","deviceInfo": {"browser": "chrome", "version": "122.0.6261", "platform":"linux"},"data": {"httpMethod": "GET", "ednPoint": "/api/example",{"param":"email":"abc@example.com"}},"message": "This is an informational log."}
{"timestamp": "2024-05-26T10:15:30.123Z", "level": "INFO", "severity": "LOW", "sessionId": "12as4f5", "screenName": "LoginScreen","deviceInfo": {"browser": "safari", "version": "122.0.6261", "platform":"windows"},"data": {"httpMethod": "GET", "ednPoint": "/api/example","param":{"email":"abc@example.com"}},"message": "This is an informational log."}
```

## Why `ndjson`?
- Easy to read and parse, with each line representing a standalone JSON object.
- Suitable for streaming and processing large amounts of data.
- Suitable for a lot of data structures in the log, especially if we are logging stack trace. 
- Popular format for logs and works well with ELK and Sentry. 

## External Tool Integration
1. [Sentry](https://sentry.io/welcome/)
2. [ELK](https://www.elastic.co/elastic-stack)
