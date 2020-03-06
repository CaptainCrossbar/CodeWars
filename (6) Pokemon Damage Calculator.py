def calculate_damage(your_type, opponent_type, attack, defense):
    #Super effective checker adn damage calculator
    if your_type == 'fire' and opponent_type == 'grass' or your_type == 'water' and opponent_type == 'fire' or your_type == 'grass' and opponent_type == 'water' or your_type == 'electric' and opponent_type == 'water':
        damage = 50 * (attack / defense ) * 2
    #Not very effective checker and damage calculator
    elif your_type == 'fire' and opponent_type == 'water' or your_type == 'water' and opponent_type == 'grass' or your_type == 'water' and opponent_type == 'electric' or your_type == 'grass' and opponent_type == 'fire':
        damage = 50 * (attack / defense ) * 0.5
    #Check to see if same type and damage calculator
    elif your_type == 'fire' and opponent_type == 'fire' or your_type == 'water' and opponent_type == 'water' or your_type == 'electric' and opponent_type == 'electric' or your_type == 'grass' and opponent_type == 'grass':
        damage = 50 * (attack / defense) * 0.5
    #Neutral effectiveness catch and damage calculator
    else: 
        damage = 50 * (attack / defense ) * 1
    return damage
