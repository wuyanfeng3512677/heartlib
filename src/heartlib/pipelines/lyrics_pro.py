"""
HeartMuLa 歌词创作专业进阶模块
包含：情感曲线设计、智能韵脚管理、质量评估、灵感生成等高级功能
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, Callable
from enum import Enum
import random


class EmotionLevel(Enum):
    """情感强度等级"""
    VERY_LOW = 1  # 非常低 - 平静
    LOW = 2       # 低 - 放松
    MEDIUM = 3    # 中等 - 平常
    HIGH = 4      # 高 - 激动
    VERY_HIGH = 5 # 非常高 - 爆发


class NarrativePerspective(Enum):
    """叙事视角"""
    FIRST_PERSON = "first_person"      # 第一人称 "我"
    SECOND_PERSON = "second_person"    # 第二人称 "你"
    THIRD_PERSON = "third_person"      # 第三人称 "他/她"
    OMNISCIENT = "omniscient"          # 全知视角
    DIALOGUE = "dialogue"              # 对话式


class HookType(Enum):
    """Hook记忆点类型"""
    EMOTIONAL = "emotional"            # 情感hook - 触动人心
    REPETITIVE = "repetitive"          # 重复hook - 洗脑循环
    UNIQUE = "unique"                  # 独特hook - 独特视角
    QUESTION = "question"              # 疑问hook - 引发思考


class RhymeComplexity(Enum):
    """押韵复杂度"""
    SIMPLE = "simple"      # 简单押韵 - 基础
    MEDIUM = "medium"     # 中等押韵 - 变化
    COMPLEX = "complex"   # 复杂押韵 - 多变


@dataclass
class EmotionCurve:
    """情感曲线配置"""
    intro_level: EmotionLevel = EmotionLevel.LOW
    verse1_level: EmotionLevel = EmotionLevel.LOW
    pre_chorus_level: EmotionLevel = EmotionLevel.MEDIUM
    chorus_level: EmotionLevel = EmotionLevel.HIGH
    verse2_level: EmotionLevel = EmotionLevel.MEDIUM
    bridge_level: EmotionLevel = EmotionLevel.VERY_HIGH
    final_chorus_level: EmotionLevel = EmotionLevel.VERY_HIGH
    
    def get_level_value(self, level: EmotionLevel) -> float:
        """将情感等级转换为具体数值"""
        value_map = {
            EmotionLevel.VERY_LOW: 0.2,
            EmotionLevel.LOW: 0.4,
            EmotionLevel.MEDIUM: 0.6,
            EmotionLevel.HIGH: 0.8,
            EmotionLevel.VERY_HIGH: 1.0
        }
        return value_map.get(level, 0.5)


class RhymeManager:
    """智能韵脚管理系统"""
    
    def __init__(self):
        # 韵脚数据库
        self.rhyme_database = {
            "a": ["她", "花", "家", "吧", "呀", "啦", "下", "大", "发", "沙", "茶", "麻", "拿", "啊", "妈", "爸"],
            "ai": ["来", "爱", "在", "白", "开", "海", "彩", "猜", "才", "怀", "买", "卖", "派", "代", "菜", "抬"],
            "an": ["看", "站", "天", "晚", "难", "暖", "完", "满", "散", "转", "班", "半", "办", "般", "山", "蓝"],
            "ang": ["想", "光", "望", "样", "唱", "长", "方", "上", "亮", "香", "忙", "放", "量", "场", "强", "房"],
            "ao": ["跳", "笑", "找", "好", "老", "跑", "叫", "要", "抱", "到", "草", "早", "高", "造", "道", "少"],
            "e": ["么", "得", "个", "热", "说", "可", "呢", "歌", "河", "客", "乐", "车", "色", "策", "特", "喝"],
            "ei": ["给", "美", "飞", "水", "谁", "泪", "累", "类", "雷", "贵", "北", "备", "背", "杯", "推", "随"],
            "en": ["真", "深", "人", "本", "很", "门", "分", "身", "心", "新", "文", "温", "问", "闻", "春", "云"],
            "eng": ["声", "能", "风", "梦", "生", "等", "城", "灯", "星", "情", "成", "程", "疼", "疼", "疼", "疼"],
            "i": ["你", "里", "起", "去", "记", "气", "地", "事", "意", "世", "离", "低", "底", "第", "米", "皮"],
            "ian": ["边", "眼", "年", "天", "前", "间", "点", "片", "面", "线", "电", "连", "脸", "变", "念", "钱"],
            "iao": ["跳", "笑", "叫", "要", "飘", "摇", "照", "妙", "巧", "调", "小", "表", "秒", "鸟", "掉", "掉"],
            "ie": ["写", "谢", "夜", "街", "别", "些", "界", "姐", "借", "鞋", "也", "野", "业", "页", "铁", "接"],
            "in": ["心", "今", "金", "近", "进", "尽", "紧", "劲", "禁", "锦", "音", "阴", "银", "因", "林", "新"],
            "ing": ["听", "情", "行", "明", "星", "命", "定", "影", "醒", "应", "轻", "清", "青", "经", "停", "疼"],
            "ou": ["走", "手", "头", "有", "友", "后", "候", "久", "就", "旧", "楼", "留", "流", "柳", "口", "豆"],
            "u": ["路", "住", "书", "出", "处", "苦", "服", "物", "助", "注", "不", "步", "部", "布", "图", "土"],
            "ua": ["花", "画", "话", "华", "化", "发", "打", "拿", "下", "怕", "瓜", "挂", "夸", "跨", "抓", "跨"],
            "uo": ["说", "多", "过", "火", "活", "落", "错", "作", "所", "破", "国", "果", "过", "或", "坐", "左"]
        }
        
        # 情绪对应的韵脚
        self.emotion_rhyme_map = {
            "happy": ["ang", "ai", "ao", "iao"],
            "sad": ["i", "in", "ing", "en"],
            "love": ["ai", "iang", "iang"],
            "courage": ["ang", "eng", "ong"],
            "nostalgia": ["i", "an", "en"]
        }
    
    def get_rhyme_for_emotion(self, emotion: str) -> str:
        """根据情绪选择合适的韵脚"""
        candidates = self.emotion_rhyme_map.get(emotion, ["a", "ai", "an"])
        return random.choice(candidates)
    
    def get_rhyme_words(self, rhyme_type: str, count: int = 5) -> List[str]:
        """获取指定韵脚的一组词"""
        words = self.rhyme_database.get(rhyme_type, [])
        if len(words) >= count:
            return random.sample(words, count)
        return words
    
    def match_rhyme(self, word: str) -> Optional[str]:
        """匹配字的韵脚"""
        for rhyme, words in self.rhyme_database.items():
            if word in words:
                return rhyme
        return None


class LyricQualityEvaluator:
    """歌词质量评估系统"""
    
    @staticmethod
    def evaluate_rhyme_quality(lyrics: List[str]) -> Dict[str, float]:
        """评估押韵质量"""
        rhyme_manager = RhymeManager()
        rhyme_scores = []
        
        for i in range(len(lyrics) - 1):
            current_end = lyrics[i][-1] if lyrics[i] else ""
            next_end = lyrics[i+1][-1] if lyrics[i+1] else ""
            
            current_rhyme = rhyme_manager.match_rhyme(current_end)
            next_rhyme = rhyme_manager.match_rhyme(next_end)
            
            if current_rhyme and current_rhyme == next_rhyme:
                rhyme_scores.append(1.0)
            elif current_rhyme or next_rhyme:
                rhyme_scores.append(0.5)
            else:
                rhyme_scores.append(0.0)
        
        avg_score = sum(rhyme_scores) / len(rhyme_scores) if rhyme_scores else 0
        return {
            "score": avg_score,
            "detail": "优秀" if avg_score > 0.8 else "良好" if avg_score > 0.5 else "一般"
        }
    
    @staticmethod
    def evaluate_imagery_density(lyrics: List[str]) -> Dict[str, float]:
        """评估意象密度"""
        imagery_words = [
            "月", "星", "光", "风", "雨", "雪", "花", "叶", "海", "山", "路", "街", "灯",
            "夜", "梦", "心", "眼", "手", "影", "声", "色", "香", "味", "温度"
        ]
        
        total_imagery = 0
        for line in lyrics:
            for word in imagery_words:
                if word in line:
                    total_imagery += 1
        
        density = total_imagery / len(lyrics) if lyrics else 0
        return {
            "score": density,
            "detail": "丰富" if density > 1.5 else "适中" if density > 0.8 else "较少"
        }
    
    @staticmethod
    def evaluate_line_length_variance(lyrics: List[str]) -> Dict[str, float]:
        """评估行长度变化"""
        lengths = [len(line) for line in lyrics]
        if not lengths:
            return {"score": 0, "detail": "无数据"}
        
        avg_length = sum(lengths) / len(lengths)
        variance = sum((l - avg_length) ** 2 for l in lengths) / len(lengths)
        
        # 适度的变化是好的，过大或过小都不好
        ideal_variance = 4
        score = 1.0 - abs(variance - ideal_variance) / ideal_variance
        score = max(0, min(1, score))
        
        return {
            "score": score,
            "detail": "节奏感强" if variance > ideal_variance else "节奏平稳"
        }
    
    @staticmethod
    def evaluate_song(lyrics: Dict[str, List[str]]) -> Dict[str, any]:
        """综合评估整首歌"""
        all_lines = []
        for section_lines in lyrics.values():
            all_lines.extend(section_lines)
        
        rhyme_eval = LyricQualityEvaluator.evaluate_rhyme_quality(all_lines)
        imagery_eval = LyricQualityEvaluator.evaluate_imagery_density(all_lines)
        length_eval = LyricQualityEvaluator.evaluate_line_length_variance(all_lines)
        
        # 综合评分
        overall_score = (
            rhyme_eval["score"] * 0.4 +
            imagery_eval["score"] * 0.3 +
            length_eval["score"] * 0.3
        )
        
        return {
            "overall_score": overall_score,
            "rhyme": rhyme_eval,
            "imagery": imagery_eval,
            "rhythm": length_eval,
            "suggestions": LyricQualityEvaluator._generate_suggestions(
                rhyme_eval, imagery_eval, length_eval
            )
        }
    
    @staticmethod
    def _generate_suggestions(rhyme, imagery, rhythm) -> List[str]:
        """根据评估结果生成改进建议"""
        suggestions = []
        
        if rhyme["score"] < 0.6:
            suggestions.append("💡 建议：可以加强押韵的规律性")
        if imagery["score"] < 0.8:
            suggestions.append("💡 建议：可以增加更多意象和画面感")
        if rhythm["score"] < 0.5:
            suggestions.append("💡 建议：可以调整句子的长短变化")
        
        return suggestions if suggestions else ["✨ 歌词质量良好，继续保持！"]


class InspirationSparkGenerator:
    """灵感火花生成器 - 基于随机组合产生创意"""
    
    @staticmethod
    def generate_emotion_combination() -> Dict[str, str]:
        """生成情绪组合"""
        emotions = [
            "温暖的", "冰冷的", "甜蜜的", "苦涩的", "明亮的", "灰暗的",
            "期待的", "绝望的", "平静的", "激动的", "怀念的", "憧憬的"
        ]
        
        subjects = [
            "离别", "重逢", "思念", "遗忘", "成长", "失去",
            "等待", "错过", "开始", "结束", "拥有", "放手"
        ]
        
        modifiers = [
            "那一刻", "那天夜里", "那年夏天", "某个转角", "某个雨天", "某个瞬间"
        ]
        
        return {
            "emotion": random.choice(emotions),
            "subject": random.choice(subjects),
            "modifier": random.choice(modifiers)
        }
    
    @staticmethod
    def generate_scene_prompt() -> str:
        """生成场景提示"""
        scenes = [
            ("{time}的{place}", "窗边", "咖啡厅", "地铁站", "天台", "海边", "森林", "雨中"),
            ("{weather}的{place}", "下雨", "下雪", "起风", "晴天", "黄昏", "黎明"),
            ("{action}的{person}", "一个人走", "两个人坐", "三个人站", "独自等待", "相互依偎"),
            ("看见{object}想起{feeling}", "那张照片", "这把吉他", "这封信", "这杯咖啡", "这首歌"),
        ]
        
        template, *options = random.choice(scenes)
        
        if "{time}" in template:
            template = template.replace("{time}", random.choice(["凌晨三点", "深夜", "黄昏", "午后", "清晨"]))
        if "{place}" in template:
            template = template.replace("{place}", random.choice(options[:4]))
        if "{weather}" in template:
            template = template.replace("{weather}", random.choice(options[:6]))
        if "{person}" in template:
            template = template.replace("{person}", random.choice(options[6:]))
        if "{object}" in template:
            template = template.replace("{object}", random.choice(["那张照片", "这把吉他", "这封信", "这杯咖啡"]))
        if "{feeling}" in template:
            template = template.replace("{feeling}", random.choice(["你", "过去", "曾经", "我们"]))
        
        return template
    
    @staticmethod
    def generate_metaphor() -> str:
        """生成比喻句"""
        metaphors = [
            "你是我的{comparison}",
            "{subject}像{comparison}",
            "爱是{comparison}",
            "思念是{comparison}",
            "时间是{comparison}",
            "记忆是{comparison}"
        ]
        
        comparisons = [
            "一首歌", "一场梦", "一本书", "一杯酒", "一束光", "一阵风",
            "一场雨", "一朵花", "一片海", "一颗星", "一条路", "一封信",
            "一首诗", "一幅画", "一段旅程", "一个秘密"
        ]
        
        template = random.choice(metaphors)
        template = template.replace("{comparison}", random.choice(comparisons))
        template = template.replace("{subject}", random.choice(["你", "我", "他", "她", "它", "我们"]))
        
        return template
    
    @staticmethod
    def generate_hook_line(song_type: str = "love") -> str:
        """生成Hook记忆点"""
        if song_type == "love":
            hooks = [
                "你是我心中的那束光",
                "我想和你在一起",
                "遇见你是最美的意外",
                "我的世界因你而改变",
                "你就是我的答案"
            ]
        elif song_type == "sad":
            hooks = [
                "谢谢你来过",
                "我会好好的",
                "我们回不去了",
                "祝你幸福",
                "再见了我的爱"
            ]
        elif song_type == "dream":
            hooks = [
                "我要去追寻我的梦",
                "没有人能阻挡我",
                "这就是我的路",
                "我不放弃",
                "梦想在前方"
            ]
        else:
            hooks = [
                "这就是人生",
                "我们都在路上",
                "珍惜当下",
                "不忘初心",
                "继续前行"
            ]
        
        return random.choice(hooks)


class SectionProgressionDesigner:
    """段落递进设计师 - 确保歌词层层递进"""
    
    @staticmethod
    def design_verse_progression(verse_num: int) -> Dict[str, any]:
        """设计主歌的递进"""
        progressions = {
            1: {
                "depth": "表面",
                "content": "描述场景、画面",
                "emotion": "平静",
                "specificity": "宽泛"
            },
            2: {
                "depth": "深入",
                "content": "加入细节、感受",
                "emotion": "逐渐升温",
                "specificity": "具体"
            }
        }
        return progressions.get(verse_num, progressions[1])
    
    @staticmethod
    def design_emotion_arc(song_type: str) -> EmotionCurve:
        """设计情感弧线"""
        if song_type == "love":
            return EmotionCurve(
                intro_level=EmotionLevel.LOW,
                verse1_level=EmotionLevel.LOW,
                pre_chorus_level=EmotionLevel.MEDIUM,
                chorus_level=EmotionLevel.HIGH,
                verse2_level=EmotionLevel.MEDIUM,
                bridge_level=EmotionLevel.VERY_HIGH,
                final_chorus_level=EmotionLevel.HIGH
            )
        elif song_type == "sad":
            return EmotionCurve(
                intro_level=EmotionLevel.LOW,
                verse1_level=EmotionLevel.LOW,
                pre_chorus_level=EmotionLevel.MEDIUM,
                chorus_level=EmotionLevel.HIGH,
                verse2_level=EmotionLevel.LOW,
                bridge_level=EmotionLevel.LOW,
                final_chorus_level=EmotionLevel.LOW
            )
        elif song_type == "courage":
            return EmotionCurve(
                intro_level=EmotionLevel.LOW,
                verse1_level=EmotionLevel.LOW,
                pre_chorus_level=EmotionLevel.MEDIUM,
                chorus_level=EmotionLevel.HIGH,
                verse2_level=EmotionLevel.MEDIUM,
                bridge_level=EmotionLevel.VERY_HIGH,
                final_chorus_level=EmotionLevel.HIGH
            )
        else:
            return EmotionCurve()


class HookDesigner:
    """Hook记忆点设计师"""
    
    @staticmethod
    def create_emotional_hook(topic: str) -> str:
        """创建情感Hook"""
        hooks = [
            f"关于{topic}，我有话想说",
            f"给{topic}的一封信",
            f"因为{topic}，所以{topic}",
            f"{topic}教会我的事"
        ]
        return random.choice(hooks)
    
    @staticmethod
    def create_repetitive_hook(keyword: str) -> str:
        """创建重复Hook"""
        hooks = [
            f"{keyword} {keyword} {keyword}",
            f"不只是{keyword}",
            f"因为{keyword}",
            f"{keyword}的{keyword}",
            f"只有{keyword}"
        ]
        return random.choice(hooks)
    
    @staticmethod
    def create_unique_hook() -> str:
        """创建独特视角Hook"""
        hooks = [
            "如果时间可以倒流",
            "也许这就是答案",
            "原来如此",
            "我终于明白",
            "一切的开始"
        ]
        return random.choice(hooks)
    
    @staticmethod
    def design_hook_for_section(section: str, topic: str = "") -> str:
        """为不同段落设计Hook"""
        if section == "Chorus":
            return HookDesigner.create_repetitive_hook(topic or "爱")
        elif section == "Bridge":
            return HookDesigner.create_unique_hook()
        elif section == "Pre-Chorus":
            return HookDesigner.create_emotional_hook(topic or "你")
        else:
            return ""


class ProfessionalLyricAssistant:
    """专业歌词创作助手 - 整合所有高级功能"""
    
    def __init__(self):
        self.rhyme_manager = RhymeManager()
        self.quality_evaluator = LyricQualityEvaluator()
        self.inspiration_generator = InspirationSparkGenerator()
        self.progression_designer = SectionProgressionDesigner()
        self.hook_designer = HookDesigner()
    
    def get_inspiration(self) -> Dict[str, str]:
        """获取灵感火花"""
        emotion_combo = self.inspiration_generator.generate_emotion_combination()
        scene = self.inspiration_generator.generate_scene_prompt()
        metaphor = self.inspiration_generator.generate_metaphor()
        
        return {
            "emotion_combination": emotion_combo,
            "scene_prompt": scene,
            "metaphor": metaphor,
            "hook": self.inspiration_generator.generate_hook_line()
        }
    
    def evaluate_lyrics(self, lyrics: Dict[str, List[str]]) -> Dict[str, any]:
        """评估歌词质量"""
        return self.quality_evaluator.evaluate_song(lyrics)
    
    def design_emotion_curve(self, song_type: str) -> EmotionCurve:
        """设计情感曲线"""
        return self.progression_designer.design_emotion_arc(song_type)
    
    def get_verse_guidance(self, verse_num: int) -> Dict[str, str]:
        """获取主歌写作指导"""
        progression = self.progression_designer.design_verse_progression(verse_num)
        guidance = {
            1: f"第一段主歌应该{progression['content']}，保持{progression['emotion']}的情绪，使用{progression['specificity']}的描述",
            2: f"第二段主歌应该{progression['content']}，情绪{progression['emotion']}，细节要{progression['specificity']}"
        }
        return {
            "guidance": guidance.get(verse_num, ""),
            "progression": progression
        }
    
    def create_professional_hook(self, hook_type: HookType, topic: str = "") -> str:
        """创建专业的Hook"""
        if hook_type == HookType.EMOTIONAL:
            return self.hook_designer.create_emotional_hook(topic)
        elif hook_type == HookType.REPETITIVE:
            return self.hook_designer.create_repetitive_hook(topic)
        elif hook_type == HookType.UNIQUE:
            return self.hook_designer.create_unique_hook()
        elif hook_type == HookType.QUESTION:
            return "为什么" + (topic or "会这样")
        else:
            return self.inspiration_generator.generate_hook_line(topic)
    
    def generate_writing_tips(self, section: str, song_type: str = "") -> List[str]:
        """生成写作技巧"""
        tips_map = {
            "Verse": [
                "🎨 描写具体的场景和细节",
                "📝 用画面代替叙述",
                "💭 表达内心感受但不要直白",
                "🌅 可以使用时间、地点、天气等元素"
            ],
            "Pre-Chorus": [
                "🔊 开始提升情绪",
                "⏰ 为即将到来的高潮做铺垫",
                "💗 表达内心的纠结和犹豫",
                "🎯 引导听众期待副歌"
            ],
            "Chorus": [
                "🎯 核心主题要清晰",
                "💖 最触动人心的一句话",
                "🔄 简洁有力，容易记忆",
                "🎵 情绪最高点"
            ],
            "Bridge": [
                "🌟 情绪最通透的时刻",
                "💡 写醒悟、写成长、写决定",
                "✨ 可以打破之前的一些规律",
                "🎭 给听众惊喜"
            ]
        }
        
        return tips_map.get(section, ["继续创作！"])


# 使用示例和演示
def demo_professional_features():
    """演示专业进阶功能"""
    print("=" * 70)
    print("HeartMuLa 歌词创作专业进阶功能演示")
    print("=" * 70)
    
    assistant = ProfessionalLyricAssistant()
    
    # 1. 灵感火花
    print("\n📌 灵感火花生成")
    print("-" * 50)
    inspiration = assistant.get_inspiration()
    print(f"情绪组合: {inspiration['emotion_combination']['emotion']} {inspiration['emotion_combination']['subject']}")
    print(f"场景提示: {inspiration['scene_prompt']}")
    print(f"比喻句: {inspiration['metaphor']}")
    print(f"Hook: {inspiration['hook']}")
    
    # 2. 主歌写作指导
    print("\n📌 主歌写作指导")
    print("-" * 50)
    for verse_num in [1, 2]:
        guidance = assistant.get_verse_guidance(verse_num)
        print(f"第{verse_num}段主歌: {guidance['guidance']}")
    
    # 3. Hook设计
    print("\n📌 Hook记忆点设计")
    print("-" * 50)
    for hook_type in HookType:
        hook = assistant.create_professional_hook(hook_type, "爱")
        print(f"{hook_type.value}: {hook}")
    
    # 4. 情感曲线
    print("\n📌 情感曲线设计")
    print("-" * 50)
    for song_type in ["love", "sad", "courage"]:
        curve = assistant.design_emotion_curve(song_type)
        print(f"\n{song_type}类型歌曲情感曲线:")
        print(f"  Intro: {curve.intro_level.name}")
        print(f"  Verse 1: {curve.verse1_level.name}")
        print(f"  Pre-Chorus: {curve.pre_chorus_level.name}")
        print(f"  Chorus: {curve.chorus_level.name}")
        print(f"  Verse 2: {curve.verse2_level.name}")
        print(f"  Bridge: {curve.bridge_level.name}")
        print(f"  Final Chorus: {curve.final_chorus_level.name}")
    
    # 5. 段落写作技巧
    print("\n📌 各段落写作技巧")
    print("-" * 50)
    for section in ["Verse", "Pre-Chorus", "Chorus", "Bridge"]:
        tips = assistant.generate_writing_tips(section)
        print(f"\n{section}:")
        for tip in tips:
            print(f"  {tip}")
    
    print("\n" + "=" * 70)
    print("专业进阶功能演示完成！")
    print("=" * 70)


if __name__ == "__main__":
    demo_professional_features()
