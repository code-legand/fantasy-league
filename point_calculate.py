"""
This module is used to find the total points for a player
"""

def calc_point(record):
    
    #=----------variables for storing detailsa
    player=record[0]
    scored=record[1]
    faced=record[2]
    fours=record[3]
    sixes=record[4]
    bowled=record[5]
    maiden=record[6]
    given=record[7]
    wkts=record[8]
    catches=record[9]
    stumping=record[10]
    ro=record[11]
    
    #-----calculate batting score-----
    two_point_score=int(scored/2)
    half_century_score=int(scored/50)*5
    century_score=int(scored/100)
    try:
        strike_rate=scored/faced
    except:
        strike_rate=0
    if strike_rate>=0.8 and strike_rate<=100:
        strike_score=2
    elif strike_rate>1:
        strike_score=4
    else:
        strike_score=0
    four_score=fours
    six_score=sixes*2
    
    bat_score=two_point_score+half_century_score+century_score+strike_score+four_score+six_score
    
    #-----calculate bowling score-----
    wicket_score=wkts*10
    three_wicket_score=int(wkts/3)*5
    five_wicket_score=int(wkts/5)*10
    overs=int(bowled/6)
    try:
        economy_rate=given/overs
    except:
        economy_rate=0
    if economy_rate>=3.5 and economy_rate<=4.5:
        economy_rate_score=4
    elif economy_rate>=2 and economy_rate<3.5:
        economy_rate_score=7
    elif economy_rate<2:
        economy_rate_score=10
    else:
        economy_rate_score=0
        
    bowl_score=wicket_score+three_wicket_score+five_wicket_score+economy_rate_score
      
    #-----calculate fielding score-----
    field_score=(catches+stumping+ro)*10
    
    total_score=bat_score+bowl_score+field_score
    return total_score

    