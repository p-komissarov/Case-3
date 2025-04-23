import random
import sys
import time
import ru_local as ru

PLAYER_START_MONEY = 500
VAULT_ATTEMPTS = 3

riddles = [
    {"text": ru.RIDDLE_1, "answers": ru.ANSWERS_1},
    {"text": ru.RIDDLE_2, "answers": ru.ANSWERS_2},
    {"text": ru.RIDDLE_3, "answers": ru.ANSWERS_3},
    {"text": ru.RIDDLE_4, "answers": ru.ANSWERS_4},
    {"text": ru.RIDDLE_5, "answers": ru.ANSWERS_5},
    {"text": ru.RIDDLE_6, "answers": ru.ANSWERS_6}
]

def slow_print(text, delay=0):

    '''
    Prints text character by character with a delay.

    :param text: The string to print slowly.
    :param delay: Delay in seconds between each character.
    :return: None
    '''

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def generate_skills():

    '''
    Randomly distributes a total of 10 skill points among four attributes.

    :return: Dictionary of skills with their assigned points.
    '''

    total_points = 10
    skills = {ru.HIDDEN: 0, ru.STRENGTH: 0, ru.INTELLECT: 0, ru.AGILITY: 0}
    while total_points > 0:
        skill = random.choice(list(skills.keys()))
        if skills[skill] < 5:
            skills[skill] += 1
            total_points -= 1
    return skills


def check_skill(skills, skill):

    '''
    Checks if a skill test succeeds by comparing a random roll to the skill value.

    :param skills: Dictionary of team's skills.
    :param skill: The skill to test.
    :return: True if roll <= skill value, False otherwise.
    '''

    return random.randint(1, 6) <= skills[skill]


def choose_entry(team_name, skills):

    '''
    Prompts the player to choose an entry route for the team.

    :param team_name: Name of the team.
    :param skills: Dictionary of team's skills (not used in choice logic).
    :return: String representing chosen option ('1', '2', or '3').
    '''

    while True:
        slow_print(ru.ENTRY_CHOICE_PROMPT.format(team=team_name))
        slow_print(ru.ENTRY_OPTION_1)
        slow_print(ru.ENTRY_OPTION_2)
        slow_print(ru.ENTRY_OPTION_3)
        choice = input(ru.ENTRY_INPUT_PROMPT).strip()
        print()
        if choice in ("1", "2", "3"):
            return choice
        slow_print(ru.ENTRY_INVALID_CHOICE)

def evaluate_outcome(team_name, path):

    '''
    Computes and displays the final outcome string for a team based on stage results.

    :param team_name: Name of the team.
    :param path: List of 'У' or 'Н' results for each stage.
    :return: Outcome string (e.g., 'УУН').
    '''

    outcome = "".join(path)
    slow_print(ru.OUTCOME_RESULT.format(team=team_name))
    if outcome == "ННН":
        slow_print(ru.OUTCOME_NNN)
    elif outcome == "УУН":
        slow_print(ru.OUTCOME_UUN)
    else:
        slow_print(ru.OUTCOME_DEFAULT)
    return outcome

def main_entrance(team_name, skills, stage, path):

    '''
    Handles the three stages of the main entrance route for the heist.

    :param team_name: Name of the team.
    :param skills: Dictionary of team's skills.
    :param stage: Current stage index (0-2).
    :param path: List to append the result of this stage ('У' or 'Н').
    :return: Updated path list.
    '''

    if stage == 0:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.MAIN_ENTRANCE_OUTSIDE.format(team=team_name))
        slow_print(ru.MAIN_ENTRANCE_OPTION_1)
        slow_print(ru.MAIN_ENTRANCE_OPTION_2)
        print()
        choice1 = input(ru.MAIN_ENTRANCE_CHOICE_PROMPT.format(team=team_name))
        print()

        if choice1 == "1":
            if check_skill(skills, ru.INTELLECT):
                slow_print(ru.MAIN_ENTRANCE_SUCCESS_INT)
                path.append("У")
            else:
                slow_print(ru.MAIN_ENTRANCE_FAIL_INT)
                path.append("Н")
        else:
            if check_skill(skills, ru.HIDDEN):
                slow_print(ru.MAIN_ENTRANCE_SUCCESS_HIDDEN)
                path.append("У")
            else:
                slow_print(ru.MAIN_ENTRANCE_FAIL_HIDDEN)
                path.append("Н")

    elif stage == 1:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.MAIN_ENTRANCE_INTERIOR)
        slow_print(ru.MAIN_ENTRANCE_OPTION_1_STAGE1)
        slow_print(ru.MAIN_ENTRANCE_OPTION_2_STAGE1)
        print()
        choice2 = input(ru.MAIN_ENTRANCE_CHOICE_PROMPT.format(team=team_name))
        print()

        if choice2 == "1":
            if check_skill(skills, ru.INTELLECT) and check_skill(skills, ru.AGILITY):
                slow_print(ru.MAIN_ENTRANCE_SUCCESS_STAGE1_HACK)
                path.append("У")
            else:
                slow_print(ru.MAIN_ENTRANCE_FAIL_STAGE1_HACK)
                path.append("Н")
        else:
            if check_skill(skills, ru.STRENGTH):
                slow_print(ru.MAIN_ENTRANCE_SUCCESS_STAGE1_STRENGTH)
                path.append("У")
            else:
                slow_print(ru.MAIN_ENTRANCE_FAIL_STAGE1_STRENGTH)
                path.append("Н")

    elif stage == 2:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.MAIN_ENTRANCE_STAGE2_INTRO)
        slow_print(ru.MAIN_ENTRANCE_OPTION_1_STAGE2)
        slow_print(ru.MAIN_ENTRANCE_OPTION_2_STAGE2)
        print()
        choice3 = input(ru.MAIN_ENTRANCE_CHOICE_PROMPT.format(team=team_name))
        print()

        if choice3 == "1":
            if check_skill(skills, ru.INTELLECT):
                slow_print(ru.MAIN_ENTRANCE_SUCCESS_STAGE2_INT)
                path.append("У")
            else:
                slow_print(ru.MAIN_ENTRANCE_FAIL_STAGE2_INT)
                path.append("Н")
        else:
            if check_skill(skills, ru.HIDDEN):
                slow_print(ru.MAIN_ENTRANCE_SUCCESS_STAGE2_HIDDEN)
                path.append("У")
            else:
                slow_print(ru.MAIN_ENTRANCE_FAIL_STAGE2_HIDDEN)
                path.append("Н")
    return path


def ventilation(team_name, skills, stage, path):

    '''
    Handles the three stages of the ventilation route for the heist.

    :param team_name: Name of the team.
    :param skills: Dictionary of team's skills.
    :param stage: Current stage index (0-2).
    :param path: List to append the result of this stage ('У' or 'Н').
    :return: Updated path list.
    '''

    if stage == 0:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.VENTILATION_INTRO.format(team=team_name))
        slow_print(ru.VENTILATION_OPTION_1)
        slow_print(ru.VENTILATION_OPTION_2)
        print()
        choice1 = input(ru.VENTILATION_CHOICE_PROMPT.format(team=team_name))
        print()

        if choice1 == "1":
            if check_skill(skills, ru.STRENGTH):
                slow_print(ru.VENTILATION_SUCCESS_STRENGTH)
                path.append("У")
            else:
                slow_print(ru.VENTILATION_FAIL_STRENGTH)
                path.append("Н")
        else:
            if check_skill(skills, ru.INTELLECT):
                slow_print(ru.VENTILATION_SUCCESS_INT)
                path.append("У")
            else:
                slow_print(ru.VENTILATION_FAIL_INT)
                path.append("Н")

    elif stage == 1:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.VENTILATION_STAGE1_DESC)
        slow_print(ru.VENTILATION_OPTION_1_STAGE1)
        slow_print(ru.VENTILATION_OPTION_2_STAGE1)
        print()
        choice2 = input(ru.VENTILATION_CHOICE_PROMPT_STAGE1.format(team=team_name))
        print()

        if choice2 == "1":
            if check_skill(skills, ru.AGILITY):
                slow_print(ru.VENTILATION_SUCCESS_STAGE1_DEX)
                path.append("У")
            else:
                slow_print(ru.VENTILATION_FAIL_STAGE1_DEX)
                path.append("Н")
        else:
            if check_skill(skills, ru.STRENGTH):
                slow_print(ru.VENTILATION_SUCCESS_STAGE1_STRENGTH)
                path.append("У")
            else:
                slow_print(ru.VENTILATION_FAIL_STAGE1_STRENGTH)
                path.append("Н")

    elif stage == 2:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.VENTILATION_STAGE2_DESC)
        slow_print(ru.VENTILATION_OPTION_1_STAGE2)
        slow_print(ru.VENTILATION_OPTION_2_STAGE2)
        print()
        choice3 = input(ru.VENTILATION_CHOICE_PROMPT_STAGE2.format(team=team_name))
        print()

        if choice3 == "1":
            if check_skill(skills, ru.STRENGTH):
                slow_print(ru.VENTILATION_SUCCESS_STAGE2_STRENGTH)
                path.append("У")
            else:
                slow_print(ru.VENTILATION_FAIL_STAGE2_STRENGTH)
                path.append("Н")
        else:
            if check_skill(skills, ru.INTELLECT):
                slow_print(ru.VENTILATION_SUCCESS_STAGE2_INT)
                path.append("У")
            else:
                slow_print(ru.VENTILATION_FAIL_STAGE2_INT)
                path.append("Н")
    return path


def service_entrance(team_name, skills, stage, path):

    '''
    Handles the three stages of the service entrance route for the heist.

    :param team_name: Name of the team.
    :param skills: Dictionary of team's skills.
    :param stage: Current stage index (0-2).
    :param path: List to append the result of this stage ('У' or 'Н').
    :return: Updated path list.
    '''

    if stage == 0:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.SERVICE_ENTRANCE_INTRO.format(team=team_name))
        slow_print(ru.SERVICE_ENTRANCE_OPTION_1)
        slow_print(ru.SERVICE_ENTRANCE_OPTION_2)
        slow_print(ru.SERVICE_ENTRANCE_OPTION_3)
        print()
        choice1 = input(ru.SERVICE_ENTRANCE_CHOICE_PROMPT.format(team=team_name))
        print()

        if choice1 == "1":
            if check_skill(skills, ru.INTELLECT):
                slow_print(ru.SERVICE_ENTRANCE_SUCCESS_INT)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_FAIL_INT)
                path.append("Н")
        elif choice1 == "2":
            if check_skill(skills, ru.HIDDEN):
                slow_print(ru.SERVICE_ENTRANCE_SUCCESS_HIDDEN)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_FAIL_HIDDEN)
                path.append("Н")
        else:
            if check_skill(skills, ru.STRENGTH):
                slow_print(ru.SERVICE_ENTRANCE_SUCCESS_STRENGTH)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_FAIL_STRENGTH)
                path.append("Н")

    elif stage == 1:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.SERVICE_ENTRANCE_STAGE1_DESC)
        slow_print(ru.SERVICE_ENTRANCE_STAGE1_OPTION_1)
        slow_print(ru.SERVICE_ENTRANCE_STAGE1_OPTION_2)
        slow_print(ru.SERVICE_ENTRANCE_STAGE1_OPTION_3)
        choice2 = input(ru.SERVICE_ENTRANCE_STAGE1_CHOICE_PROMPT.format(team=team_name))
        print()

        if choice2 == "1":
            if check_skill(skills, ru.STRENGTH):
                slow_print(ru.SERVICE_ENTRANCE_STAGE1_SUCCESS_STRENGTH)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_STAGE1_FAIL_STRENGTH)
                path.append("Н")
        elif choice2 == "2":
            if check_skill(skills, ru.HIDDEN):
                slow_print(ru.SERVICE_ENTRANCE_STAGE1_SUCCESS_HIDDEN)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_STAGE1_FAIL_HIDDEN)
                path.append("Н")
        else:
            if check_skill(skills, ru.INTELLECT) and check_skill(skills, ru.AGILITY):
                slow_print(ru.SERVICE_ENTRANCE_STAGE1_SUCCESS_INT_AGI)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_STAGE1_FAIL_INT_AGI)
                path.append("Н")

    elif stage == 2:
        slow_print(ru.CHARACTERISTICS.format(team=team_name))
        for skill, value in skills.items():
            slow_print(ru.SKILL_DISPLAY.format(skill=skill, value=value))
        print()

        slow_print(ru.SERVICE_ENTRANCE_STAGE2_DESC)
        slow_print(ru.SERVICE_ENTRANCE_STAGE2_OPTION_1)
        slow_print(ru.SERVICE_ENTRANCE_STAGE2_OPTION_2)
        slow_print(ru.SERVICE_ENTRANCE_STAGE2_OPTION_3)
        print()
        choice3 = input(ru.SERVICE_ENTRANCE_STAGE2_CHOICE_PROMPT.format(team=team_name))
        print()

        if choice3 == "1":
            if check_skill(skills, ru.INTELLECT):
                slow_print(ru.SERVICE_ENTRANCE_STAGE2_SUCCESS_INT)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_STAGE2_FAIL_INT)
                path.append("Н")
        elif choice3 == "2":
            if check_skill(skills, ru.STRENGTH):
                slow_print(ru.SERVICE_ENTRANCE_STAGE2_SUCCESS_STRENGTH)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_STAGE2_FAIL_STRENGTH)
                path.append("Н")
        else:
            if check_skill(skills, ru.AGILITY) and check_skill(skills, ru.HIDDEN):
                slow_print(ru.SERVICE_ENTRANCE_STAGE2_SUCCESS_AGI_HIDDEN)
                path.append("У")
            else:
                slow_print(ru.SERVICE_ENTRANCE_STAGE2_FAIL_AGI_HIDDEN)
                path.append("Н")
    return path

def update_skills_after_vault(skills: dict, outcomes: list) -> dict:

    '''
    Updates team's skills after the pre-vault stages based on success/failure counts.

    :param skills: Dictionary of team's skills.
    :param outcomes: List of 'У'/'Н' results from stages.
    :return: Updated dictionary of skills.
    '''

    success_count = outcomes.count("У")
    failure_count = outcomes.count("Н")
    any_zero = any(value == 0 for value in skills.values())
    if success_count == 3 or (success_count == 1 and failure_count == 2 and any_zero):
        for k in skills:
            skills[k] += 1
        if any(v == 5 for v in skills.values()):
            skills[random.choice(list(skills.keys()))] += 1
    elif success_count == 1 and failure_count == 2:
        for k in skills:
            if skills[k] > 0:
                skills[k] -= 1
            else:
                for kk in skills:
                    skills[kk] += 1
                if any(v == 5 for v in skills.values()):
                    skills[random.choice(list(skills.keys()))] += 1
                break
    return skills

def solve_riddle(riddles, team_name, team_money):

    '''
    Prompts a riddle challenge in the vault zone.

    :param riddles: List of available riddles.
    :param team_name: Name of the team.
    :param team_money: Dictionary of team's money balances.
    :return: Tuple(delta_money, outcome_char).
    '''

    slow_print(ru.VAULT_RIDDLE_INTRO)
    if riddles:
        riddle = random.choice(riddles)
        riddles.remove(riddle)
        slow_print(riddle["text"])
    else:
        slow_print(ru.VAULT_NO_RIDDLES)
        return 0, "Н"

    answer = input(ru.VAULT_RIDDLE_ANSWER_PROMPT).strip().lower()
    if answer in riddle["answers"]:
        earned = random.randint(250, 500)
        print()
        slow_print(ru.RIDDLE_SUCCESSFUL_WITH_REWARD.format(earned=earned))
        return earned, "У"
    else:
        print()
        slow_print(ru.RIDDLE_FAILED_WITH_PENALTY.format(answers=riddle["answers"], penalty=200))
        return -200, "Н"


def talk_to_guard(skills, team_name):
    
    '''
    Simulates talking to a guard in the vault.

    :param skills: Dictionary of team's skills.
    :param team_name: Name of the team.
    :return: Tuple(delta_money, outcome_char).
    '''

    print()
    slow_print(ru.GUARD_INTRO)
    if all(check_skill(skills, s) for s in [ru.INTELLECT, ru.AGILITY, ru.STRENGTH, ru.HIDDEN]):
        reward = random.randint(2500, 3000)
        print()
        slow_print(ru.GUARD_TALK_REWARD.format(reward=reward))
        return reward, "У"
    else:
        loss = int(PLAYER_START_MONEY * 0.7)
        print()
        slow_print(ru.GUARD_TRICKED_LOSS.format(lost=loss))
        return -loss, "Н"


def interfere_with_team(team_name, skills, current_money):
    
    '''
    Simulates interference action against another team.

    :param team_name: Name of the acting team.
    :param skills: Dictionary of acting team's skills.
    :param current_money: Integer current money of the acting team.
    :return: Tuple(delta_money, outcome_char).
    '''

    slow_print(ru.INTERFERE_TEAM_TITLE)
    slow_print(ru.INTERFERE_TEAM_OPTION1)
    slow_print(ru.INTERFERE_TEAM_OPTION2)
    slow_print(ru.INTERFERE_TEAM_OPTION3)
    choice = input(ru.INTERFERE_TEAM_PROMPT.format(team=team_name)).strip()
    print()
    if choice == "1":
        if check_skill(skills, ru.HIDDEN):
            stolen = int(0.3 * current_money)
            slow_print(ru.SUCCESSFUL_THEFT.format(stolen=stolen))
            return stolen, "У"
        else:
            lost = int(0.2 * current_money)
            slow_print(ru.INTERFERE_TEAM_FAIL_OPTION1.format(lost=lost))
            return -lost, "Н"
    elif choice == "2":
        if check_skill(skills, ru.STRENGTH):
            reward = int(0.2 * current_money)
            slow_print(ru.INTERFERE_TEAM_SUCCESS_OPTION2.format(reward=reward))
            return reward, "У"
        else:
            lost = int(0.2 * current_money)
            slow_print(ru.INTERFERE_TEAM_FAIL_OPTION2.format(lost=lost))
            return -lost, "Н"
    else:
        if check_skill(skills, ru.INTELLECT):
            convinced = int(0.3 * current_money)
            slow_print(ru.INTERFERE_TEAM_SUCCESS_OPTION3.format(convinced=convinced))
            return convinced, "У"
        else:
            lost = int(0.2 * current_money)
            slow_print(ru.INTERFERE_TEAM_FAIL_OPTION3.format(lost=lost))
            return -lost, "Н"


def run_vault(participants, skills, team_money):
    
    '''
    Conducts the vault phase: each participant gets VAULT_ATTEMPTS turns.

    :param participants: List of team names that reached the vault.
    :param skills: Dict mapping team_name to its skill dict.
    :param team_money: Dict of team money balances.
    :return: None
    '''
    
    for team in list(team_money.keys()):
        if team not in participants:
            team_money[team] = 0

    if len(participants) == 1:
        slow_print(ru.WINNER_ANNOUNCEMENT.format(winner=participants[0]))
        return

    entered = set()
    for round_num in range(1, VAULT_ATTEMPTS + 1):
        for team in participants:
            if team not in entered:
                slow_print("\n" + ru.VAULT_ENTRY_TITLE.format(team=team))
                entered.add(team)
            slow_print(ru.CHARACTERISTICS.format(team=team))
            for sk, val in skills[team].items():
                slow_print(ru.SKILL_DISPLAY.format(skill=sk, value=val))
            print()
            
            slow_print(ru.VAULT_PLAYER_MONEY.format(money=team_money[team]))
            print()
            slow_print(ru.VAULT_CHOOSE_ACTION)
            slow_print(ru.VAULT_ACTION_OPTION1)
            slow_print(ru.VAULT_ACTION_OPTION2)
            slow_print(ru.VAULT_ACTION_OPTION3)
            print()
            choice = input(ru.VAULT_ACTION_PROMPT).strip()

            if choice == "1":
                delta, _ = solve_riddle(riddles, team, team_money)
            elif choice == "2":
                delta, _ = talk_to_guard(skills[team], team)
            elif choice == "3":
                delta, _ = interfere_with_team(team, skills[team], team_money[team])
            else:
                slow_print(ru.VAULT_INVALID_CHOICE)
                delta = 0

            team_money[team] += delta

    max_money = max(team_money[t] for t in participants)
    winners = [t for t in participants if team_money[t] == max_money]
    print()
    if len(winners) == 1:
        slow_print(ru.WINNER_ANNOUNCEMENT.format(winner=winners[0]))
    else:
        slow_print(ru.TIE_ANNOUNCEMENT.format(teams=", ".join(winners)))


def start_game():
    
    '''
    Orchestrates the entire game flow: setup, stages, vault, and final results.

    :return: None
    '''

    teams = [ru.TEAM_NAME_TEMPLATE.format(number=i+1) for i in range(3)]
    skills = {team: generate_skills() for team in teams}
    paths = {team: [] for team in teams}
    route_choices = {}
    outcomes = {}
    team_money = {team: PLAYER_START_MONEY for team in teams}

    slow_print(ru.GAME_START)
    slow_print(ru.GAME_TEAM_SKILLS)
    print()
    for team in teams:
        slow_print(f"{team}: {skills[team]}")
    slow_print(ru.GAME_ROUTE_CHOICE)

    for team in teams:
        route_choices[team] = choose_entry(team, skills[team])
        slow_print(ru.GAME_TEAM_CHOICE.format(team=team, route=route_choices[team]))
        print("-" * 50, "\n")

    slow_print(ru.GAME_HEIST_START)

    for stage in range(3):
        for team in teams:
            slow_print(ru.GAME_STAGE_PROMPT.format(team=team, stage=stage + 1))
            if route_choices[team] == "1":
                paths[team] = main_entrance(team, skills[team], stage, paths[team])
            elif route_choices[team] == "2":
                paths[team] = ventilation(team, skills[team], stage, paths[team])
            else:
                paths[team] = service_entrance(team, skills[team], stage, paths[team])
            print("\n" + "-" * 50 + "\n")

    slow_print(ru.GAME_OUTCOME_SUMMARY)

    for team in teams:
        outcomes[team] = evaluate_outcome(team, paths[team])

    participants = [t for t, res in outcomes.items() if res != "ННН"]

    slow_print(ru.VAULT_START)
    print()
    slow_print(ru.NEW_CHARACTERICTICS)

    if participants:
        for team in participants:
            skills[team] = update_skills_after_vault(skills[team], paths[team])
            slow_print(ru.CHARACTERISTICS.format(team=team))
            for sk, val in skills[team].items():
                slow_print(ru.SKILL_DISPLAY.format(skill=sk, value=val))
        run_vault(participants, skills, team_money)
    else:
        slow_print(ru.NO_VAULT_PARTICIPANTS)

    print()
    slow_print(ru.FINAL_TEAM_BALANCE_HEADER)
    print()
    for team in teams:
        slow_print(ru.FINAL_TEAM_BALANCE.format(team=team, balance=team_money[team]))
        print()

if __name__ == "__main__":
    start_game()
