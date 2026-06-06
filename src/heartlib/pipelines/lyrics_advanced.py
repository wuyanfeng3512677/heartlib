from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union, Callable
import random
import re
from enum import Enum
from collections import defaultdict


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


class SongType(Enum):
    CONFESSION = "confession"
    BREAKUP = "breakup"
    NOSTALGIA = "nostalgia"
    COURAGE = "courage"
    DREAM = "dream"
    FRIENDSHIP = "friendship"
    LONELINESS = "loneliness"
    HOPE = "hope"


class MusicStyle(Enum):
    CHINESE_FOLK = "chinese_folk"
    HIPHOP = "hiphop"
    BALLAD = "ballad"
    ROCK = "rock"
    ELECTRONIC = "electronic"
    RNB = "rnb"


class RhymeScheme(Enum):
    AABB = "aabb"
    ABAB = "abab"
    ABBA = "abba"
    ABCB = "abcb"
    FREE = "free"


@dataclass
class LyricConfig:
    theme: str = "love"
    mood: str = "sad"
    song_structure: SongStructure = SongStructure.FULL_STRUCTURE
    song_type: Optional[SongType] = None
    music_style: Optional[MusicStyle] = None
    language: str = "chinese"
    opening_technique: Optional[OpeningTechnique] = None
    rhyme_scheme: RhymeScheme = RhymeScheme.ABAB
    line_length: int = 7
    use_rhyme: bool = True
    use_imagery: bool = True
    num_verses: int = 2
    verse_lines: int = 4
    pre_chorus_lines: int = 2
    chorus_lines: int = 4
    bridge_lines: int = 3
    use_advanced_devices: bool = True


class AdvancedLyricTemplates:
    # 进阶修辞手法模板
    FIGURATIVE_LANGUAGE = {
        "metaphor": [
            "{subject}是{object}",
            "{subject}像{object}",
            "{subject}是{adjective}的{object}"
        ],
        "personification": [
            "{object}{action}",
            "{object}在{action}",
            "{object}{feeling}"
        ],
        "hyperbole": [
            "{action}到{extreme}",
            "{feeling}得{extreme}",
            "连{object}都{action}"
        ],
        "synesthesia": [
            "{sound}听起来{feeling}",
            "{color}看起来{feeling}",
            "{taste}尝起来{feeling}"
        ]
    }

    # 进阶押韵字典（更全面）
    EXTENDED_RHYME_DICTS = {
        "a": ["她", "花", "家", "吧", "呀", "啦", "下", "大", "发", "吧", "纱", "茶", "麻", "拿"],
        "ai": ["来", "爱", "在", "白", "开", "海", "彩", "猜", "才", "怀", "买", "卖", "派", "代"],
        "an": ["看", "站", "天", "晚", "难", "暖", "完", "满", "散", "转", "班", "半", "办", "般"],
        "ang": ["想", "光", "望", "样", "唱", "长", "方", "上", "亮", "香", "忙", "放", "唱", "量"],
        "ao": ["跳", "笑", "找", "好", "老", "跑", "叫", "要", "抱", "到", "草", "早", "高", "造"],
        "e": ["么", "得", "个", "热", "说", "可", "呢", "歌", "河", "客", "乐", "车", "色", "策"],
        "ei": ["给", "美", "飞", "水", "谁", "泪", "累", "类", "雷", "贵", "北", "备", "背", "杯"],
        "en": ["真", "深", "人", "本", "很", "门", "分", "身", "心", "新", "文", "温", "问", "闻"],
        "eng": ["声", "能", "风", "梦", "生", "等", "城", "灯", "星", "情", "声", "成", "城", "程"],
        "i": ["你", "里", "起", "去", "记", "气", "地", "事", "意", "世", "离", "低", "底", "第"],
        "ian": ["边", "眼", "年", "天", "前", "间", "点", "片", "面", "线", "电", "年", "连", "脸"],
        "iao": ["跳", "笑", "叫", "要", "飘", "摇", "照", "妙", "巧", "调", "小", "表", "秒", "鸟"],
        "ie": ["写", "谢", "夜", "街", "别", "些", "界", "姐", "借", "鞋", "也", "野", "业", "页"],
        "in": ["心", "今", "金", "近", "进", "尽", "紧", "劲", "禁", "锦", "音", "阴", "银", "因"],
        "ing": ["听", "情", "行", "明", "星", "命", "定", "影", "醒", "应", "轻", "清", "青", "经"],
        "ou": ["走", "手", "头", "有", "友", "后", "候", "久", "就", "旧", "楼", "留", "流", "柳"],
        "u": ["路", "住", "书", "出", "处", "苦", "服", "物", "助", "注", "不", "步", "部", "布"],
        "ua": ["花", "画", "话", "华", "化", "发", "打", "拿", "下", "怕", "瓜", "挂", "夸", "跨"],
        "uo": ["说", "多", "过", "火", "活", "落", "错", "作", "所", "破", "国", "果", "过", "或"]
    }

    # 扩展的意象库
    EXTENDED_IMAGERY = {
        "love": ["月光", "星光", "玫瑰", "咖啡杯", "明信片", "夕阳", "微风", "烟火", "情书", "礼物",
                "心跳", "拥抱", "牵手", "亲吻", "约会", "情书", "礼物", "约会", "心跳", "拥抱"],
        "sad": ["落叶", "冷雨", "旧照片", "空房间", "孤灯", "咖啡凉了", "未发送的消息", "远去的背影",
                "断了的弦", "枯萎的花", "孤独的夜", "逝去的爱", "破碎的梦", "离别的车站"],
        "happy": ["阳光", "花朵", "笑声", "奔跑", "拥抱", "彩虹", "星空", "舞蹈", "心跳", "快乐",
                "笑容", "温暖", "幸福", "希望", "未来", "梦想"],
        "nostalgia": ["旧时光", "老地方", "照片", "回忆", "从前", "小时候", "老街", "老歌", "旧物",
                     "童年", "故乡", "母校", "老朋友", "过去"],
        "courage": ["翅膀", "远方", "路", "光", "前行", "坚持", "勇气", "力量", "希望", "梦想",
                   "奋斗", "拼搏", "不屈", "坚强"],
        "dream": ["星空", "月光", "梦", "幻想", "未来", "希望", "远方", "飞翔", "云端", "彩虹",
                  "奇迹", "魔法", "童话"],
        "friendship": ["朋友", "兄弟", "姐妹", "友谊", "陪伴", "时光", "回忆", "共同", "一起", "支持"],
        "loneliness": ["孤独", "寂寞", "孤单", "一个人", "空荡", "安静", "夜", "月光", "影子"],
        "hope": ["光", "希望", "明天", "未来", "朝阳", "新生", "萌芽", "曙光", "梦想"]
    }

    # 进阶歌曲类型模板
    EXTENDED_SONG_TYPES = {
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
        },
        SongType.NOSTALGIA: {
            "Verse 1": "想起了旧时光",
            "Pre-Chorus": "那些画面历历在目",
            "Chorus": "怀念过去的美好",
            "Verse 2": "那些年的故事",
            "Bridge": "原来这就是成长"
        },
        SongType.COURAGE: {
            "Verse 1": "我曾经很迷茫",
            "Pre-Chorus": "但我知道不能放弃",
            "Chorus": "我要勇敢向前走",
            "Verse 2": "一路上的风景",
            "Bridge": "原来我可以的"
        },
        SongType.DREAM: {
            "Verse 1": "我有一个梦",
            "Pre-Chorus": "它在远方呼唤我",
            "Chorus": "我要去追寻我的梦",
            "Verse 2": "路上的艰辛",
            "Bridge": "梦想一定会实现"
        },
        SongType.FRIENDSHIP: {
            "Verse 1": "我们一起走过的路",
            "Pre-Chorus": "那些美好的回忆",
            "Chorus": "友谊万岁",
            "Verse 2": "未来我们还要一起走",
            "Bridge": "朋友是一辈子的"
        },
        SongType.LONELINESS: {
            "Verse 1": "这城市的孤独",
            "Pre-Chorus": "我一个人在角落",
            "Chorus": "孤独也是一种美",
            "Verse 2": "习惯了一个人",
            "Bridge": "我学会了与自己相处"
        },
        SongType.HOPE: {
            "Verse 1": "黑暗中的一点光",
            "Pre-Chorus": "我知道希望就在前方",
            "Chorus": "明天会更好",
            "Verse 2": "我看到了曙光",
            "Bridge": "希望照亮前方"
        }
    }

    # 音乐风格特定词汇
    STYLE_SPECIFIC_WORDS = {
        MusicStyle.CHINESE_FOLK: {
            "nouns": ["山水", "烟雨", "江南", "古道", "西风", "瘦马", "夕阳", "明月", "清风", "杨柳"],
            "verbs": ["吟", "叹", "醉", "梦", "忆", "思", "念", "望", "归", "候"],
            "adjectives": ["寂寞", "萧瑟", "苍茫", "悠然", "凄凉", "婉转", "清", "淡", "雅", "幽"]
        },
        MusicStyle.HIPHOP: {
            "nouns": ["节奏", "麦克风", "舞台", "街头", "梦想", "奋斗", "坚持", "态度", "真实", "自由"],
            "verbs": ["说唱", "摇摆", "舞动", "打破", "创造", "挑战", "证明", "坚持", "奋斗", "燃烧"],
            "adjectives": ["酷", "帅", "炫", "燃", "炸", "真实", "硬气", "有态度", "不一样"]
        },
        MusicStyle.BALLAD: {
            "nouns": ["心", "爱", "梦", "夜", "风", "雨", "月", "星", "泪", "笑"],
            "verbs": ["爱", "想", "等", "守", "盼", "望", "思", "念", "哭", "笑"],
            "adjectives": ["温柔", "甜蜜", "幸福", "痛苦", "悲伤", "快乐", "深情", "真挚"]
        },
        MusicStyle.ROCK: {
            "nouns": ["摇滚", "吉他", "鼓点", "呐喊", "热血", "青春", "梦想", "自由", "叛逆", "力量"],
            "verbs": ["燃烧", "释放", "呐喊", "冲破", "打破", "飞翔", "奔跑", "摇滚"],
            "adjectives": ["热血", "激情", "疯狂", "自由", "不羁", "强烈", "有力"]
        },
        MusicStyle.ELECTRONIC: {
            "nouns": ["节奏", "旋律", "节拍", "电音", "未来", "太空", "霓虹", "幻想", "梦境"],
            "verbs": ["舞动", "摇摆", "放飞", "沉醉", "漂浮", "穿越", "探索"],
            "adjectives": ["梦幻", "迷幻", "未来", "科技", "酷炫", "动感"]
        },
        MusicStyle.RNB: {
            "nouns": ["节奏", "蓝调", "灵魂", "感觉", "氛围", "夜", "浪漫"],
            "verbs": ["摇摆", "舞动", "沉醉", "感受", "拥抱", "亲吻"],
            "adjectives": ["性感", "浪漫", "温柔", "深情", "甜蜜"]
        }
    }

    # 进阶写作技巧
    ADVANCED_TECHNIQUES = {
        "repetition": "重复关键词或句子，增强记忆点",
        "anaphora": "句首重复，增强气势",
        "epiphora": "句尾重复，增强节奏感",
        "alliteration": "双声叠韵，增强音乐性",
        "assonance": "元音押韵，增强和谐感",
        "contrast": "对比手法，突出主题",
        "parallelism": "排比句式，增强气势",
        "climax": "层层递进，推向高潮",
        "anticlimax": "突降手法，制造反差",
        "irony": "反语，增加深度"
    }


class AdvancedLyricGenerator:
    def __init__(self, config: Optional[LyricConfig] = None):
        self.config = config or LyricConfig()
        self.templates = AdvancedLyricTemplates()

    def _generate_line_with_style(self, length: Optional[int] = None) -> str:
        length = length or self.config.line_length
        imagery = self.templates.EXTENDED_IMAGERY.get(self.config.theme, []) + \
                  self.templates.EXTENDED_IMAGERY.get(self.config.mood, [])
        
        if self.config.music_style and self.config.music_style in self.templates.STYLE_SPECIFIC_WORDS:
            style_words = self.templates.STYLE_SPECIFIC_WORDS[self.config.music_style]
            style_nouns = style_words.get("nouns", [])
            style_verbs = style_words.get("verbs", [])
            style_adjectives = style_words.get("adjectives", [])
            words = style_nouns + style_verbs + style_adjectives + imagery
        else:
            words = imagery + ["我", "你", "我们", "心", "爱", "梦", "想", "走", "看", "听", "说", "笑", "哭", "等"]
        
        return "".join(random.sample(words, min(length, len(words))))

    def _generate_rhyming_line(self, end_rhyme: str, length: Optional[int] = None) -> str:
        length = length or self.config.line_length
        rhyme_words = self.templates.EXTENDED_RHYME_DICTS.get(end_rhyme, [])
        if not rhyme_words:
            return self._generate_line_with_style(length)
        base = self._generate_line_with_style(length - 1)
        return base + random.choice(rhyme_words)

    def _get_rhyme_for_char(self, char: str) -> Optional[str]:
        for rhyme, words in self.templates.EXTENDED_RHYME_DICTS.items():
            if char in words:
                return rhyme
        return None

    def _generate_verse_with_scheme(self, scheme: RhymeScheme, lines: int = 4) -> List[str]:
        verse = []
        rhyme_map = {}
        current_rhyme = None
        
        for i in range(lines):
            if i == 0:
                line = self._generate_line_with_style()
                verse.append(line)
                if self.config.use_rhyme and scheme != RhymeScheme.FREE:
                    end_char = line[-1] if line else ""
                    current_rhyme = self._get_rhyme_for_char(end_char)
                    rhyme_map['A'] = current_rhyme
            else:
                if scheme == RhymeScheme.AABB:
                    if i % 2 == 1:
                        if 'A' in rhyme_map:
                            verse.append(self._generate_rhyming_line(rhyme_map['A']))
                        else:
                            verse.append(self._generate_line_with_style())
                    else:
                        line = self._generate_line_with_style()
                        verse.append(line)
                        if self.config.use_rhyme:
                            end_char = line[-1] if line else ""
                            rhyme_map['B'] = self._get_rhyme_for_char(end_char)
                elif scheme == RhymeScheme.ABAB:
                    if i % 2 == 1:
                        if 'A' in rhyme_map:
                            verse.append(self._generate_rhyming_line(rhyme_map['A']))
                        else:
                            verse.append(self._generate_line_with_style())
                    else:
                        if 'B' not in rhyme_map:
                            line = self._generate_line_with_style()
                            verse.append(line)
                            if self.config.use_rhyme:
                                end_char = line[-1] if line else ""
                                rhyme_map['B'] = self._get_rhyme_for_char(end_char)
                        else:
                            verse.append(self._generate_rhyming_line(rhyme_map['B']))
                elif scheme == RhymeScheme.ABCB:
                    if i % 2 == 1:
                        if 'B' in rhyme_map:
                            verse.append(self._generate_rhyming_line(rhyme_map['B']))
                        else:
                            line = self._generate_line_with_style()
                            verse.append(line)
                            if self.config.use_rhyme:
                                end_char = line[-1] if line else ""
                                rhyme_map['B'] = self._get_rhyme_for_char(end_char)
                    else:
                        verse.append(self._generate_line_with_style())
                else:
                    verse.append(self._generate_line_with_style())
        return verse

    def _generate_verse(self, verse_num: int = 1) -> List[str]:
        return self._generate_verse_with_scheme(
            self.config.rhyme_scheme, 
            self.config.verse_lines
        )

    def _generate_pre_chorus(self) -> List[str]:
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
        
        for i in range(self.config.pre_chorus_lines):
            if i == 0:
                pre_chorus.append(random.choice(hesitation_words))
            else:
                pre_chorus.append(self._generate_line_with_style())
        return pre_chorus

    def _generate_chorus(self) -> List[str]:
        chorus = []
        hooks = []
        
        if self.config.song_type and self.config.song_type in self.templates.EXTENDED_SONG_TYPES:
            chorus_desc = self.templates.EXTENDED_SONG_TYPES[self.config.song_type].get("Chorus", "")
            if chorus_desc:
                hooks = [chorus_desc]
        
        if not hooks:
            hooks = [
                f"{self.config.theme}是{random.choice(['一首歌', '一个梦', '一束光', '一场雨', '一阵风'])}",
                f"我{random.choice(['想你', '爱你', '等你', '忘不了你', '放不下'])}",
                f"就这样{random.choice(['吧', '了', '吧', '好吗', '行吗'])}"
            ]
        
        chorus.append(random.choice(hooks))
        for i in range(1, self.config.chorus_lines):
            chorus.append(self._generate_line_with_style())
        return chorus

    def _generate_bridge(self) -> List[str]:
        bridge = []
        realization_words = [
            "其实我早就该明白",
            "终于我想通了",
            "原来这就是成长",
            "我决定了",
            "从此以后",
            "现在我才懂",
            "原来如此",
            "这就是答案"
        ]
        
        bridge.append(f"{random.choice(realization_words)}{self._generate_line_with_style(5)}")
        for i in range(1, self.config.bridge_lines):
            bridge.append(self._generate_line_with_style())
        return bridge

    def generate(self, config: Optional[LyricConfig] = None) -> Dict[str, List[str]]:
        if config:
            self.config = config
        
        structure_map = {
            SongStructure.VERSE_CHORUS: ["Verse 1", "Chorus", "Verse 2", "Chorus", "Chorus"],
            SongStructure.ABABCB: ["Verse 1", "Chorus", "Verse 2", "Chorus", "Bridge", "Chorus"],
            SongStructure.AABA: ["Verse 1", "Verse 2", "Bridge", "Verse 1"],
            SongStructure.FULL_STRUCTURE: ["Verse 1", "Pre-Chorus", "Chorus", "Verse 2", "Pre-Chorus", "Chorus", "Bridge", "Chorus"]
        }
        
        structure = structure_map.get(self.config.song_structure, structure_map[SongStructure.FULL_STRUCTURE])
        
        song = {}
        
        for part in structure:
            if "Verse 1" in part and "Verse 1" not in song:
                song["Verse 1"] = self._generate_verse(1)
            elif "Verse 2" in part and "Verse 2" not in song:
                song["Verse 2"] = self._generate_verse(2)
            elif "Verse" in part:
                verse_num = len([k for k in song.keys() if "Verse" in k]) + 1
                song[f"Verse {verse_num}"] = self._generate_verse(verse_num)
            elif "Pre-Chorus" in part and "Pre-Chorus" not in song:
                song["Pre-Chorus"] = self._generate_pre_chorus()
            elif "Chorus" in part and "Chorus" not in song:
                song["Chorus"] = self._generate_chorus()
            elif "Bridge" in part and "Bridge" not in song:
                song["Bridge"] = self._generate_bridge()
        
        return song

    def format_song(self, song: Dict[str, List[str]]) -> str:
        lines = []
        for section, content in song.items():
            lines.append(f"[{section}]")
            lines.extend(content)
            lines.append("")
        return "\n".join(lines)


class LyricsPolisher:
    """歌词润色器，提供歌词优化功能"""
    
    @staticmethod
    def polish_line(line: str, style: Optional[MusicStyle] = None) -> str:
        """润色单行歌词"""
        if len(line) < 3:
            return line
        
        # 简单的润色规则
        polished = line
        
        # 替换重复字
        polished = re.sub(r'(.)\1+', r'\1', polished)
        
        # 优化语句流畅度
        if len(polished) > 10:
            # 对于过长的句子，适当简化
            mid = len(polished) // 2
            polished = polished[:mid] + polished[mid+1:]
        
        return polished
    
    @staticmethod
    def polish_song(song: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """润色整首歌"""
        polished_song = {}
        for section, lines in song.items():
            polished_lines = [LyricsPolisher.polish_line(line) for line in lines]
            polished_song[section] = polished_lines
        return polished_song


class ThemeExplorer:
    """灵感主题探索器"""
    
    @staticmethod
    def explore_themes(keyword: str = "") -> List[Dict[str, str]]:
        """探索相关的歌词主题"""
        themes = [
            {"theme": "爱情", "mood": "甜蜜", "keywords": "爱,喜欢,你,我,在一起"},
            {"theme": "失恋", "mood": "悲伤", "keywords": "分手,离开,再见,忘记,回忆"},
            {"theme": "梦想", "mood": "励志", "keywords": "梦,想,未来,远方,奋斗"},
            {"theme": "友情", "mood": "温暖", "keywords": "朋友,兄弟,姐妹,一起,陪伴"},
            {"theme": "家乡", "mood": "怀旧", "keywords": "故乡,回家,童年,老街,老屋"},
            {"theme": "孤独", "mood": "寂寞", "keywords": "一个人,孤独,寂寞,夜,安静"},
            {"theme": "希望", "mood": "积极", "keywords": "希望,明天,未来,光,朝阳"},
            {"theme": "成长", "mood": "深刻", "keywords": "成长,改变,明白,懂得,学习"}
        ]
        
        if keyword:
            filtered = [t for t in themes if keyword.lower() in t["keywords"].lower() or keyword.lower() in t["theme"].lower()]
            return filtered if filtered else themes
        return themes
    
    @staticmethod
    def get_related_words(theme: str, count: int = 10) -> List[str]:
        """获取与主题相关的词汇"""
        word_map = {
            "爱情": ["爱", "情", "心", "你", "我", "在一起", "牵手", "拥抱", "吻", "幸福"],
            "失恋": ["分手", "离开", "再见", "忘记", "回忆", "痛", "泪", "伤", "别", "离"],
            "梦想": ["梦", "想", "飞", "远", "未来", "希望", "追", "求", "拼", "搏"],
            "友情": ["朋友", "兄弟", "姐妹", "一起", "陪伴", "谊", "情", "义", "共", "同"],
            "家乡": ["故乡", "回家", "童年", "老街", "老屋", "乡", "家", "旧", "忆", "念"]
        }
        return word_map.get(theme, ["爱", "情", "心", "梦", "想", "你", "我"])[:count]


class AdvancedLyricsAssistant:
    """进阶版歌词创作助手"""
    
    def __init__(self):
        self.generator = AdvancedLyricGenerator()
        self.polisher = LyricsPolisher()
        self.theme_explorer = ThemeExplorer()
    
    def generate_song_by_type(self, song_type: SongType, style: Optional[MusicStyle] = None) -> str:
        """根据歌曲类型生成歌词"""
        config = LyricConfig(
            song_type=song_type,
            music_style=style,
            theme=song_type.value.lower(),
            mood=self._get_mood_for_type(song_type)
        )
        song = self.generator.generate(config)
        polished = self.polisher.polish_song(song)
        return self.generator.format_song(polished)
    
    def _get_mood_for_type(self, song_type: SongType) -> str:
        mood_map = {
            SongType.CONFESSION: "happy",
            SongType.BREAKUP: "sad",
            SongType.NOSTALGIA: "nostalgia",
            SongType.COURAGE: "courage",
            SongType.DREAM: "happy",
            SongType.FRIENDSHIP: "happy",
            SongType.LONELINESS: "sad",
            SongType.HOPE: "happy"
        }
        return mood_map.get(song_type, "love")
    
    def get_advanced_tips(self) -> List[str]:
        """获取进阶创作技巧"""
        tips = []
        for name, desc in AdvancedLyricTemplates.ADVANCED_TECHNIQUES.items():
            tips.append(f"{name}: {desc}")
        return tips
    
    def get_style_guide(self, style: MusicStyle) -> Dict[str, List[str]]:
        """获取特定风格的创作指南"""
        if style in AdvancedLyricTemplates.STYLE_SPECIFIC_WORDS:
            return AdvancedLyricTemplates.STYLE_SPECIFIC_WORDS[style]
        return {}
