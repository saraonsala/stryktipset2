class MatchResult:
        def __init__(self, result, probability):
                self.result = result
                #self.probability = "{:.2%}".format(probability)
                self.probability = float(probability)
                print(self.result, ":", self.probability)