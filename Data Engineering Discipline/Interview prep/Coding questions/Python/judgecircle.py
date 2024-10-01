class Solution:
    def judgeCircle(self, moves: str) -> bool:
        L = moves.count("L")
        U = moves.count("U")
        D = moves.count("D")
        R = moves.count("R")

        return L == R and U == D
        
 