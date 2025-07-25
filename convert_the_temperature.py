class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]

if __name__ == "__main__":
    solver = Solution()
    
    print("Celsius: 25.00 -> {}".format(solver.convertTemperature(25.00)))
    print("Celsius: 0.00 -> {}".format(solver.convertTemperature(0.00)))
    print("Celsius: 100.00 -> {}".format(solver.convertTemperature(100.00)))
    print("Celsius: 37.50 -> {}".format(solver.convertTemperature(37.50)))
