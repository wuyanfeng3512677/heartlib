#!/usr/bin/env python3
"""
进阶版歌词创作辅助工具 - 完整功能演示
包含所有新增的高级功能
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import random
from enum import Enum


# 重新定义所需的类，避免导入问题
class SongStructure(Enum):
    VERSE_CHORUS = "verse_chorus"
    ABABCB = "ababcb"
    AABA = "aaba"
    FULL_STRUCTURE = "full_structure"


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
    EXTENDED_IMAGERY = {
        "love": ["月光", "星光", "玫瑰", "咖啡杯", "明信片", "夕阳", "微风", "烟火"],
        "sad": ["落叶", "冷雨", "旧照片", "空房间", "孤灯", "咖啡凉了", "未发送的消息"],
        "happy": ["阳光", "花朵", "笑声", "奔跑", "拥抱", "彩虹", "星空", "舞蹈"],
        "nostalgia": ["旧时光", "老地方", "照片", "回忆", "从前", "小时候", "老街"],
        "courage": ["翅膀", "远方", "路", "光", "前行", "坚持", "勇气", "力量"],
        "dream": ["星空", "月光", "梦", "幻想", "未来", "希望", "远方", "飞翔"],
        "friendship": ["朋友", "兄弟", "姐妹", "友谊", "陪伴", "时光", "回忆", "共同"],
        "loneliness": ["孤独", "寂寞", "孤单", "一个人", "空荡", "安静", "夜", "月光"],
        "hope": ["光", "希望", "明天", "未来", "朝阳", "新生", "萌芽", "曙光"]
    }
    
    STYLE_SPECIFIC_WORDS = {
        MusicStyle.CHINESE_FOLK: {
            "nouns": ["山水", "烟雨", "江南", "古道", "西风", "瘦马", "夕阳", "明月"],
            "verbs": ["吟", "叹", "醉", "梦", "忆", "思", "念", "望"],
            "adjectives": ["寂寞", "萧瑟", "苍茫", "悠然", "凄凉", "婉转"]
        },
        MusicStyle.HIPHOP: {
            "nouns": ["节奏", "麦克风", "舞台", "街头", "梦想", "奋斗", "坚持", "态度"],
            "verbs": ["说唱", "摇摆", "舞动", "打破", "创造", "挑战", "证明", "燃烧"],
            "adjectives": ["酷", "帅", "炫", "燃", "炸", "真实", "硬气", "有态度"]
        },
        MusicStyle.BALLAD: {
            "nouns": ["心", "爱", "梦", "夜", "风", "雨", "月", "星", "泪", "笑"],
            "verbs": ["爱", "想", "等", "守", "盼", "望", "思", "念", "哭", "笑"],
            "adjectives": ["温柔", "甜蜜", "幸福", "痛苦", "悲伤", "快乐", "深情"]
        },
        MusicStyle.ROCK: {
            "nouns": ["摇滚", "吉他", "鼓点", "呐喊", "热血", "青春", "梦想", "自由"],
            "verbs": ["燃烧", "释放", "呐喊", "冲破", "打破", "飞翔", "奔跑"],
            "adjectives": ["热血", "激情", "疯狂", "自由", "不羁", "强烈", "有力"]
        },
        MusicStyle.ELECTRONIC: {
            "nouns": ["节奏", "旋律", "节拍", "电音", "未来", "太空", "霓虹", "幻想"],
            "verbs": ["舞动", "摇摆", "放飞", "沉醉", "漂浮", "穿越", "探索"],
            "adjectives": ["梦幻", "迷幻", "未来", "科技", "酷炫", "动感"]
        },
        MusicStyle.RNB: {
            "nouns": ["节奏", "蓝调", "灵魂", "感觉", "氛围", "夜", "浪漫"],
            "verbs": ["摇摆", "舞动", "沉醉", "感受", "拥抱", "亲吻"],
            "adjectives": ["性感", "浪漫", "温柔", "深情", "甜蜜"]
        }
    }
    
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
    
    def _generate_verse(self, verse_num: int = 1) -> List[str]:
        verse = []
        for i in range(self.config.verse_lines):
            verse.append(self._generate_line_with_style())
        return verse
    
    def _generate_pre_chorus(self) -> List[str]:
        pre_chorus = []
        hesitation_words = [
            "我想说却又不敢",
            "心跳越来越快",
            "话到嘴边又咽下",
            "我在等一个回答",
            "我还在犹豫什么",
            "终于决定要开口"
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
                f"{self.config.theme}是{random.choice(['一首歌', '一个梦', '一束光'])}",
                f"我{random.choice(['想你', '爱你', '等你', '忘不了你'])}"
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
            "从此以后"
        ]
        bridge.append(f"{random.choice(realization_words)}{self._generate_line_with_style(5)}")
        for i in range(1, self.config.bridge_lines):
            bridge.append(self._generate_line_with_style())
        return bridge
    
    def generate(self, config: Optional[LyricConfig] = None) -> Dict[str, List[str]]:
        if config:
            self.config = config
        
        structure = ["Verse 1", "Pre-Chorus", "Chorus", "Verse 2", "Pre-Chorus", "Chorus", "Bridge", "Chorus"]
        song = {}
        
        for part in structure:
            if "Verse 1" in part and "Verse 1" not in song:
                song["Verse 1"] = self._generate_verse(1)
            elif "Verse 2" in part and "Verse 2" not in song:
                song["Verse 2"] = self._generate_verse(2)
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


class ThemeExplorer:
    @staticmethod
    def explore_themes(keyword: str = "") -> List[Dict[str, str]]:
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


class AdvancedLyricsAssistant:
    def __init__(self):
        self.generator = AdvancedLyricGenerator()
        self.theme_explorer = ThemeExplorer()
    
    def generate_song_by_type(self, song_type: SongType, style: Optional[MusicStyle] = None) -> str:
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
        
        config = LyricConfig(
            song_type=song_type,
            music_style=style,
            theme=song_type.value.lower(),
            mood=mood_map.get(song_type, "love")
        )
        song = self.generator.generate(config)
        return self.generator.format_song(song)
    
    def get_advanced_tips(self) -> List[str]:
        tips = []
        for name, desc in AdvancedLyricTemplates.ADVANCED_TECHNIQUES.items():
            tips.append(f"{name}: {desc}")
        return tips
    
    def get_style_guide(self, style: MusicStyle) -> Dict[str, List[str]]:
        if style in AdvancedLyricTemplates.STYLE_SPECIFIC_WORDS:
            return AdvancedLyricTemplates.STYLE_SPECIFIC_WORDS[style]
        return {}


def print_separator(title):
    print("\n" + "=" * 70)
    print(f"  {title}".center(70))
    print("=" * 70)


def main():
    print_separator("🎵 HeartMuLa 进阶版歌词创作辅助工具 🎵")
    
    assistant = AdvancedLyricsAssistant()
    
    # 1. 展示进阶写作技巧
    print_separator("📚 进阶写作技巧")
    tips = assistant.get_advanced_tips()
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")
    
    # 2. 展示灵感主题探索
    print_separator("💡 灵感主题探索")
    themes = ThemeExplorer.explore_themes()
    for i, theme_info in enumerate(themes, 1):
        print(f"{i}. 【{theme_info['theme']}】({theme_info['mood']}) - 关键词: {theme_info['keywords']}")
    
    # 3. 展示音乐风格选项
    print_separator("🎶 音乐风格选项")
    styles = list(MusicStyle)
    style_names = {
        MusicStyle.CHINESE_FOLK: "中国风",
        MusicStyle.HIPHOP: "嘻哈/说唱",
        MusicStyle.BALLAD: "抒情民谣",
        MusicStyle.ROCK: "摇滚",
        MusicStyle.ELECTRONIC: "电子音乐",
        MusicStyle.RNB: "R&B"
    }
    for i, style in enumerate(styles, 1):
        print(f"{i}. {style_names[style]} ({style.value})")
    
    # 4. 展示中国风歌曲示例
    print_separator("🎎 示例：中国风歌曲 (怀旧主题)")
    chinese_folk = assistant.generate_song_by_type(SongType.NOSTALGIA, MusicStyle.CHINESE_FOLK)
    print(chinese_folk)
    
    # 5. 展示嘻哈风格歌曲示例
    print_separator("🎤 示例：嘻哈/说唱歌曲 (梦想主题)")
    hiphop = assistant.generate_song_by_type(SongType.DREAM, MusicStyle.HIPHOP)
    print(hiphop)
    
    # 6. 展示抒情民谣歌曲示例
    print_separator("🎸 示例：抒情民谣歌曲 (告白主题)")
    ballad = assistant.generate_song_by_type(SongType.CONFESSION, MusicStyle.BALLAD)
    print(ballad)
    
    # 7. 展示摇滚风格歌曲示例
    print_separator("🎸 示例：摇滚风格歌曲 (勇气主题)")
    rock = assistant.generate_song_by_type(SongType.COURAGE, MusicStyle.ROCK)
    print(rock)
    
    # 8. 歌曲类型总结
    print_separator("📋 可用歌曲类型总结")
    song_types = list(SongType)
    type_names = {
        SongType.CONFESSION: "告白/心动",
        SongType.BREAKUP: "分手/释怀",
        SongType.NOSTALGIA: "怀旧/回忆",
        SongType.COURAGE: "勇气/励志",
        SongType.DREAM: "梦想/追逐",
        SongType.FRIENDSHIP: "友情/陪伴",
        SongType.LONELINESS: "孤独/寂寞",
        SongType.HOPE: "希望/未来"
    }
    for i, song_type in enumerate(song_types, 1):
        print(f"{i}. {type_names[song_type]} ({song_type.value})")
    
    print_separator("✨ 所有功能演示完成！")
    print("\n💡 使用提示:")
    print("1. 从灵感主题中找到你想要的主题")
    print("2. 选择合适的音乐风格")
    print("3. 调用 generate_song_by_type() 生成完整歌词")
    print("4. 根据进阶写作技巧进行润色和优化")
    print("\n🚀 尽情创作吧！")


if __name__ == "__main__":
    main()
