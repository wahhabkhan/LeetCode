class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        words = sentence.split()
        for i in range(len(words)):
            word = words[i]
            if word.startswith('$') and word[1:].isdigit():
                price = int(word[1:])
                discounted = price * (100 - discount) / 100.0
                words[i] = "${:.2f}".format(discounted)
        return " ".join(words)
        
