#!/usr/bin/env python3
"""
HeartMuLa 专业进阶歌词创作功能演示 - 独立版本
包含所有专业功能的完整演示
"""

from enum import Enum
import random


# 重新定义所需的类
class EmotionLevel(Enum):
    VERY_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGH = 5


class HookType(Enum):
    EMOTIONAL = "emotional"
    REPETITIVE = "repetitive"
    UNIQUE = "unique"
    QUESTION = "question"


class NarrativePerspective(Enum):
    FIRST_PERSON = "first_person"
    SECOND_PERSON = "second_person"
    THIRD_PERSON = "third_person"
    OMNISCIENT = "omniscient"
    DIALOGUE = "dialogue"


class EmotionCurve:
    def __init__(self,
                 intro_level=EmotionLevel.LOW,
                 verse1_level=EmotionLevel.LOW,
                 pre_chorus_level=EmotionLevel.MEDIUM,
                 chorus_level=EmotionLevel.HIGH,
                 verse2_level=EmotionLevel.MEDIUM,
                 bridge_level=EmotionLevel.VERY_HIGH,
                 final_chorus_level=EmotionLevel.HIGH):
        self.intro_level = intro_level
        self.verse1_level = verse1_level
        self.pre_chorus_level = pre_chorus_level
        self.chorus_level = chorus_level
        self.verse2_level = verse2_level
        self.bridge_level = bridge_level
        self.final_chorus_level = final_chorus_level


class RhymeManager:
    def __init__(self):
        self.rhyme_database = {
            "a": ["她", "花", "家", "吧", "呀", "啦", "下", "大", "发", "沙", "茶", "麻", "拿"],
            "ai": ["来", "爱", "在", "白", "开", "海", "彩", "猜", "才", "怀", "买", "卖", "派"],
            "an": ["看", "站", "天", "晚", "难", "暖", "完", "满", "散", "转", "班", "半", "办"],
            "ang": ["想", "光", "望", "样", "唱", "长", "方", "上", "亮", "香", "忙", "放", "量"],
            "ao": ["跳", "笑", "找", "好", "老", "跑", "叫", "要", "抱", "到", "草", "早", "高"],
            "e": ["么", "得", "个", "热", "说", "可", "呢", "歌", "河", "客", "乐", "车", "色"],
            "ei": ["给", "美", "飞", "水", "谁", "泪", "累", "类", "雷", "贵", "北", "备", "背"],
            "en": ["真", "深", "人", "本", "很", "门", "分", "身", "心", "新", "文", "温", "问"],
            "eng": ["声", "能", "风", "梦", "生", "等", "城", "灯", "星", "情", "成", "程", "疼"],
            "i": ["你", "里", "起", "去", "记", "气", "地", "事", "意", "世", "离", "低", "底"],
            "ian": ["边", "眼", "年", "天", "前", "间", "点", "片", "面", "线", "电", "连", "脸"],
            "iao": ["跳", "笑", "叫", "要", "飘", "摇", "照", "妙", "巧", "调", "小", "表", "秒"],
            "ie": ["写", "谢", "夜", "街", "别", "些", "界", "姐", "借", "鞋", "也", "野", "业"],
            "in": ["心", "今", "金", "近", "进", "尽", "紧", "劲", "禁", "锦", "音", "阴", "银"],
            "ing": ["听", "情", "行", "明", "星", "命", "定", "影", "醒", "应", "轻", "清", "青"],
            "ou": ["走", "手", "头", "有", "友", "后", "候", "久", "就", "旧", "楼", "留", "流"],
            "u": ["路", "住", "书", "出", "处", "苦", "服", "物", "助", "注", "不", "步", "部"],
            "ua": ["花", "画", "话", "华", "化", "发", "打", "拿", "下", "怕", "瓜", "挂", "夸"],
            "uo": ["说", "多", "过", "火", "活", "落", "错", "作", "所", "破", "国", "果", "或"]
        }
        
        self.emotion_rhyme_map = {
            "happy": ["ang", "ai", "ao", "iao"],
            "sad": ["i", "in", "ing", "en"],
            "love": ["ai", "iang", "iang"],
            "courage": ["ang", "eng", "ong"],
            "nostalgia": ["i", "an", "en"]
        }
    
    def get_rhyme_for_emotion(self, emotion: str) -> str:
        candidates = self.emotion_rhyme_map.get(emotion, ["a", "ai", "an"])
        return random.choice(candidates)
    
    def get_rhyme_words(self, rhyme_type: str, count: int = 5) -> list:
        words = self.rhyme_database.get(rhyme_type, [])
        if len(words) >= count:
            return random.sample(words, count)
        return words
    
    def match_rhyme(self, word: str):
        for rhyme, words in self.rhyme_database.items():
            if word in words:
                return rhyme
        return None


class LyricQualityEvaluator:
    @staticmethod
    def evaluate_rhyme_quality(lyrics):
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
    def evaluate_imagery_density(lyrics):
        imagery_words = ["月", "星", "光", "风", "雨", "雪", "花", "叶", "海", "山", "路", "街", "灯"]
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
    def evaluate_song(lyrics):
        all_lines = []
        for section_lines in lyrics.values():
            all_lines.extend(section_lines)
        
        rhyme_eval = LyricQualityEvaluator.evaluate_rhyme_quality(all_lines)
        imagery_eval = LyricQualityEvaluator.evaluate_imagery_density(all_lines)
        
        overall_score = rhyme_eval["score"] * 0.5 + imagery_eval["score"] * 0.5
        suggestions = []
        if rhyme_eval["score"] < 0.6:
            suggestions.append("💡 建议：可以加强押韵的规律性")
        if imagery_eval["score"] < 0.8:
            suggestions.append("💡 建议：可以增加更多意象和画面感")
        
        return {
            "overall_score": overall_score,
            "rhyme": rhyme_eval,
            "imagery": imagery_eval,
            "suggestions": suggestions if suggestions else ["✨ 歌词质量良好，继续保持！"]
        }


class InspirationSparkGenerator:
    @staticmethod
    def generate_emotion_combination():
        emotions = ["温暖的", "冰冷的", "甜蜜的", "苦涩的", "明亮的", "灰暗的"]
        subjects = ["离别", "重逢", "思念", "遗忘", "成长", "失去"]
        return {
            "emotion": random.choice(emotions),
            "subject": random.choice(subjects)
        }
    
    @staticmethod
    def generate_scene_prompt():
        templates = [
            "{time}的{place}",
            "{weather}的{place}",
            "看见{object}想起{feeling}"
        ]
        template = random.choice(templates)
        
        replacements = {
            "{time}": random.choice(["凌晨三点", "深夜", "黄昏"]),
            "{place}": random.choice(["街道", "咖啡厅", "天台"]),
            "{weather}": random.choice(["下雨", "下雪", "起风"]),
            "{object}": random.choice(["那张照片", "这把吉他"]),
            "{feeling}": random.choice(["你", "过去"])
        }
        
        for key, value in replacements.items():
            if key in template:
                template = template.replace(key, value)
        
        return template
    
    @staticmethod
    def generate_metaphor():
        metaphors = [
            "你是我的{comparison}",
            "爱是{comparison}",
            "思念是{comparison}"
        ]
        comparisons = ["一首歌", "一场梦", "一束光", "一阵风", "一片海"]
        template = random.choice(metaphors)
        return template.replace("{comparison}", random.choice(comparisons))
    
    @staticmethod
    def generate_hook_line(song_type="love"):
        hooks = {
            "love": ["你是我心中的那束光", "我想和你在一起"],
            "sad": ["谢谢你来过", "我会好好的"],
            "dream": ["我要去追寻我的梦", "没有人能阻挡我"]
        }
        return random.choice(hooks.get(song_type, ["这就是人生"]))


class HookDesigner:
    @staticmethod
    def create_emotional_hook(topic=""):
        return f"关于{topic}，我有话想说"
    
    @staticmethod
    def create_repetitive_hook(keyword=""):
        return f"{keyword} {keyword} {keyword}"
    
    @staticmethod
    def create_unique_hook():
        return random.choice(["如果时间可以倒流", "也许这就是答案", "原来如此", "我终于明白"])


class SectionProgressionDesigner:
    @staticmethod
    def design_emotion_arc(song_type):
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
        else:
            return EmotionCurve()


class ProfessionalLyricAssistant:
    def __init__(self):
        self.rhyme_manager = RhymeManager()
        self.quality_evaluator = LyricQualityEvaluator()
        self.inspiration_generator = InspirationSparkGenerator()
        self.progression_designer = SectionProgressionDesigner()
        self.hook_designer = HookDesigner()
    
    def get_inspiration(self):
        return {
            "emotion_combination": self.inspiration_generator.generate_emotion_combination(),
            "scene_prompt": self.inspiration_generator.generate_scene_prompt(),
            "metaphor": self.inspiration_generator.generate_metaphor(),
            "hook": self.inspiration_generator.generate_hook_line()
        }
    
    def evaluate_lyrics(self, lyrics):
        return self.quality_evaluator.evaluate_song(lyrics)
    
    def design_emotion_curve(self, song_type):
        return self.progression_designer.design_emotion_arc(song_type)
    
    def create_professional_hook(self, hook_type, topic=""):
        if hook_type == HookType.EMOTIONAL:
            return self.hook_designer.create_emotional_hook(topic)
        elif hook_type == HookType.REPETITIVE:
            return self.hook_designer.create_repetitive_hook(topic)
        elif hook_type == HookType.UNIQUE:
            return self.hook_designer.create_unique_hook()
        elif hook_type == HookType.QUESTION:
            return "为什么" + topic
        return ""
    
    def generate_writing_tips(self, section):
        tips_map = {
            "Verse": ["🎨 描写具体的场景和细节", "📝 用画面代替叙述"],
            "Pre-Chorus": ["🔊 开始提升情绪", "⏰ 为即将到来的高潮做铺垫"],
            "Chorus": ["🎯 核心主题要清晰", "💖 最触动人心的一句话"],
            "Bridge": ["🌟 情绪最通透的时刻", "💡 写醒悟、写成长、写决定"]
        }
        return tips_map.get(section, ["继续创作！"])


def print_separator(title):
    print("\n" + "=" * 80)
    print(f"  {title}".center(80))
    print("=" * 80)


def main():
    print_separator("🎵 HeartMuLa 专业进阶歌词创作功能演示")
    
    assistant = ProfessionalLyricAssistant()
    
    # 1. 情感曲线设计
    print_separator("🎭 情感曲线设计")
    for song_type in ["love", "sad", "courage"]:
        curve = assistant.design_emotion_curve(song_type)
        print(f"\n📀 {song_type.upper()} 歌曲情感曲线:")
        sections = [
            ("Intro", curve.intro_level),
            ("Verse 1", curve.verse1_level),
            ("Pre-Chorus", curve.pre_chorus_level),
            ("Chorus", curve.chorus_level),
            ("Verse 2", curve.verse2_level),
            ("Bridge", curve.bridge_level)
        ]
        for section, level in sections:
            bar = "█" * level.value + "░" * (5 - level.value)
            print(f"  {section:15} [{bar}] {level.name}")
    
    # 2. Hook设计
    print_separator("🎣 Hook记忆点设计")
    print("\n情感Hook:", assistant.create_professional_hook(HookType.EMOTIONAL, "梦想"))
    print("重复Hook:", assistant.create_professional_hook(HookType.REPETITIVE, "爱"))
    print("独特Hook:", assistant.create_professional_hook(HookType.UNIQUE))
    print("疑问Hook:", assistant.create_professional_hook(HookType.QUESTION, "离别"))
    
    # 3. 灵感火花
    print_separator("💡 灵感火花生成")
    for i in range(3):
        inspiration = assistant.get_inspiration()
        print(f"\n灵感 {i+1}:")
        print(f"  情绪组合: {inspiration['emotion_combination']['emotion']}{inspiration['emotion_combination']['subject']}")
        print(f"  场景提示: {inspiration['scene_prompt']}")
        print(f"  比喻句: {inspiration['metaphor']}")
        print(f"  Hook: {inspiration['hook']}")
    
    # 4. 质量评估
    print_separator("📊 歌词质量评估")
    sample_lyrics = {
        "Verse 1": ["窗外的月光洒在街道上", "我独自走在这熟悉的地方", "想起曾经的点点滴滴"],
        "Chorus": ["你是我心中的那束光", "照亮我前行的方向"]
    }
    
    print("\n📝 示例歌词:")
    for section, lines in sample_lyrics.items():
        print(f"  [{section}]")
        for line in lines:
            print(f"    {line}")
    
    evaluation = assistant.evaluate_lyrics(sample_lyrics)
    print("\n📈 评估结果:")
    print(f"  综合评分: {evaluation['overall_score']:.2f}/1.00")
    print(f"  押韵质量: {evaluation['rhyme']['detail']}")
    print(f"  意象密度: {evaluation['imagery']['detail']}")
    for suggestion in evaluation['suggestions']:
        print(f"  {suggestion}")
    
    # 5. 韵脚管理
    print_separator("🎵 智能韵脚管理")
    manager = RhymeManager()
    print("\n根据情绪匹配韵脚:")
    for emotion in ["happy", "sad", "love", "courage"]:
        rhyme = manager.get_rhyme_for_emotion(emotion)
        words = manager.get_rhyme_words(rhyme, 5)
        print(f"\n  {emotion}情绪 → 韵脚「{rhyme}」")
        print(f"    示例: {', '.join(words)}")
    
    # 6. 写作技巧
    print_separator("📖 段落写作指导")
    for section in ["Verse", "Pre-Chorus", "Chorus", "Bridge"]:
        print(f"\n🎯 {section}:")
        for tip in assistant.generate_writing_tips(section):
            print(f"  {tip}")
    
    print_separator("✨ 专业功能演示完成！")
    print("\n🚀 立即开始创作吧！")


if __name__ == "__main__":
    main()
