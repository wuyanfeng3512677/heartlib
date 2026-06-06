from dataclasses import dataclass
from typing import List, Dict, Optional, Union
import random
import re
from enum import Enum


class SongStructure(Enum):
    VERSE_CHORUS = "verse_chorus"
    ABABCB = "ababcb"
    AABA = "aaba"


class OpeningTechnique(Enum):
    SCENE = "scene"
    ACTION = "action"
    SOUND = "sound"
    TIME = "time"
    QUESTION = "question"
    CONTRAST = "contrast"
    OBJECT = "object"
    LOCATION = "location"
    WEATHER = "weather"
    LINE = "line"


class NarrativeTechnique(Enum):
    MOMENT = "moment"
    FRAGMENT = "fragment"
    MEMORY = "memory"
    DREAM = "dream"
    MICRO_STORY = "micro_story"
    THIRD_PERSON = "third_person"
    FIRST_PERSON = "first_person"
    SECOND_PERSON = "second_person"
    TIME_JUMP = "time_jump"
    LEAVE_BLANK = "leave_blank"


@dataclass
class LyricConfig:
    theme: str = "love"
    mood: str = "sad"
    song_structure: SongStructure = SongStructure.ABABCB
    language: str = "chinese"
    opening_technique: Optional[OpeningTechnique] = None
    narrative_technique: Optional[NarrativeTechnique] = None
    line_length: int = 7
    use_rhyme: bool = True
    use_imagery: bool = True
    num_verses: int = 2
    verse_lines: int = 4
    chorus_lines: int = 4


class LyricTemplateLibrary:
    OPENINGS = {
        OpeningTechnique.SCENE: [
            "{scene} {detail}",
            "窗外的{object} {action}",
            "{place}的{scene} {mood}"
        ],
        OpeningTechnique.ACTION: [
            "我{action} {object}",
            "{action}着{something}",
            "轻轻{action} {detail}"
        ],
        OpeningTechnique.SOUND: [
            "{sound}响着 {detail}",
            "听见{sound} {feeling}",
            "{sound}在{place} {state}"
        ],
        OpeningTechnique.TIME: [
            "{time}的{scene} {state}",
            "{time} {scene}还没{action}",
            "从{time}到{time} {feeling}"
        ],
        OpeningTechnique.QUESTION: [
            "{someone}以后 {question}",
            "{thing}到底 {question}",
            "为什么{thing} {question}"
        ],
        OpeningTechnique.CONTRAST: [
            "{positive}越{adj} 我越{negative}",
            "{crowd}越{adj} 我越{lonely}",
            "{light}越{adj} 我越{dark}"
        ],
        OpeningTechnique.OBJECT: [
            "那个{object} 还{state}",
            "这把{object} 留着{detail}",
            "{object}里藏着{something}"
        ],
        OpeningTechnique.LOCATION: [
            "这座{place} 装不下{something}",
            "{place}的{scene} {feeling}",
            "在{place} {action}"
        ],
        OpeningTechnique.WEATHER: [
            "这场{weather} {action}",
            "{weather}淋湿了{something}",
            "{weather}的{day} {feeling}"
        ],
        OpeningTechnique.LINE: [
            "{line} 我们就到这里",
            "{line} {feeling}",
            "{line} {result}"
        ]
    }

    IMAGERY = {
        "love": ["月光", "星光", "玫瑰", "咖啡杯", "明信片", "夕阳", "微风", "烟火"],
        "sad": ["落叶", "冷雨", "旧照片", "空房间", "孤灯", "咖啡凉了", "未发送的消息", "远去的背影"],
        "happy": ["阳光", "花朵", "笑声", "奔跑", "拥抱", "彩虹", "星空", "舞蹈"],
        "nostalgia": ["旧时光", "老地方", "照片", "回忆", "从前", "小时候", "老街", "老歌"],
        "courage": ["翅膀", "远方", "路", "光", "前行", "坚持", "勇气", "力量"]
    }

    RHYME_DICTS = {
        "a": ["她", "花", "家", "吧", "呀", "啦", "下", "大", "发", "吧"],
        "ai": ["来", "爱", "在", "白", "开", "海", "彩", "猜", "才", "怀"],
        "an": ["看", "站", "天", "晚", "难", "暖", "完", "满", "散", "转"],
        "ang": ["想", "光", "望", "样", "唱", "长", "方", "上", "亮", "香"],
        "ao": ["跳", "笑", "找", "好", "老", "跑", "叫", "要", "抱", "到"],
        "e": ["么", "得", "个", "热", "说", "可", "呢", "歌", "河", "客"],
        "ei": ["给", "美", "飞", "水", "谁", "泪", "累", "类", "雷", "贵"],
        "en": ["真", "深", "人", "本", "很", "门", "分", "身", "心", "新"],
        "eng": ["声", "能", "风", "梦", "生", "等", "城", "灯", "星", "情"],
        "i": ["你", "里", "起", "去", "记", "气", "地", "事", "意", "世"],
        "ian": ["边", "眼", "年", "天", "前", "间", "点", "片", "面", "线"],
        "iao": ["跳", "笑", "叫", "要", "飘", "摇", "照", "妙", "巧", "调"],
        "ie": ["写", "谢", "夜", "街", "别", "些", "界", "姐", "借", "鞋"],
        "in": ["心", "今", "金", "近", "进", "尽", "紧", "劲", "禁", "锦"],
        "ing": ["听", "情", "行", "明", "星", "命", "定", "影", "醒", "应"],
        "ou": ["走", "手", "头", "有", "友", "后", "候", "久", "就", "旧"],
        "u": ["路", "住", "书", "出", "处", "苦", "服", "物", "助", "注"],
        "ua": ["花", "画", "话", "华", "化", "发", "打", "拿", "下", "怕"],
        "uo": ["说", "多", "过", "火", "活", "落", "错", "作", "所", "破"]
    }

    STRUCTURE_TEMPLATES = {
        SongStructure.VERSE_CHORUS: ["Verse", "Chorus", "Verse", "Chorus", "Chorus"],
        SongStructure.ABABCB: ["Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus"],
        SongStructure.AABA: ["Verse", "Verse", "Bridge", "Verse"]
    }

    TRANSITIONS = {
        "Verse->Chorus": ["于是", "所以", "而如今", "可", "但是", "然而", "不过", "直到"],
        "Chorus->Verse": ["还记得", "想起", "又看见", "每当", "每当我"],
        "Verse->Bridge": ["其实", "我知道", "也许", "如果", "假如"],
        "Bridge->Chorus": ["所以", "于是", "因此", "就这样"]
    }


class LyricGenerator:
    def __init__(self, config: Optional[LyricConfig] = None):
        self.config = config or LyricConfig()
        self.templates = LyricTemplateLibrary()
        self._used_lines = set()

    def _generate_opening(self, technique: Optional[OpeningTechnique] = None) -> str:
        if technique is None:
            technique = random.choice(list(OpeningTechnique))
        templates = self.templates.OPENINGS.get(technique, [])
        if not templates:
            return self._generate_random_line()
        template = random.choice(templates)
        return self._fill_template(template)

    def _fill_template(self, template: str) -> str:
        mood = self.config.mood
        theme = self.config.theme
        imagery = self.templates.IMAGERY.get(theme, []) + self.templates.IMAGERY.get(mood, [])
        
        fillings = {
            "{scene}": random.choice(["街道", "天空", "房间", "街角", "窗边", "路口", "公园", "车站"]),
            "{detail}": random.choice(["如此安静", "那么熟悉", "有点陌生", "像从前一样", "在等谁", "沉默着", "发着光", "暗下来"]),
            "{object}": random.choice(imagery) if imagery else "东西",
            "{action}": random.choice(["飘落", "走过", "关上", "打开", "想起", "忘记", "等待", "离开"]),
            "{place}": random.choice(["城市", "小镇", "老街", "旧巷", "这里", "那里", "原地", "原地"]),
            "{mood}": random.choice(["很寂寞", "很孤单", "很温柔", "很冰冷", "很温暖", "很难过", "很想你", "很安静"]),
            "{something}": random.choice(["回忆", "梦想", "心事", "过去", "未来", "思念", "故事", "秘密"]),
            "{time}": random.choice(["凌晨三点", "深夜", "黄昏", "午后", "清晨", "那年", "昨天", "今天"]),
            "{state}": random.choice(["还没睡", "还亮着", "还等着", "还在那", "没变", "依旧", "依然", "如故"]),
            "{someone}": random.choice(["你走", "他走", "我们分开", "告别后", "离开后"]),
            "{question}": random.choice(["谁替谁温柔", "到底有多远", "还会不会回来", "还有什么意义", "该怎么办"]),
            "{positive}": random.choice(["人群", "笑声", "烟火", "阳光", "热闹"]),
            "{negative}": random.choice(["孤单", "寂寞", "难过", "想你", "安静"]),
            "{crowd}": random.choice(["人群", "世界", "周围", "大家"]),
            "{lonely}": random.choice(["像孤岛", "很孤单", "很寂寞", "格格不入"]),
            "{light}": random.choice(["灯光", "阳光", "月光", "星光"]),
            "{dark}": random.choice(["黑暗", "难过", "孤单", "想你"]),
            "{weather}": random.choice(["冷雨", "微风", "雪", "阳光", "大风"]),
            "{day}": random.choice(["夜晚", "白天", "午后", "黄昏"]),
            "{feeling}": random.choice(["很想你", "很难过", "很孤单", "很温暖", "很幸福"]),
            "{line}": random.choice(["算了吧", "就这样", "再见吧", "别回头", "忘了吧"]),
            "{result}": random.choice(["不再回头", "各自安好", "不再相见", "变成回忆"]),
            "{adj}": random.choice(["热闹", "明亮", "温暖", "寒冷", "安静"]),
        }
        
        result = template
        for key, value in fillings.items():
            if key in result:
                result = result.replace(key, value)
        return result

    def _generate_random_line(self, length: Optional[int] = None) -> str:
        length = length or self.config.line_length
        imagery = self.templates.IMAGERY.get(self.config.theme, []) + self.templates.IMAGERY.get(self.config.mood, [])
        words = imagery + ["我", "你", "我们", "心", "爱", "梦", "想", "走", "看", "听", "说", "笑", "哭", "等", "离开", "回来", "永远", "瞬间", "昨天", "明天"]
        return "".join(random.sample(words, min(length, len(words))))

    def _get_rhyme_words(self, end_char: str) -> List[str]:
        for rhyme_group in self.templates.RHYME_DICTS.values():
            if end_char in rhyme_group:
                return rhyme_group
        return []

    def _generate_rhyming_line(self, end_rhyme: str, length: Optional[int] = None) -> str:
        length = length or self.config.line_length
        rhyme_words = self.templates.RHYME_DICTS.get(end_rhyme, [])
        if not rhyme_words:
            return self._generate_random_line(length)
        base = self._generate_random_line(length - 1)
        return base + random.choice(rhyme_words)

    def _generate_verse(self, num_lines: Optional[int] = None) -> List[str]:
        num_lines = num_lines or self.config.verse_lines
        verse = []
        rhyme_group = random.choice(list(self.templates.RHYME_DICTS.keys()))
        
        for i in range(num_lines):
            if i == 0:
                line = self._generate_opening(self.config.opening_technique)
            else:
                if self.config.use_rhyme and i % 2 == 1:
                    prev_end = verse[i-1][-1] if verse[i-1] else ""
                    rhyme = None
                    for rg, words in self.templates.RHYME_DICTS.items():
                        if prev_end in words:
                            rhyme = rg
                            break
                    if rhyme:
                        line = self._generate_rhyming_line(rhyme)
                    else:
                        line = self._generate_random_line()
                else:
                    line = self._generate_random_line()
            verse.append(line)
        return verse

    def _generate_chorus(self, num_lines: Optional[int] = None) -> List[str]:
        num_lines = num_lines or self.config.chorus_lines
        chorus = []
        rhyme_group = random.choice(list(self.templates.RHYME_DICTS.keys()))
        
        hooks = [
            f"{self.config.theme}是{random.choice(['一首歌', '一个梦', '一束光', '一场雨', '一阵风'])}",
            f"我{random.choice(['想你', '爱你', '等你', '忘不了你', '放不下'])}",
            f"就这样{random.choice(['吧', '了', '吧', '好吗', '行吗'])}",
        ]
        
        chorus.append(random.choice(hooks))
        for i in range(1, num_lines):
            if self.config.use_rhyme and i % 2 == 1:
                chorus.append(self._generate_rhyming_line(rhyme_group))
            else:
                chorus.append(self._generate_random_line())
        return chorus

    def _generate_bridge(self) -> List[str]:
        bridge = []
        transitions = ["其实", "也许", "如果", "我知道", "可是", "然而"]
        bridge.append(f"{random.choice(transitions)}{self._generate_random_line(5)}")
        bridge.append(f"{self._generate_random_line(7)}")
        bridge.append(f"{self._generate_random_line(7)}")
        return bridge

    def generate(self, config: Optional[LyricConfig] = None) -> Dict[str, List[str]]:
        if config:
            self.config = config
        
        structure = self.templates.STRUCTURE_TEMPLATES.get(self.config.song_structure)
        if not structure:
            structure = self.templates.STRUCTURE_TEMPLATES[SongStructure.ABABCB]
        
        song = {}
        
        for part in structure:
            if part == "Verse":
                verse_num = len([k for k in song.keys() if "Verse" in k]) + 1
                song[f"Verse {verse_num}"] = self._generate_verse()
            elif part == "Chorus":
                if "Chorus" not in song:
                    song["Chorus"] = self._generate_chorus()
            elif part == "Bridge":
                song["Bridge"] = self._generate_bridge()
        
        return song

    def format_song(self, song: Dict[str, List[str]]) -> str:
        lines = []
        for section, content in song.items():
            lines.append(f"[{section}]")
            lines.extend(content)
            lines.append("")
        return "\n".join(lines)


class LyricsWritingAssistant:
    def __init__(self):
        self.generator = LyricGenerator()
        self.inspiration_library = []

    def get_tips(self, category: Optional[str] = None) -> List[str]:
        tips = {
            "opening": [
                "从画面开始：窗外的梧桐又落满深秋",
                "从动作切入：我轻轻关上没说完的话",
                "用声音开篇：旧唱片转着熟悉的旋律",
                "从时间落笔：凌晨三点的街灯还没睡",
                "用问题开头：你走以后风替谁温柔"
            ],
            "imagery": [
                "把抽象变具体：不说\"我想你\"，说\"你的咖啡杯还在桌上\"",
                "使用陌生化比喻：思念是没地址的信",
                "拟人化：路灯低着头偷看我难过",
                "通感：你的离开苦得像中药"
            ],
            "structure": [
                "主歌铺景，副歌抒情",
                "主歌讲故事，副歌讲心情",
                "层层递进：有点难过→很难过→崩溃",
                "首尾呼应：开头温柔，结尾你已不在"
            ],
            "rhyme": [
                "隔句押韵：ABAB式更自然",
                "适当换韵：主歌副歌不同韵",
                "不要为了押韵牺牲意思",
                "半押半散更灵活"
            ]
        }
        if category and category in tips:
            return tips[category]
        all_tips = []
        for t in tips.values():
            all_tips.extend(t)
        return all_tips

    def generate_with_tips(self, theme: str, mood: str) -> str:
        config = LyricConfig(theme=theme, mood=mood)
        song = self.generator.generate(config)
        formatted = self.generator.format_song(song)
        tips = self.get_tips()
        tip_section = "\n\n💡 歌词创作技巧建议：\n" + "\n".join([f"- {t}" for t in tips[:5]])
        return formatted + tip_section

    def brainstorm_themes(self) -> List[str]:
        return [
            "想念一个人",
            "告别一段感情",
            "追逐梦想",
            "怀念过去",
            "城市孤独",
            "雨后的心情",
            "深夜的思考",
            "旅行的意义",
            "友谊万岁",
            "自我成长"
        ]

    def refine_lyric(self, line: str, suggestion: str) -> str:
        if "更具体" in suggestion:
            imagery = self.generator.templates.IMAGERY.get("sad", [])
            if imagery:
                return f"{line}，{random.choice(imagery)}还在"
        elif "更有画面" in suggestion:
            scenes = ["窗外", "街角", "路灯下", "旧房间", "车站"]
            if scenes:
                return f"{random.choice(scenes)}，{line}"
        return line
