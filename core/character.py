import uuid
import random

class Stats:
    """
    캐릭터의 능력치를 관리하는 클래스.
    버프/디버프를 위해 기본 스탯과 현재 스탯을 분리합니다.
    """
    def __init__(self, base_stats):
        self.base = base_stats  # 기본 스탯 (딕셔너리)
        self.current = base_stats.copy()  # 현재 스탯 (버프/디버프 적용)

class Emotion:
    """
    캐릭터의 감정을 수치화하는 클래스.
    """
    def __init__(self, initial_values=None):
        if initial_values is None:
            initial_values = {
                'joy': 50,
                'sadness': 0,
                'anger': 0,
                'fear': 0,
                'love': 0,
                'guilt': 0,
                'jealousy': 0,
                'nostalgia': 0,
                'relief': 0,
            }
        self.values = initial_values

class Personality:
    """
    캐릭터의 성격 타입을 정의하고, 초기 감정값에 영향을 줍니다.
    """
    def __init__(self, type, moral_alignment):
        self.type = type
        self.moral_alignment = moral_alignment

class Character:
    """
    게임의 모든 캐릭터를 대표하는 메인 클래스.
    """
    def __init__(self, name, profession, grade, personality_type, moral_alignment):
        # 1. 기본 정보
        self.name = name
        self.profession = profession
        self.id = str(uuid.uuid4())  # 고유하고 안정적인 UUID 사용
        self.grade = grade
        self.level = 1
        self.exp = 0

        # 2. 핵심 데이터 인스턴스 (등급, 직업, 성격에 따라 초기화)
        initial_base_stats = self.get_initial_stats(profession, grade)
        self.stats = Stats(initial_base_stats)

        initial_emotions = self.get_initial_emotions(personality_type)
        self.emotions = Emotion(initial_emotions)
        
        self.personality = Personality(personality_type, moral_alignment)

        # 3. 현재 상태
        self.current_status = 'Healthy'
        self.current_role = 'Trainee'
        self.relationships = {}  # {'캐릭터ID': {'affinity': 80, 'trust': 50}} 형태

        # 4. 스킬 (추후 Skill 클래스로 구현)
        self.skills = []

    def get_initial_stats(self, profession, grade):
        """직업과 등급에 따른 초기 스탯을 반환합니다."""
        base_stats = {
            'strength': 10, 'agility': 10, 'vitality': 10,
            'intelligence': 10, 'willpower': 10, 'charisma': 10
        }
        
        # 직업 및 등급에 따른 스탯 보정 로직 (예시)
        if profession == '과학자':
            base_stats['intelligence'] += 5
        if grade == 2:
            base_stats['strength'] += 3
        # ... 기타 직업/등급 보정 로직 추가 ...

        return base_stats

    def get_initial_emotions(self, personality_type):
        """성격 타입에 따른 초기 감정값을 반환합니다."""
        initial_emotions = {
            'joy': 50, 'sadness': 0, 'anger': 0, 'fear': 0,
            'love': 0, 'guilt': 0, 'jealousy': 0,
            'nostalgia': 0, 'relief': 0,
        }
        
        # 성격에 따른 초기 감정 보정 로직 (예시)
        if personality_type == '낙천적':
            initial_emotions['joy'] = 80
            initial_emotions['sadness'] = 10
        elif personality_type == '비관적':
            initial_emotions['joy'] = 20
            initial_emotions['sadness'] = 60
        
        return initial_emotions

    def apply_buff(self, stat_name, amount):
        """특정 스탯에 버프를 적용합니다."""
        if stat_name in self.stats.current:
            self.stats.current[stat_name] += amount
            print(f"{self.name}의 {stat_name} 스탯이 {amount}만큼 증가했습니다.")

    def reset_stats_to_base(self):
        """모든 스탯을 기본값으로 되돌립니다."""
        self.stats.current = self.stats.base.copy()
        print(f"{self.name}의 모든 스탯이 기본값으로 초기화되었습니다.")