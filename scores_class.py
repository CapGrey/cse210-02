class Score:
    
    def __init__(self, score = 300):
        self.score = score
        
    def update_score(self, add):
        if add:
            self.score += 100
        else:
            self.score -= 75