def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for i in dice1:
        for j in dice2:
            if i>j:
                dice1_wins +=1
            elif j>i:
                dice2_wins +=1

    return (dice1_wins, dice2_wins)
def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    for candidate_dice in range(len(dices)):
      count=0
      for other_dice in range(len(dices)):
        (x,y)=count_wins(dices[candidate_dice],dices[other_dice])
        if x>y or other_dice==candidate_dice:
          count=count+1
      if count==len(dices):
        return candidate_dice
    return -1
def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    if find_the_best_dice(dices)!=-1:
      strategy["choose_first"]=True
      strategy["first_dice"]=find_the_best_dice(dices)
    else:
      strategy["choose_first"]=False
      for candidate_dice in range(len(dices)):
        for other_dice in range(len(dices)):
           (x,y)=count_wins(dices[candidate_dice],dices[other_dice])
           if y>=x and candidate_dice!=other_dice:
             strategy[candidate_dice]=other_dice
    return strategy
