# The code below shows how to keep one temperature value inside an object
# It explains how to convert the value using two well known formulas
# It helps you practice writing simple methods and returning calculated results
# You can use this structure in small science tools or beginner exercises
'''
الكلاس ده بيخزن درجة حرارة واحدة بالدرجة المئوية.

بيوفر وظيفتين لتحويل درجة الحرارة دي:

يحولها لدرجة فهرنهايت باستخدام المعادلة (C × 9/5) + 32.

يحولها لدرجة كلفن بإضافة 273.15.

بتقدر تستخدمه لو عاوز تحوّل درجة حرارة من مئوي لفهرنهايت أو كلفن بسهولة.
'''

class TemperatureConverter:
    def __init__(self, celsius):        # sets the celsius value
        self.celsius = celsius          # stores temperature in celsius

    def to_fahrenheit(self):            # converts to fahrenheit
        return (self.celsius * 9/5) + 32   # applies conversion formula

    def to_kelvin(self):                # converts to kelvin
        return self.celsius + 273.15       # adds kelvin offset

# Example usage
temp = TemperatureConverter(25)          # creates converter with twenty five celsius
print("Fahrenheit:", temp.to_fahrenheit())
print("Kelvin:", temp.to_kelvin())