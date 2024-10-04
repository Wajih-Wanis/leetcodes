class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        length = len(skill)
        team_sum = sum(skill)//(length//2)
        if sum(skill)%team_sum != 0:
            return -1
        hashy = dict()
        for d in skill:
            if d in hashy:
                hashy[d]+=1
            else:
                hashy[d]=1
        result = 0
        for k in hashy.keys():
            #print(hashy)
            while hashy[k]>0:
                if not team_sum-k in hashy.keys():
                    return -1
                if hashy[team_sum-k]>0:
                    result += (k*(team_sum-k))
                    hashy[k]-=1
                    hashy[team_sum-k]-=1
                else:
                    return -1
        return result