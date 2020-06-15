class GameEntry:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def get_name(self):
        return self.nam
    def get_score(self):
        return self.score
    def __str__(self):
        return '({0},{1}).format(self.name,self.score) '

class Scoreboard:
    def __init__(self,capacity=10):
        self.boadr=[None]*capacity
        self.n=0
        def __getitem__(self,k):
            return self.board[k]
        def __str__(self):
            return '\n'.join(str(str.board[j])for j in range(self.n))
        def add(self,entry):
            score=entry.get_score()
            # Does new entry qualify as a high score?
# answer is yes if board not full or score is higher than last entry

            good = self. n < len(self. board) or score > self. board[−1].get score()
            if good:
                if.self.n<len(self.board):
                    self.n+=1
                    j=self.n-1
                    whilej>0 and self.board[j-1].get_score()<score:
                    self.board[j]=self.board[j-1]
                    j-=1
                    self.board[j]=entry



