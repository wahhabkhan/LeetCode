class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        vol = length * width * height
        
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or vol >= 10**9:
            cat1 = "Bulky"
        else:
            cat1 = None
        if mass >= 100:
            cat2 = "Heavy"
        else:
            cat2 = None

        if cat1 == "Bulky" and cat2 == "Heavy":
            return "Both"
        elif cat1 != "Bulky" and cat2 != "Heavy":
            return "Neither"
        elif cat1 == "Bulky" and cat2 != "Heavy":
            return "Bulky"
        elif cat1 != "Bulky" and cat2 == "Heavy":
            return "Heavy"

        
