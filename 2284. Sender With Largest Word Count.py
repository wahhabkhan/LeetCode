class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        word_count = {}

        for msg, sender in zip(messages, senders):
            word_count[sender] = word_count.get(sender,0) + len(msg.split())

        return max(word_count.keys(), key = lambda name:(word_count[name], name))
        
