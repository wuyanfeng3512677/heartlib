"""
HeartMuLa 歌词创作顶级专家模块
包含：AI分析器、流派识别、智能推荐、结构优化等高级功能
"""

from enum import Enum
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import random


class Genre(Enum):
    """歌词流派"""
    POP = "pop"                    # 流行
    ROCK = "rock"                  # 摇滚
    BALLAD = "ballad"              # 民谣/抒情
    HIPHOP = "hiphop"              # 嘻哈
    RNB = "rnb"                    # R&B
    CHINESE_CLASSICAL = "chinese_classical"  # 中国风/古风
    ROCK_N_ROLL = "rock_n_roll"    # 摇滚乐
    ELECTRONIC = "electronic"      # 电子


class AnalysisMetric(Enum):
    """分析指标"""
    STRUCTURE = "structure"        # 结构完整性
    RHYME = "rhyme"               # 押韵质量
    IMAGERY = "imagery"            # 意象密度
    EMOTION = "emotion"            # 情感表达
    MEMORABILITY = "memorability"  # 记忆度
    FLOW = "flow"                  # 流畅度


@dataclass
class LyricAnalysis:
    """歌词分析结果"""
    structure_score: float
    rhyme_score: float
    imagery_score: float
    emotion_score: float
    memorability_score: float
    flow_score: float
    overall_score: float
    suggestions: List[str]
    strengths: List[str]


class EmotionWordLibrary:
    """情感词汇库"""
    
    # 积极情感词汇
    POSITIVE = {
        "joy": ["开心", "快乐", "幸福", "温暖", "甜蜜", "美好", "灿烂", "明亮", "欢快", "愉悦"],
        "love": ["爱", "喜欢", "心动", "思念", "依恋", "眷恋", "深情", "浓烈", "炽热", "缠绵"],
        "hope": ["希望", "梦想", "期待", "憧憬", "向往", "追求", "光明", "未来", "前行", "奋斗"],
        "gratitude": ["感谢", "感恩", "珍惜", "铭记", "珍藏", "难忘", "感动", "温暖", "幸福"],
        "courage": ["勇敢", "坚强", "坚定", "不屈", "拼搏", "奋斗", "冲刺", "突破", "力量", "热血"]
    }
    
    # 消极情感词汇
    NEGATIVE = {
        "sadness": ["悲伤", "难过", "痛苦", "伤心", "失落", "沮丧", "绝望", "崩溃", "心碎", "泪"],
        "loneliness": ["孤独", "寂寞", "孤单", "独自", "一个人", "空荡", "冷清", "沉默", "寂静"],
        "regret": ["后悔", "遗憾", "可惜", "错过", "失去", "离别", "分手", "告别", "遗憾", "无奈"],
        "fear": ["害怕", "恐惧", "担忧", "不安", "焦虑", "紧张", "迷茫", "困惑", "彷徨"],
        "anger": ["愤怒", "生气", "不满", "怨恨", "讨厌", "失望", "抱怨", "委屈", "心寒"]
    }
    
    # 中性情感词汇
    NEUTRAL = {
        "memory": ["回忆", "往事", "过去", "曾经", "从前", "那年", "那天", "那年夏", "时光"],
        "time": ["时间", "岁月", "光阴", "流年", "时光", "时光流逝", "年年岁岁"],
        "life": ["人生", "生活", "世界", "命运", "生活", "人间", "世间", "众生"],
        "nature": ["天空", "大地", "海洋", "山川", "河流", "森林", "星空", "月光", "阳光"]
    }


class GenreIdentifier:
    """歌词流派识别器"""
    
    # 各流派的特征词汇
    GENRE_FEATURES = {
        Genre.POP: {
            "keywords": ["爱", "心", "梦", "情", "想", "你", "我", "我们", "永远", "幸福", "快乐"],
            "structures": ["verse_chorus"],
            "typical_length": 7,
            "rhyme_frequency": "high"
        },
        Genre.ROCK: {
            "keywords": ["呐喊", "自由", "热血", "摇滚", "叛逆", "不羁", "疯狂", "燃烧", "释放", "冲破"],
            "structures": ["verse_chorus"],
            "typical_length": 8,
            "rhyme_frequency": "medium"
        },
        Genre.BALLAD: {
            "keywords": ["风", "雨", "夜", "月", "星", "光", "梦", "回忆", "时光", "从前", "思念"],
            "structures": ["ababcb"],
            "typical_length": 7,
            "rhyme_frequency": "high"
        },
        Genre.HIPHOP: {
            "keywords": ["说唱", "节奏", "态度", "真实", "街头", "奋斗", "麦克风", "打破", "创造", "我"],
            "structures": ["verse_chorus"],
            "typical_length": 10,
            "rhyme_frequency": "low"
        },
        Genre.RNB: {
            "keywords": ["爱", "夜", "心", "感觉", "氛围", "温柔", "浪漫", "甜蜜", "亲吻", "拥抱"],
            "structures": ["verse_chorus"],
            "typical_length": 8,
            "rhyme_frequency": "medium"
        },
        Genre.CHINESE_CLASSICAL: {
            "keywords": ["月", "风", "烟雨", "江南", "古道", "西风", "瘦马", "山水", "杨柳", "清", "淡"],
            "structures": ["ababcb"],
            "typical_length": 7,
            "rhyme_frequency": "very_high"
        }
    }
    
    @classmethod
    def identify(cls, lyrics: List[str]) -> Dict[Genre, float]:
        """识别歌词流派"""
        scores = {genre: 0.0 for genre in Genre}
        
        for line in lyrics:
            for genre, features in cls.GENRE_FEATURES.items():
                keyword_count = sum(1 for keyword in features["keywords"] if keyword in line)
                scores[genre] += keyword_count
        
        # 归一化
        total = sum(scores.values())
        if total > 0:
            scores = {genre: score/total for genre, score in scores.items()}
        
        return scores
    
    @classmethod
    def get_top_genre(cls, lyrics: List[str]) -> Tuple[Genre, float]:
        """获取最可能的流派"""
        scores = cls.identify(lyrics)
        top_genre = max(scores, key=scores.get)
        return top_genre, scores[top_genre]


class RhymeRecommender:
    """智能韵脚推荐器"""
    
    def __init__(self):
        self.emotion_library = EmotionWordLibrary()
        self.rhyme_db = {
            "a": ["她", "花", "家", "吧", "呀", "啦", "下", "大", "发"],
            "ai": ["来", "爱", "在", "白", "开", "海", "彩", "猜", "才", "怀"],
            "an": ["看", "站", "天", "晚", "难", "暖", "完", "满", "散", "转"],
            "ang": ["想", "光", "望", "样", "唱", "长", "方", "上", "亮", "香"],
            "i": ["你", "里", "起", "去", "记", "气", "地", "事", "意", "世"],
            "ian": ["边", "眼", "年", "天", "前", "间", "点", "片", "面", "线"],
            "in": ["心", "今", "金", "近", "进", "尽", "紧", "劲", "禁", "锦"],
            "ing": ["听", "情", "行", "明", "星", "命", "定", "影", "醒", "应"],
            "ou": ["走", "手", "头", "有", "友", "后", "候", "久", "就", "旧"]
        }
    
    def get_rhyme_group(self, char: str) -> Optional[str]:
        """获取字符的韵脚组"""
        for group, chars in self.rhyme_db.items():
            if char in chars:
                return group
        return None
    
    def recommend_rhyme_words(self, last_word: str, count: int = 5) -> List[str]:
        """根据上一个词推荐韵脚词"""
        rhyme_group = self.get_rhyme_group(last_word)
        if rhyme_group and rhyme_group in self.rhyme_db:
            return random.sample(self.rhyme_db[rhyme_group], min(count, len(self.rhyme_db[rhyme_group])))
        return []
    
    def recommend_by_emotion(self, emotion: str, count: int = 5) -> List[str]:
        """根据情绪推荐韵脚词"""
        emotion_rhyme_map = {
            "happy": ["ang", "ai", "iao"],
            "sad": ["i", "in", "ing"],
            "love": ["ai", "iang"],
            "courage": ["ang", "eng"]
        }
        
        rhyme_groups = emotion_rhyme_map.get(emotion, ["a", "ai"])
        words = []
        for group in rhyme_groups:
            if group in self.rhyme_db:
                words.extend(self.rhyme_db[group])
        
        return random.sample(words, min(count, len(words)))


class LyricStructureOptimizer:
    """歌词结构优化器"""
    
    # 各部分建议长度
    SECTION_LENGTHS = {
        "Verse": (4, 8),
        "Pre-Chorus": (2, 4),
        "Chorus": (4, 8),
        "Bridge": (2, 4),
        "Intro": (1, 2),
        "Outro": (1, 2)
    }
    
    @classmethod
    def optimize_section_lengths(cls, song_structure: Dict[str, List[str]]) -> Dict[str, Dict]:
        """优化各部分长度"""
        suggestions = {}
        
        for section, lines in song_structure.items():
            min_len, max_len = cls.SECTION_LENGTHS.get(section, (4, 8))
            actual_len = len(lines)
            
            if actual_len < min_len:
                suggestions[section] = {
                    "status": "too_short",
                    "current": actual_len,
                    "recommended": f"{min_len}-{max_len}",
                    "suggestion": f"建议增加{min_len - actual_len}到{min_len}行"
                }
            elif actual_len > max_len:
                suggestions[section] = {
                    "status": "too_long",
                    "current": actual_len,
                    "recommended": f"{min_len}-{max_len}",
                    "suggestion": f"建议精简{actual_len - max_len}行"
                }
            else:
                suggestions[section] = {
                    "status": "good",
                    "current": actual_len,
                    "recommended": f"{min_len}-{max_len}",
                    "suggestion": "长度合适"
                }
        
        return suggestions
    
    @classmethod
    def suggest_structure(cls, song_type: str) -> List[str]:
        """建议歌曲结构"""
        structures = {
            "simple": ["Verse", "Chorus", "Verse", "Chorus"],
            "standard": ["Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus"],
            "full": ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Bridge", "Chorus", "Outro"]
        }
        
        if song_type == "simple":
            return structures["simple"]
        elif song_type == "standard":
            return structures["standard"]
        else:
            return structures["full"]


class RhymePatternGenerator:
    """押韵模式生成器"""
    
    PATTERNS = {
        "AABB": "两句一换韵，适合叙事",
        "ABAB": "隔句押韵，最常见",
        "ABBA": "包孕式押韵，变化丰富",
        "ABCB": "一三句不押，二四句押",
        "AAAA": "通篇一韵，节奏感强",
        "FREE": "自由押韵，随心所欲"
    }
    
    @classmethod
    def generate_pattern(cls, pattern_name: str, lines: List[str]) -> List[Tuple[int, str]]:
        """生成押韵模式"""
        if pattern_name not in cls.PATTERNS:
            return [(i, "free") for i in range(len(lines))]
        
        pattern_map = {
            "AABB": cls._aabb_pattern,
            "ABAB": cls._abab_pattern,
            "ABBA": cls._abba_pattern,
            "ABCB": cls._abcb_pattern,
            "FREE": cls._free_pattern
        }
        
        return pattern_map[pattern_name](lines)
    
    @classmethod
    def _aabb_pattern(cls, lines: List[str]):
        """AABB模式"""
        result = []
        for i in range(0, len(lines), 2):
            rhyme_group = f"A{i//2}"
            if i < len(lines):
                result.append((i, rhyme_group))
            if i+1 < len(lines):
                result.append((i+1, f"B{i//2}"))
        return result
    
    @classmethod
    def _abab_pattern(cls, lines: List[str]):
        """ABAB模式"""
        result = []
        current_rhyme = "A"
        for i in range(len(lines)):
            if i % 2 == 0:
                result.append((i, current_rhyme))
            else:
                result.append((i, current_rhyme.replace("A", "B")))
                current_rhyme = "A" if current_rhyme != "A" else "B"
        return result
    
    @classmethod
    def _abba_pattern(cls, lines: List[str]):
        """ABBA模式"""
        result = []
        rhyme_groups = ["A", "B", "B", "A"]
        for i, rhyme in enumerate(rhyme_groups):
            if i < len(lines):
                result.append((i, rhyme))
        return result
    
    @classmethod
    def _abcb_pattern(cls, lines: List[str]):
        """ABCB模式"""
        result = []
        rhyme_counter = 0
        for i in range(len(lines)):
            if i % 2 == 0:
                result.append((i, "A"))
            else:
                result.append((i, f"B{rhyme_counter}"))
                rhyme_counter += 1
        return result
    
    @classmethod
    def _free_pattern(cls, lines: List[str]):
        """FREE模式"""
        return [(i, f"free_{i}") for i in range(len(lines))]


class AI LyricAnalyzer:
    """AI歌词分析器"""
    
    def __init__(self):
        self.emotion_library = EmotionWordLibrary()
        self.genre_identifier = GenreIdentifier()
        self.rhyme_recommender = RhymeRecommender()
    
    def analyze_line(self, line: str) -> Dict:
        """分析单行歌词"""
        # 统计字数
        char_count = len(line)
        
        # 检测情感词汇
        emotions = []
        all_words = {**self.emotion_library.POSITIVE, 
                     **self.emotion_library.NEGATIVE, 
                     **self.emotion_library.NEUTRAL}
        
        for category, words in all_words.items():
            for word in words:
                if word in line:
                    emotions.append({"word": word, "category": category})
        
        # 检测意象词
        imagery_words = ["月", "星", "光", "风", "雨", "雪", "花", "叶", "海", "山", "路", "街", "灯"]
        imagery = [w for w in imagery_words if w in line]
        
        # 检测韵脚
        if line:
            last_char = line[-1]
            rhyme_group = self.rhyme_recommender.get_rhyme_group(last_char)
        else:
            rhyme_group = None
        
        return {
            "line": line,
            "char_count": char_count,
            "emotions": emotions,
            "imagery": imagery,
            "rhyme_group": rhyme_group,
            "suggestions": self._generate_line_suggestions(line, char_count, emotions, imagery)
        }
    
    def _generate_line_suggestions(self, line: str, char_count: int, emotions: List, imagery: List) -> List[str]:
        """生成单行建议"""
        suggestions = []
        
        if char_count > 12:
            suggestions.append("句子较长，可考虑精简")
        elif char_count < 5:
            suggestions.append("句子较短，可适当扩展")
        
        if not imagery:
            suggestions.append("可增加意象词增强画面感")
        
        if not emotions:
            suggestions.append("可加入情感词汇增强感染力")
        
        return suggestions if suggestions else ["表达良好"]
    
    def analyze_song(self, song: Dict[str, List[str]]) -> LyricAnalysis:
        """分析整首歌"""
        all_lines = []
        for lines in song.values():
            all_lines.extend(lines)
        
        # 分析各指标
        structure_score = self._evaluate_structure(song)
        rhyme_score = self._evaluate_rhyme(all_lines)
        imagery_score = self._evaluate_imagery(all_lines)
        emotion_score = self._evaluate_emotion(all_lines)
        memorability_score = self._evaluate_memorability(all_lines)
        flow_score = self._evaluate_flow(all_lines)
        
        # 综合评分
        overall = (structure_score * 0.2 + rhyme_score * 0.25 + 
                  imagery_score * 0.15 + emotion_score * 0.2 + 
                  memorability_score * 0.1 + flow_score * 0.1)
        
        return LyricAnalysis(
            structure_score=structure_score,
            rhyme_score=rhyme_score,
            imagery_score=imagery_score,
            emotion_score=emotion_score,
            memorability_score=memorability_score,
            flow_score=flow_score,
            overall_score=overall,
            suggestions=self._generate_suggestions(structure_score, rhyme_score, imagery_score, 
                                                  emotion_score, memorability_score, flow_score),
            strengths=self._identify_strengths(structure_score, rhyme_score, imagery_score, 
                                             emotion_score, memorability_score, flow_score)
        )
    
    def _evaluate_structure(self, song: Dict[str, List[str]]) -> float:
        """评估结构"""
        expected_sections = {"Verse", "Chorus"}
        actual_sections = set(song.keys())
        
        # 检查是否有主歌和副歌
        if expected_sections.issubset(actual_sections):
            return 0.9
        elif len(actual_sections) >= 2:
            return 0.7
        else:
            return 0.5
    
    def _evaluate_rhyme(self, lines: List[str]) -> float:
        """评估押韵"""
        rhyme_groups = []
        for line in lines:
            if line:
                last_char = line[-1]
                rhyme = self.rhyme_recommender.get_rhyme_group(last_char)
                if rhyme:
                    rhyme_groups.append(rhyme)
        
        # 计算重复率
        if len(rhyme_groups) < 2:
            return 0.3
        
        unique = len(set(rhyme_groups))
        total = len(rhyme_groups)
        repeat_rate = 1 - (unique / total)
        
        return min(1.0, repeat_rate * 1.5)
    
    def _evaluate_imagery(self, lines: List[str]) -> float:
        """评估意象"""
        imagery_words = ["月", "星", "光", "风", "雨", "雪", "花", "叶", "海", "山", "路", "街", "灯"]
        total_imagery = 0
        
        for line in lines:
            for word in imagery_words:
                if word in line:
                    total_imagery += 1
        
        # 理想密度：每2-3行一个意象词
        ideal_density = len(lines) / 2.5
        actual_density = total_imagery
        
        return min(1.0, actual_density / ideal_density)
    
    def _evaluate_emotion(self, lines: List[str]) -> float:
        """评估情感"""
        all_words = {**self.emotion_library.POSITIVE, **self.emotion_library.NEGATIVE}
        emotion_count = 0
        
        for line in lines:
            for category, words in all_words.items():
                for word in words:
                    if word in line:
                        emotion_count += 1
        
        # 理想：每行0.5-1个情感词
        ideal = len(lines) * 0.75
        return min(1.0, emotion_count / ideal)
    
    def _evaluate_memorability(self, lines: List[str]) -> float:
        """评估记忆度"""
        # 检查重复词
        word_freq = {}
        for line in lines:
            for char in line:
                word_freq[char] = word_freq.get(char, 0) + 1
        
        # 计算信息熵
        total = sum(word_freq.values())
        entropy = 0
        for freq in word_freq.values():
            p = freq / total
            if p > 0:
                entropy -= p * (p ** 0.5)
        
        # 适度的重复有助于记忆
        return min(1.0, entropy * 2)
    
    def _evaluate_flow(self, lines: List[str]) -> float:
        """评估流畅度"""
        lengths = [len(line) for line in lines]
        if not lengths:
            return 0.5
        
        # 计算长度方差
        avg = sum(lengths) / len(lengths)
        variance = sum((l - avg) ** 2 for l in lengths) / len(lengths)
        
        # 适度的变化是好的
        ideal_variance = 4
        return max(0, 1 - abs(variance - ideal_variance) / ideal_variance)
    
    def _generate_suggestions(self, structure, rhyme, imagery, emotion, memorability, flow) -> List[str]:
        """生成改进建议"""
        suggestions = []
        
        if structure < 0.7:
            suggestions.append("💡 结构可以更完整，建议添加主歌和副歌")
        if rhyme < 0.6:
            suggestions.append("💡 押韵可以更规律，使用ABAB或AABB模式")
        if imagery < 0.6:
            suggestions.append("💡 增加意象词，如月亮、星光、风雨等")
        if emotion < 0.6:
            suggestions.append("💡 加强情感表达，使用更多情感词汇")
        if memorability < 0.5:
            suggestions.append("💡 适当重复关键词，增强记忆点")
        if flow < 0.6:
            suggestions.append("💡 调整句子长短，增强节奏感")
        
        return suggestions if suggestions else ["✨ 歌词质量优秀！"]
    
    def _identify_strengths(self, structure, rhyme, imagery, emotion, memorability, flow) -> List[str]:
        """识别优势"""
        strengths = []
        
        if structure >= 0.8:
            strengths.append("✅ 结构完整清晰")
        if rhyme >= 0.8:
            strengths.append("✅ 押韵优美流畅")
        if imagery >= 0.8:
            strengths.append("✅ 意象丰富生动")
        if emotion >= 0.8:
            strengths.append("✅ 情感表达真挚")
        if memorability >= 0.7:
            strengths.append("✅ 朗朗上口易记")
        if flow >= 0.7:
            strengths.append("✅ 节奏感强")
        
        return strengths if strengths else ["🎵 具有创作潜力"]


class ExpertLyricAssistant:
    """顶级歌词创作专家"""
    
    def __init__(self):
        self.analyzer = AI LyricAnalyzer()
        self.genre_identifier = GenreIdentifier()
        self.rhyme_recommender = RhymeRecommender()
        self.structure_optimizer = LyricStructureOptimizer()
        self.rhyme_pattern_generator = RhymePatternGenerator()
    
    def analyze(self, song: Dict[str, List[str]]) -> LyricAnalysis:
        """分析歌词"""
        return self.analyzer.analyze_song(song)
    
    def identify_genre(self, lyrics: List[str]) -> Dict[Genre, float]:
        """识别流派"""
        return self.genre_identifier.identify(lyrics)
    
    def recommend_rhyme(self, last_word: str, emotion: str = "") -> List[str]:
        """推荐韵脚"""
        if emotion:
            return self.rhyme_recommender.recommend_by_emotion(emotion)
        return self.rhyme_recommender.recommend_rhyme_words(last_word)
    
    def optimize_structure(self, song: Dict[str, List[str]]) -> Dict[str, Dict]:
        """优化结构"""
        return self.structure_optimizer.optimize_section_lengths(song)
    
    def generate_rhyme_pattern(self, pattern_name: str, lines: List[str]) -> List[Tuple[int, str]]:
        """生成押韵模式"""
        return self.rhyme_pattern_generator.generate_pattern(pattern_name, lines)
    
    def get_rhyme_patterns(self) -> Dict[str, str]:
        """获取所有押韵模式"""
        return RhymePatternGenerator.PATTERNS


# 演示函数
def demo_expert_features():
    """演示顶级专家功能"""
    print("=" * 80)
    print("HeartMuLa 歌词创作顶级专家功能演示")
    print("=" * 80)
    
    assistant = ExpertLyricAssistant()
    
    # 示例歌词
    sample_song = {
        "Verse 1": [
            "窗外的月光洒在街道上",
            "我独自走在这熟悉的地方",
            "想起曾经的点点滴滴",
            "那些美好的时光"
        ],
        "Chorus": [
            "你是我心中的那束光",
            "照亮我前行的方向",
            "不管未来有多迷茫",
            "我都会永远爱你"
        ]
    }
    
    # 1. 分析歌词
    print("\n📊 AI歌词分析")
    print("-" * 50)
    analysis = assistant.analyze(sample_song)
    print(f"综合评分: {analysis.overall_score:.2f}/1.00")
    print(f"\n各项评分:")
    print(f"  结构完整性: {analysis.structure_score:.2f}")
    print(f"  押韵质量: {analysis.rhyme_score:.2f}")
    print(f"  意象密度: {analysis.imagery_score:.2f}")
    print(f"  情感表达: {analysis.emotion_score:.2f}")
    print(f"  记忆度: {analysis.memorability_score:.2f}")
    print(f"  流畅度: {analysis.flow_score:.2f}")
    
    print("\n💪 优势:")
    for strength in analysis.strengths:
        print(f"  {strength}")
    
    print("\n💡 改进建议:")
    for suggestion in analysis.suggestions:
        print(f"  {suggestion}")
    
    # 2. 流派识别
    print("\n\n🎸 流派识别")
    print("-" * 50)
    all_lines = []
    for lines in sample_song.values():
        all_lines.extend(lines)
    
    genre_scores = assistant.identify_genre(all_lines)
    print("流派匹配度:")
    for genre, score in sorted(genre_scores.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"  {genre.value}: {score:.2f}")
    
    # 3. 韵脚推荐
    print("\n\n🎵 智能韵脚推荐")
    print("-" * 50)
    print("根据'光'推荐韵脚词:")
    rhyme_words = assistant.recommend_rhyme("光")
    print(f"  {', '.join(rhyme_words)}")
    
    print("\n根据'悲伤'情绪推荐韵脚:")
    emotion_words = assistant.recommend_rhyme("", "sad")
    print(f"  {', '.join(emotion_words[:8])}")
    
    # 4. 结构优化
    print("\n\n📐 结构优化建议")
    print("-" * 50)
    suggestions = assistant.optimize_structure(sample_song)
    for section, info in suggestions.items():
        print(f"\n{section}:")
        print(f"  当前: {info['current']}行")
        print(f"  推荐: {info['recommended']}行")
        print(f"  状态: {info['status']}")
        print(f"  建议: {info['suggestion']}")
    
    # 5. 押韵模式
    print("\n\n🎼 押韵模式")
    print("-" * 50)
    patterns = assistant.get_rhyme_patterns()
    print("可用押韵模式:")
    for pattern, desc in patterns.items():
        print(f"  {pattern}: {desc}")
    
    print("\n示例 - ABAB模式:")
    lines = ["第一句", "第二句", "第三句", "第四句"]
    pattern = assistant.generate_rhyme_pattern("ABAB", lines)
    for line_num, rhyme_group in pattern:
        print(f"  第{line_num+1}句: {rhyme_group}韵")
    
    print("\n" + "=" * 80)
    print("顶级专家功能演示完成！")
    print("=" * 80)


if __name__ == "__main__":
    demo_expert_features()
