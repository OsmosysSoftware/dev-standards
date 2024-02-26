# Standard regular expressions to be used across the technologies

1. **Phone number without country code**:
   - Regex: `^\d{6,14}$`
   - Example HTML:
     ```html
     <input type="tel" name="phone" pattern="^\d{6,14}$" required>
     ```

2. **Phone number with Indian country code and Indian mobile number**:
   - Regex: `^\+91[1-9]\d{9}$`
   - Example HTML:
     ```html
     <input type="tel" name="phone" pattern="^\+91[1-9]\d{9}$" required>
     ```
   - Regex (handling multiple formats): `^(\+91|\(\+91\))(\s?)([0-9]+)?(\s?)([0-9]+)?(\s)?([0-9]+)?$`
   - Example formats:
     ```
     +911234567890
     +91 1234567890
     +91 123 456 7890
     +91 12345 67890
     +9112345 67890
     (+91)1234567890
     (+91) 1234567890
     (+91) 123 456 7890
     (+91) 12345 67890
     (+91)12345 67890
     ```

3. **Phone number with any country code + any international mobile number**:
   - Regex: `^\+[1-9]\d{6,14}$`
   - Example HTML:
     ```html
     <input type="tel" name="phone" pattern="^\+[1-9]\d{6,14}$" required>
     ```

4. **Email**:
   - Regex: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
   - Example HTML:
     ```html
     <input type="email" name="email" pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" required>
     ```

5. **Date**:
   - Regex: `^\d{4}-\d{2}-\d{2}$`
   - Example HTML:
     ```html
     <input type="date" name="date" pattern="^\d{4}-\d{2}-\d{2}$" required>
     ```

6. **Time**:
   - Regex: `^([01]?[0-9]|2[0-3]):[0-5][0-9]$`
   - Example HTML:
     ```html
     <input type="time" name="time" pattern="^([01]?[0-9]|2[0-3]):[0-5][0-9]$" required>
     ```

7. **URL**:
   - Regex: `^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$`
   - Example HTML:
     ```html
     <input type="url" name="url" pattern="^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$" required>
     ```

8. **Postal code**:
   - Regex: `^\d{5}(?:[-\s]\d{4})?$`
   - Example HTML:
     ```html
     <input type="text" name="postalcode" pattern="^\d{5}(?:[-\s]\d{4})?$" required>
     ```
