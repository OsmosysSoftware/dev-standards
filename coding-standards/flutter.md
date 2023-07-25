# Flutter Coding Standards

## Flutter Coding Style Guidelines
We adapted standards to design and program Flutter, from high-level architectural principles all the way to indentation rules, from Flutter offical git repo :</br>
https://github.com/flutter/flutter/wiki/Style-guide-for-Flutter-repo
## Dart Coding Style Guidelines
Dart Style Guide focuses primarily on Dart-specific conventions: https://dart.dev/effective-dart

## Standard Enforcing Tools

`flutter_lints` `dartfmt`
## **Set up Flutter Linter and Dart Formatter in Android Studio**

### **Flutter Linter:**
Add `flutter_lints` to your pubspec.yaml file as a dev dependency under the dev_dependencies section:
```
dev_dependencies:
  flutter_lints: ^1.0.0
```
run the following command in the terminal to fetch and install the newly added package:
```
flutter pub get
```
**Configure flutter_lints**:</br>
Mac Android Studio: "Preferences/Settings" </br>
Window Android Studio: go to "Languages & Frameworks" > "Dart" > "Lints". Click on the "Configure" link next to the "Package: flutter_lints" option.

**Enable flutter_lints rules**:
In the "Select Dart Lints" window, check the box next to "flutter_lints" to enable its lint rules. Click "OK" to apply the changes.

### **Dart Formatter:**
**Configure and Enable dartfmt**:
In the "Preferences/Settings" window, go to "Languages & Frameworks" > "Dart" > "Enable 'Run 'dartfmt' on save' for .dart files". This will automatically format your Dart code using dartfmt whenever you save a file.

