#!/usr/bin/env python3
"""
歌词创作辅助模块 - 增强版测试
包含图片里的技巧：预副歌、告白/分手情歌模板等
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Union
import random
import re
from enum import Enum


class SongStructure(Enum):
    VERSE_CHORUS = "verse_chorus"
    ABABCB = "ababcb"
    AABA = "aaba"
    FULL_STRUCTURE = "full_structure"


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


class SongType(Enum):
    CONFESSION = "confession"
    BREAKUP = "breakup"


@dataclass
class LyricConfig:
    theme: str = "love"
    mood: str = "sad"
    song_structure: SongStructure = SongStructure.FULL_STRUCTURE
    song_type: Optional[SongType] = None
    language: str = "chinese"
    opening_technique: Optional[OpeningTechnique] = None
    narrative_technique: Optional[NarrativeTechnique] = None
    line_length: int = 7
    use_rhyme: bool = True
    use_imagery: bool = True
    num_verses: int = 2
    verse_lines: int = 4
    pre_chorus_lines: int = 2
    chorus_lines: int = 4
    bridge_lines: int = 3


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
        "love": ["月光", "星光", "玫瑰", "咖啡杯", "明信片", "夕阳", "微风", "烟火", "情书", "礼物"],
        "sad": ["落叶", "冷雨", "旧照片", "空房间", "孤灯", "咖啡凉了", "未发送的消息", "远去的背影", "断了的弦"],
        "happy": ["阳光", "花朵", "笑声", "奔跑", "拥抱", "彩虹", "星空", "舞蹈", "心跳"],
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
        SongStructure.AABA: ["Verse", "Verse", "Bridge", "Verse"],
        SongStructure.FULL_STRUCTURE: ["Verse 1", "Pre-Chorus", "Chorus", "Verse 2", "Pre-Chorus", "Chorus", "Bridge", "Chorus"]
    }

    # 图片里的超直白口诀
    WRITING_RULES = {
        "Verse": "写画面、写事情、写细节，不要喊口号，不要放金句",
        "Pre-Chorus": "写纠结、写犹豫、写铺垫，快要爆发但还没爆发",
        "Chorus": "写态度、写心声、写核心，一句话让人记住整首歌",
        "Bridge": "写醒悟、写成长、写决定，情绪最通透、最有力量"
    }

    # 具体歌曲类型模板
    SONG_TYPES = {
        SongType.CONFESSION: {
            "Verse 1": "遇见你的场景",
            "Pre-Chorus": "我很心动但不敢说",
            "Chorus": "我喜欢你、你是我的光",
            "Verse 2": "相处的小细节",
            "Bridge": "我决定勇敢一次"
        },
        SongType.BREAKUP: {
            "Verse 1": "分手的那天场景",
            "Pre-Chorus": "我还舍不得但必须放手",
            "Chorus": "谢谢你来过、我会好好的",
            "Verse 2": "后来的日子里",
            "Bridge": "终于释怀了"
        }
    }

    # 各部分功能说明（来自图片）
    SECTION_FUNCTIONS = {
        "Intro": "定风格、定情绪、进歌前铺垫",
        "Verse": "讲故事、铺画面、写细节（时间、地点、场景、心情、经历）",
        "Pre-Chorus": "情绪爬坡、从平静推向高潮",
        "Chorus": "核心主题、情绪最高点、最抓耳（态度、观点、告白、遗憾、释怀、梦想）",
        "Bridge": "写醒悟、写成长、写决定"
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
            "{scene}": random.choice(["街道", "天空", "房间", "街角", "窗边", "路口", "公园", "车站", "咖啡店", "操场"]),
            "{detail}": random.choice(["如此安静", "那么熟悉", "有点陌生", "像从前一样", "在等谁", "沉默着", "发着光", "暗下来"]),
            "{object}": random.choice(imagery) if imagery else "东西",
            "{action}": random.choice(["飘落", "走过", "关上", "打开", "想起", "忘记", "等待", "离开", "微笑", "哭泣"]),
            "{place}": random.choice(["城市", "小镇", "老街", "旧巷", "这里", "那里", "原地", "原地"]),
            "{mood}": random.choice(["很寂寞", "很孤单", "很温柔", "很冰冷", "很温暖", "很难过", "很想你", "很安静"]),
            "{something}": random.choice(["回忆", "梦想", "心事", "过去", "未来", "思念", "故事", "秘密", "秘密"]),
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
            "{feeling}": random.choice(["很想你", "很难过", "很孤单", "很温暖", "很幸福", "很紧张"]),
            "{line}": random.choice(["算了吧", "就这样", "再见吧", "别回头", "忘了吧", "我爱你"]),
            "{result}": random.choice(["不再回头", "各自安好", "不再相见", "变成回忆", "永远记得"]),
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

    def _generate_verse(self, verse_num: int = 1, num_lines: Optional[int] = None) -> List[str]:
        num_lines = num_lines or self.config.verse_lines
        verse = []
        rhyme_group = random.choice(list(self.templates.RHYME_DICTS.keys()))
        
        if self.config.song_type:
            song_type_template = self.templates.SONG_TYPES.get(self.config.song_type, {})
            if verse_num == 1:
                verse.append(f"记得{self._generate_opening(self.config.opening_technique)}")
            else:
                verse.append(f"后来{self._generate_opening(OpeningTechnique.TIME)}")
        else:
            verse.append(self._generate_opening(self.config.opening_technique))
        
        for i in range(1, num_lines):
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

    def _generate_pre_chorus(self, num_lines: Optional[int] = None) -> List[str]:
        num_lines = num_lines or self.config.pre_chorus_lines
        pre_chorus = []
        
        hesitation_words = [
            "我想说却又不敢",
            "心跳越来越快",
            "话到嘴边又咽下",
            "我在等一个回答",
            "我还在犹豫什么",
            "终于决定要开口",
            "这一次我不想错过",
            "我已经快忍不住了"
        ]
        
        for i in range(num_lines):
            if i == 0:
                pre_chorus.append(random.choice(hesitation_words))
            else:
                if self.config.use_rhyme:
                    prev_end = pre_chorus[i-1][-1] if pre_chorus[i-1] else ""
                    rhyme = None
                    for rg, words in self.templates.RHYME_DICTS.items():
                        if prev_end in words:
                            rhyme = rg
                            break
                    if rhyme:
                        pre_chorus.append(self._generate_rhyming_line(rhyme))
                    else:
                        pre_chorus.append(self._generate_random_line())
                else:
                    pre_chorus.append(self._generate_random_line())
        return pre_chorus

    def _generate_chorus(self, num_lines: Optional[int] = None) -> List[str]:
        num_lines = num_lines or self.config.chorus_lines
        chorus = []
        rhyme_group = random.choice(list(self.templates.RHYME_DICTS.keys()))
        
        hooks = []
        if self.config.song_type == SongType.CONFESSION:
            hooks = [
                "我喜欢你你知道吗",
                "你是我的光",
                "想和你在一起",
                "我的心只属于你"
            ]
        elif self.config.song_type == SongType.BREAKUP:
            hooks = [
                "谢谢你来过我的世界",
                "我会好好的",
                "我们都要幸福",
                "再见了我的爱"
            ]
        else:
            hooks = [
                f"{self.config.theme}是{random.choice(['一首歌', '一个梦', '一束光', '一场雨', '一阵风'])}",
                f"我{random.choice(['想你', '爱你', '等你', '忘不了你', '放不下'])}",
                f"就这样{random.choice(['吧', '了', '吧', '好吗', '行吗'])}"
            ]
        
        chorus.append(random.choice(hooks))
        for i in range(1, num_lines):
            if self.config.use_rhyme and i % 2 == 1:
                chorus.append(self._generate_rhyming_line(rhyme_group))
            else:
                chorus.append(self._generate_random_line())
        return chorus

    def _generate_bridge(self, num_lines: Optional[int] = None) -> List[str]:
        num_lines = num_lines or self.config.bridge_lines
        bridge = []
        
        realization_words = [
            "其实我早就该明白",
            "终于我想通了",
            "原来这就是成长",
            "我决定了",
            "从此以后"
        ]
        
        bridge.append(f"{random.choice(realization_words)}{self._generate_random_line(5)}")
        bridge.append(f"{self._generate_random_line(7)}")
        bridge.append(f"{self._generate_random_line(7)}")
        return bridge

    def generate(self, config: Optional[LyricConfig] = None) -> Dict[str, List[str]]:
        if config:
            self.config = config
        
        structure = self.templates.STRUCTURE_TEMPLATES.get(self.config.song_structure)
        if not structure:
            structure = self.templates.STRUCTURE_TEMPLATES[SongStructure.FULL_STRUCTURE]
        
        song = {}
        
        for part in structure:
            if "Verse 1" in part:
                song["Verse 1"] = self._generate_verse(1)
            elif "Verse 2" in part:
                song["Verse 2"] = self._generate_verse(2)
            elif "Verse" in part:
                verse_num = len([k for k in song.keys() if "Verse" in k]) + 1
                song[f"Verse {verse_num}"] = self._generate_verse(verse_num)
            elif "Pre-Chorus" in part:
                song["Pre-Chorus"] = self._generate_pre_chorus()
            elif "Chorus" in part:
                if "Chorus" not in song:
                    song["Chorus"] = self._generate_chorus()
            elif "Bridge" in part:
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
                "主歌：写画面、写事情、写细节，不要喊口号",
                "预副歌：写纠结、写犹豫、写铺垫，快要爆发",
                "副歌：写态度、写心声、写核心，让人记住",
                "桥段：写醒悟、写成长、写决定，情绪最通透"
            ],
            "rhyme": [
                "隔句押韵：ABAB式更自然",
                "适当换韵：主歌副歌不同韵",
                "不要为了押韵牺牲意思",
                "半押半散更灵活"
            ],
            "song_types": [
                "告白情歌：相遇场景→心动犹豫→大声表白",
                "分手情歌：分手那天→舍不得放手→释怀放下"
            ]
        }
        if category and category in tips:
            return tips[category]
        all_tips = []
        for t in tips.values():
            all_tips.extend(t)
        return all_tips

    def get_section_guide(self, section: str) -> str:
        return LyricTemplateLibrary.WRITING_RULES.get(section, "")

    def generate_confession_song(self) -> str:
        config = LyricConfig(
            theme="love",
            mood="happy",
            song_structure=SongStructure.FULL_STRUCTURE,
            song_type=SongType.CONFESSION
        )
        song = self.generator.generate(config)
        formatted = self.generator.format_song(song)
        return formatted

    def generate_breakup_song(self) -> str:
        config = LyricConfig(
            theme="love",
            mood="sad",
            song_structure=SongStructure.FULL_STRUCTURE,
            song_type=SongType.BREAKUP
        )
        song = self.generator.generate(config)
        formatted = self.generator.format_song(song)
        return formatted


def print_separator(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def test_module():
    assistant = LyricsWritingAssistant()
    
    # 1. 测试创作技巧
    print_separator("1. 歌词创作技巧（来自图片）")
    tips = assistant.get_tips()
    for i, tip in enumerate(tips[:10], 1):
        print(f"{i}. {tip}")
    
    # 2. 测试各部分写作口诀
    print_separator("2. 各部分写作口诀（超直白）")
    for section, rule in LyricTemplateLibrary.WRITING_RULES.items():
        print(f"[{section}] {rule}")
    
    # 3. 测试各部分功能说明
    print_separator("3. 各部分功能说明（来自图片）")
    for section, func in LyricTemplateLibrary.SECTION_FUNCTIONS.items():
        print(f"[{section}] {func}")
    
    # 4. 生成告白情歌
    print_separator("4. 生成示例：告白情歌")
    confession_song = assistant.generate_confession_song()
    print(confession_song)
    
    # 5. 生成分手情歌
    print_separator("5. 生成示例：分手/释怀情歌")
    breakup_song = assistant.generate_breakup_song()
    print(breakup_song)
    
    print("\n" + "=" * 60)
    print("  ✨ 所有功能测试完成！✨")
    print("=" * 60)


if __name__ == "__main__":
    test_module()
