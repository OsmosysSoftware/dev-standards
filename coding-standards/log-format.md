# Log format

## Requirements
- To create a common log format which fits the most technologies that we work with 
- Include severity of the log to understand if the roofs on fire
- Include type of log to segregate if its info, error or warning
- Include request/page URL in cases possible. Example: logs of APIs can have API end point whereas logs of UI can have page URL
- Include any unique id to trace-back the request when it flows to different components or pages. Ex: if there’s API that involves multiple micro services or components, have request ID would be helpful to trace-back the request 
- Include source - Could be a function name, module or sub-module name or field name or any scope that conveys the context in which log came from
- Include data - Of type JSON, this can have properties of your convenience like below. And it is  important to note that the specific details to log will vary based on the requirements
- User information - user id & his device information (browser type, OS), session id, login/logout time, any relevant meta data. (No email address or password or any user personal details)
- Activity information - page visits, button clicks, events, file uploads/downloads
- Performance metrics - response time, network speed, database query times etc.,
- Data changes - old/new values of the modified data

> **Warning**
> Going against GDPR regulations is a absolute NO

## Proposed solution

``` json
 {"timestamp": "[timestamp]", "level": "[level]", "severity": "[severity]", "tracebackId": "[unique id]", "httpMethod": "[http method]", "url": "[request/page url]", "source": "[function/module name]", "data": [any relevant data of type JSON], "message": "[log message]", "stackTrace": "[stackTrace]"} 
```

### Explanation of each component: 
- [timestamp] : Represents the timestamp when the log entry was created. Use ISO 8601 format, which is widely recognized and provides a standardized representation of date and time (Mandatory)
- [level] : Represents the log level, such as INFO, WARN, ERROR, or FATAL (Mandatory)
- [severity] : Represents the severity level associated with the log entry (e.g., LOW, MEDIUM, HIGH)  (Mandatory)
- [tracebackId] : A unique identifier associated with the request  (Mandatory)
- [url] : Represents the API end point or Page URL (Optional)
- [httpMethod] : Type of request  (Optional)
- [source] : Function name, Module & Sub module names etc.,  (Mandatory)
- [data] : Any relevant data like user information, activity, performance metrics, data changes etc., (Optional)
- [message] - Contains the log message or description of the event (Mandatory)
- [stackTrace] - The stack trace of the exception, providing details about the method calls leading to the exception. It includes file names, line numbers, and method names (Optional)

Here are some examples - 
``` json
{"timestamp": "2023-05-26T10:15:30.123Z", "level": "INFO", "severity": "LOW", "requestId": "12345", "httpMethod": "GET", "requestUrl": "/api/example", "message": "This is an informational log."}
{"timestamp": "2023-05-26T10:16:30.456Z", "level": "WARNING", "severity": "MED", "requestId": "67890", "httpMethod": "POST", "requestUrl": "/api/example", "message": "This is a warning log."}
{"timestamp": "2023-05-26T10:17:30.789Z", "level": "ERROR", "severity": "HIGH", "requestId": "23456", "httpMethod": "GET", "requestUrl": "/api/example", "message": "This is an error log.", "stackTrace": "Exception occurred at line 42\n\tat com.example.app.MyClass.method1(MyClass.java:42)\n\tat com.example.app.MyClass.method2(MyClass.java:64)"}
{"timestamp": "2023-05-26T10:18:30.012Z", "level": "INFO", "severity": "LOW", "requestId": "54321", "httpMethod": "GET", "requestUrl": "/api/example", "message": "Another informational log."}
{"timestamp": "2023-05-26T10:19:30.345Z", "level": "ERROR", "severity": "HIGH", "requestId": "98765", "httpMethod": "POST", "requestUrl": "/api/example", "message": "This is an error log with a multiline stack trace.", "stackTrace": "Exception occurred at line 42\n\tat com.example.app.MyClass.method1(MyClass.java:42)\n\tat com.example.app.MyClass.method2(MyClass.java:64)\nCaused by: NullPointerException\n\tat com.example.app.MyClass.method3(MyClass.java:85)\n\t..."}
{"timestamp": "2023-05-26T10:20:30.678Z", "level": "INFO", "severity": "LOW", "requestId": "24680", "httpMethod": "GET", "requestUrl": "/api/example", "message": "Yet another informational log."}
{"timestamp": "2023-05-26T10:21:30.901Z", "level": "ERROR", "severity": "HIGH", "requestId": "13579", "httpMethod": "POST", "requestUrl": "/api/example", "message": "This is an error log with a multiline stack trace.", "stackTrace": "Exception occurred at line 42\n\tat com.example.app.MyClass.method1(MyClass.java:42)\n\tat com.example.app.MyClass.method2(MyClass.java:64)\nCaused by: RuntimeException\n\tat com.example.app.MyClass.method4(MyClass.java:102)\n\t..."}
{"timestamp": "2023-05-26T10:22:31.234Z", "level": "INFO", "severity": "LOW", "requestId": "31415", "httpMethod": "GET", "requestUrl": "/api/example", "message": "Another informational log."}
```

## Why `ndjson`?
- Easy to read and parse, with each line representing a standalone JSON object.
- Suitable for streaming and processing large amounts of data.
- Suitable for a lot of data structures in the log, especially if we are logging stack trace. 
- Popular format for logs and works well with ELK. 