import random

class JankenEnv:
    def __init__(self):
        # ステートを定義する
        self.state_names = ["グー", "チョキ", "パー"]
        # アクションを定義する
        self.actions = ["グー", "チョキ", "パー"]
        # 報酬を定義する
        self.rewards = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

    def get_state(self):
        # 現在の状態を返す
        return self.state

    def is_done(self):
        # ゲームが終了したかどうかを返す
        return self.done

    def action(self, action):
        # 指定されたアクションを実行する
        # ランダムに相手の手を決める
        opponent_action = self.actions[random.randint(0, 2)]
        # 現在の状態を更新する
        self.state = self.state_names.index(opponent_action)
        # 報酬を取得する
        reward = self.rewards[self.state][self.actions.index(action)]
        # ゲームの終了状態を更新する
        self.done = reward != 0
        # 報酬とゲームの終了状態を返す
        return reward, self.done

class JankenAgent:
    def __init__(self, env):
        # 環境を保持する
        self.env = env
        # Q テーブルを初期化する
        self.q_table = [[0 for _ in range(len(env.actions))] for _ in range(len(env.state_names))]
        # 学習率を設定する
        self.learning_rate = 0.1
        # 減衰率を設定する
        self.discount_rate = 0.9
        # ε-greedy 法の ε 値を設定する
        self.epsilon = 0.1

    def get_action(self, state):
        # ε-greedy 法に基づいて、行動を決定する
        if random.random() < self.epsilon:
            # ランダムに行動を選択する
            action = self.env.actions[random.randint(0, 2)]
        else:
            # Q テーブルから最大の Q 値を持つ行動を選択する
            action = self.env.actions[self.q_table[state].index(max(self.q_table[state]))]
        return action

    def update_q_table(self, state, action, next_state, reward, done):
        # Q テーブルを更新する
        if not done:
            # 次の状態で得られる最大の Q 値を取得する
            max_q = max(self.q_table[next_state])
            # Q テーブルを更新する
            self.q_table[state][self.env.actions.index(action)] = (1 - self.learning_rate) * self.q_table[state][self.env.actions.index(action)] + self.learning_rate * (reward + self.discount_rate * max_q)
        else:
            # ゲームが終了した場合は、Q テーブルを直接更新する
            self.q_table[state][self.env.actions.index(action)] = reward

# 環境を初期化する
env = JankenEnv()
# エージェントを初期化する
agent = JankenAgent(env)

# 学習を開始する
for episode in range(10000):
    # ゲームを初期化する
    state = env.state_names.index("グー")
    done = False
    while not done:
        # エージェントが行動を選択する
        action = agent.get_action(state)
        # 行動を実行する
        reward, done = env.action(action)
        # 次の状態を取得する
        next_state = env.get_state()
        # Q テーブルを更新する
        agent.update_q_table(state, action, next_state, reward, done)
        # 状態を更新する
        state = next_state

# Q テーブルを表示する
print(agent.q_table)