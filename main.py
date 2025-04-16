import random 
import sys
import time
import ru_local as ru

riddles = [
    {
        "text": ru.RIDDLE_1,
        "answers": ru.ANSWERS_1
    },
    {
        "text": ru.RIDDLE_2,
        "answers": ru.ANSWERS_2
    },
    {
        "text": ru.RIDDLE_3,
        "answers": ru.ANSWERS_3
    },
    {
        "text": ru.RIDDLE_4,
        "answers": ru.ANSWERS_4
    },
    {
        "text": ru.RIDDLE_5,
        "answers": ru.ANSWERS_5
    },
    {
        "text": ru.RIDDLE_6,
        "answers": ru.ANSWERS_6
    }
]

PLAYER_START_MONEY = 500
VAULT_ATTEMPTS = 9


def slow_print(text, delay=0.02):
    """
    Types the output slowly
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def generate_skills():
    """
    Generates random skill point amount for every ability

    :return: dictionary with skill points
    """
    total_points = 10
    skills = {
        ru.HIDDEN: 0,
        ru.STRENGTH: 0,
        ru.INTELLECT: 0,
        ru.AGILITY: 0
    }
    while total_points > 0:
        skill = random.choice(list(skills.keys()))
        if skills[skill] < 5:
            skills[skill] += 1
            total_points -= 1
    return skills


def check_skill(skills, skill):
    """
    Checks the success by comparing skill points with a random number

    :param skills: dictionary with skills
    :param skill: name of tested skill
    :return: True, if success, else False.
    """
    return random.randint(1, 6) <= skills[skill]


def choose_entry(team_name, skills):
    """
    Suggests entry way

    :param team_name: team name
    :param skills: dictionary with words
    :return: entry way
    """
    slow_print(ru.ENTRY_CHOICE_PROMPT.format(team=team_name))
    slow_print(ru.ENTRY_OPTION_1)
    slow_print(ru.ENTRY_OPTION_2)
    slow_print(ru.ENTRY_OPTION_3)
    choice = input(ru.ENTRY_INPUT_PROMPT)
    print()

    if choice in ["1", "2", "3"]:
        return choice
    else:
        slow_print(ru.ENTRY_INVALID_CHOICE)
        return choose_entry(team_name, skills)


def evaluate_outcome(team_name, path):
    """
    Оценивает и выводит итоговый результат для команды по полученному пути.

    :param team_name: Имя команды.
    :param path: Список итоговых результатов этапов.
    :return: Итоговая строка (например, "ННН", "УУН" и пр.).
    """
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
    """
    Обрабатывает события для маршрута главного входа по этапам.
    
    :param team_name: Имя команды.
    :param skills: Словарь с навыками команды.
    :param stage: Номер этапа.
    :param path: Список результатов этапов.
    :return: Обновлённый путь.
    """
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
    """
    Обрабатывает события для маршрута вентиляции по этапам.
    
    :param team_name: Имя команды.
    :param skills: Словарь с навыками команды.
    :param stage: Номер этапа.
    :param path: Список результатов этапов.
    :return: Обновлённый путь.
    """
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
    """
    Обрабатывает события для маршрута служебного входа по этапам.
    
    :param team_name: Имя команды.
    :param skills: Словарь с навыками команды.
    :param stage: Номер этапа.
    :param path: Список результатов этапов.
    :return: Обновлённый путь.
    """
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
        print()
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


def update_skills_after_vault(skills, outcomes):
    """
    Обновляет навыки команды после испытания в хранилище по результатам.
    
    :param skills: Словарь с навыками.
    :param outcomes: Список итогов (символ "У" – успех, "Н" – неудача).
    :return: Обновлённый словарь навыков.
    """
    success_count = outcomes.count("У")
    failure_count = outcomes.count("Н")
    any_zero = any(value == 0 for value in skills.values())
    if success_count == 3 or (success_count == 1 and failure_count == 2 and any_zero):
        for key in skills:
            skills[key] += 1
        if any(value == 5 for value in skills.values()):
            random_skill = random.choice(list(skills.keys()))
            skills[random_skill] += 1
    elif success_count == 1 and failure_count == 2:
        for key in skills:
            if skills[key] > 0:
                skills[key] -= 1
            else:
                for k in skills:
                    skills[k] += 1
                if any(value == 5 for value in skills.values()):
                    random_skill = random.choice(list(skills.keys()))
                    skills[random_skill] += 1
                break
    return skills


def solve_riddle(riddles, team_name, team_player_money):
    """
    Предлагает игроку разгадать загадку из списка. При правильном ответе выдаёт случайное вознаграждение,
    списывая его со счёта хранилища; иначе, штрафует на 200 монет.
    
    :param riddles: Список загадок.
    :param team_name: Имя команды.
    :param team_player_money: Словарь личных денег команд.
    :param team_storage: Словарь денег хранилища команд.
    :return: "У" при успехе, "Н" при неудаче.
    """
    slow_print(ru.VAULT_RIDDLE_INTRO)
    if riddles:
        riddle = random.choice(riddles)
        riddles.remove(riddle)
        slow_print(riddle["text"])
    else:
        slow_print(ru.VAULT_NO_RIDDLES)
        return "Н"
    user_answer = input(ru.VAULT_RIDDLE_ANSWER_PROMPT).strip().lower()
    if user_answer in riddle["answers"]:
        earned = random.randint(250, 500)
        team_player_money[team_name] += earned
       
        slow_print(ru.RIDDLE_SUCCESSFUL_WITH_REWARD.format(earned=earned))
        return "У"
    else:
        slow_print(ru.RIDDLE_FAILED_WITH_PENALTY.format(answers=riddle["answers"], penalty=200))
        team_player_money[team_name] -= 200
        return "Н"


def talk_to_guard(skills, team_name, team_player_money):
    """
    Имитация разговора с охранником в хранилище.
    При успешной проверке выдаёт вознаграждение, иначе – списывает 70% личных денег.
    
    :param skills: Словарь с навыками.
    :param team_name: Имя команды.
    :param team_player_money: Словарь личных денег команд.
    :param team_storage: Словарь денег хранилища команд.
    :return: "У" при успехе, "Н" при неудаче.
    """
    slow_print(ru.GUARD_INTRO)
    if (check_skill(skills, ru.INTELLECT) and check_skill(skills, ru.AGILITY) and
            check_skill(skills, ru.STRENGTH) and check_skill(skills, ru.HIDDEN)):
        reward = random.randint(2500, 3000)
        slow_print(ru.GUARD_TALK_REWARD.format(reward=reward))
        team_player_money[team_name] += reward
       
        return "У"
    else:
        lost = int(team_player_money[team_name] * 0.7)
        slow_print(ru.GUARD_TRICKED_LOSS.format(lost=lost))
        team_player_money[team_name] -= lost

        return "Н"


def interfere_with_team(team_name, skills, team_player_money):
    """
    Имитация вмешательства в действия другой команды. В зависимости от выбора и проверки навыка,
    команда ворует деньги или теряет их.
    
    :param team_name: Имя команды.
    :param skills: Словарь с навыками.
    :param team_player_money: Словарь личных денег команд.
    :return: "У" при успехе, "Н" при неудаче.
    """
    slow_print(ru.INTERFERE_TEAM_TITLE)
    slow_print(ru.INTERFERE_TEAM_OPTION1)
    slow_print(ru.INTERFERE_TEAM_OPTION2)
    slow_print(ru.INTERFERE_TEAM_OPTION3)
    choice = input(ru.INTERFERE_TEAM_PROMPT.format(team=team_name))
    print()
    if choice == "1":
        if check_skill(skills, ru.HIDDEN):
            stolen = int(0.3 * team_player_money[team_name])
            slow_print(ru.SUCCESSFUL_THEFT.format(stolen=stolen))
            team_player_money[team_name] += stolen
            return "У"
        else:
            lost = int(0.2 * team_player_money[team_name])
            slow_print(ru.INTERFERE_TEAM_FAIL_OPTION1.format(lost=lost))
            team_player_money[team_name] -= lost
            return "Н"
    elif choice == "2":
        if check_skill(skills, ru.STRENGTH):
            reward = int(0.2 * team_player_money[team_name])
            slow_print(ru.INTERFERE_TEAM_SUCCESS_OPTION2.format(reward=reward))
            team_player_money[team_name] += reward
            return "У"
        else:
            lost = int(0.2 * team_player_money[team_name])
            slow_print(ru.INTERFERE_TEAM_FAIL_OPTION2.format(lost=lost))
            team_player_money[team_name] -= lost
            return "Н"
    else:
        if check_skill(skills, ru.INTELLECT):
            convinced = int(0.3 * team_player_money[team_name])
            slow_print(ru.INTERFERE_TEAM_SUCCESS_OPTION3.format(convinced=convinced))
            team_player_money[team_name] += convinced
            return "У"
        else:
            lost = int(0.2 * team_player_money[team_name])
            slow_print(ru.INTERFERE_TEAM_FAIL_OPTION3.format(lost=lost))
            team_player_money[team_name] -= lost
            return "Н"


def run_vault(participating_teams, skills, team_player_money):
    """
    Реализует обход участвующих команд в зоне хранилища.
    Все команды ходят по кругу (round-robin). Как только суммарно совершено 9 корректных действий,
    завершается испытание, после чего выводится итоговый счет для каждой команды.
    
    :param participating_teams: Список имён команд, участвующих в испытании.
    :param skills: Словарь с навыками команд (ключ — имя команды).
    :param team_player_money: Словарь с личными деньгами команд.
    """
    total_actions = 0
    while total_actions < 9:
        for team in participating_teams:
            if total_actions >= 9:
                break
            slow_print(ru.VAULT_ENTRY_TITLE.format(team=team))
            slow_print(ru.VAULT_PLAYER_MONEY.format(money=team_player_money[team]))
            slow_print(ru.VAULT_CHOOSE_ACTION)
            slow_print(ru.VAULT_ACTION_OPTION1)
            slow_print(ru.VAULT_ACTION_OPTION2)
            slow_print(ru.VAULT_ACTION_OPTION3)
            choice = input(ru.VAULT_ACTION_PROMPT)
            print()
           
            if choice == "1":
                outcome = solve_riddle(riddles, team, team_player_money)
            elif choice == "2":
                outcome = talk_to_guard(skills[team], team, team_player_money)
            elif choice == "3":
                outcome = interfere_with_team(team, skills[team], team_player_money)
            else:
                slow_print(ru.VAULT_INVALID_CHOICE)
                continue
            total_actions += 1

def start_game():
    """
    Инициализирует игру: задаёт команды, показывает начальные навыки,
    предлагает выбор маршрута, проводит этапы и затем организует испытание в зоне хранилища.
    По окончании испытания выводится итоговый счет для каждой команды (в долларах) и объявляется победитель.
    """
    teams = [f"Команда {i+1}" for i in range(3)]
    skills = {team: generate_skills() for team in teams}
    paths = {team: [] for team in teams}
    route_choices = {}
    outcomes = {}


    team_player_money = {team: PLAYER_START_MONEY for team in teams}

    slow_print(ru.GAME_START)
    slow_print(ru.GAME_TEAM_SKILLS)
    print()
    for team in teams:
        slow_print(f"{team}: {skills[team]}")
    slow_print(ru.GAME_ROUTE_CHOICE)

    for team in teams:
        route_choices[team] = choose_entry(team, skills[team])
        slow_print(ru.GAME_TEAM_CHOICE.format(team=team, route=route_choices[team]))
        print("-" * 50)
        print()

    slow_print(ru.GAME_HEIST_START)

    for stage in range(3):
        for team in teams:
            slow_print(ru.GAME_STAGE_PROMPT.format(team=team, stage=stage + 1))
            if route_choices[team] == "1":
                paths[team] = main_entrance(team, skills[team], stage, paths[team])
            elif route_choices[team] == "2":
                paths[team] = ventilation(team, skills[team], stage, paths[team])
            elif route_choices[team] == "3":
                paths[team] = service_entrance(team, skills[team], stage, paths[team])
            print()
            print("-" * 50)
            print()

    slow_print(ru.GAME_OUTCOME_SUMMARY)
    for team in teams:
        outcomes[team] = evaluate_outcome(team, paths[team])


    participating_teams = [team for team in teams if outcomes[team] != "ННН"]

    if participating_teams:
        run_vault(participating_teams, skills, team_player_money)
    else:
        slow_print(ru.NO_VAULT_PARTICIPANTS)


    slow_print(ru.FINAL_TEAM_BALANCE_HEADER)
    for team in teams:
        slow_print(ru.FINAL_TEAM_BALANCE.format(team=team, balance=team_player_money[team]))

  
    participating_accounts = {team: team_player_money[team] for team in teams if outcomes[team] != "ННН"}
    if participating_accounts:
        max_money = max(participating_accounts.values())
        winners = [team for team, money in participating_accounts.items() if money == max_money]
        if len(winners) == 1:
            slow_print(ru.WINNER_ANNOUNCEMENT.format(winner=winners[0]))
        else:
            slow_print(ru.TIE_ANNOUNCEMENT.format(teams=", ".join(winners)))
    else:
        slow_print(ru.NO_WINNER)


if __name__ == "__main__":
    start_game()
