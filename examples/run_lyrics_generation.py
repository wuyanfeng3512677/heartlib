#!/usr/bin/env python3
"""
歌词生成示例脚本
使用 HeartMuLa 的歌词创作辅助模块
"""

import argparse
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from heartlib.pipelines import LyricsWritingAssistant, LyricConfig, SongStructure, OpeningTechnique


def main():
    parser = argparse.ArgumentParser(description="歌词创作辅助工具")
    parser.add_argument("--theme", type=str, default="love", help="歌词主题 (love, sad, happy, nostalgia, courage)")
    parser.add_argument("--mood", type=str, default="sad", help="情绪 (sad, happy, love, nostalgia, courage)")
    parser.add_argument("--tips", action="store_true", help="显示创作技巧")
    parser.add_argument("--brainstorm", action="store_true", help="灵感主题建议")
    parser.add_argument("--save", type=str, help="保存歌词到文件")
    parser.add_argument("--structure", type=str, default="ababcb", 
                        choices=["verse_chorus", "ababcb", "aaba"], help="歌曲结构")
    parser.add_argument("--opening", type=str, default=None,
                        choices=["scene", "action", "sound", "time", "question", 
                                "contrast", "object", "location", "weather", "line"],
                        help="开篇技巧")
    
    args = parser.parse_args()
    
    assistant = LyricsWritingAssistant()
    
    if args.brainstorm:
        print("💡 灵感主题建议：")
        themes = assistant.brainstorm_themes()
        for i, theme in enumerate(themes, 1):
            print(f"  {i}. {theme}")
        return
    
    if args.tips:
        print("📝 歌词创作技巧：")
        tips = assistant.get_tips()
        for i, tip in enumerate(tips, 1):
            print(f"  {i}. {tip}")
        return
    
    print("🎵 开始生成歌词...\n")
    
    structure_map = {
        "verse_chorus": SongStructure.VERSE_CHORUS,
        "ababcb": SongStructure.ABABCB,
        "aaba": SongStructure.AABA
    }
    
    opening_map = {
        "scene": OpeningTechnique.SCENE,
        "action": OpeningTechnique.ACTION,
        "sound": OpeningTechnique.SOUND,
        "time": OpeningTechnique.TIME,
        "question": OpeningTechnique.QUESTION,
        "contrast": OpeningTechnique.CONTRAST,
        "object": OpeningTechnique.OBJECT,
        "location": OpeningTechnique.LOCATION,
        "weather": OpeningTechnique.WEATHER,
        "line": OpeningTechnique.LINE
    }
    
    config = LyricConfig(
        theme=args.theme,
        mood=args.mood,
        song_structure=structure_map.get(args.structure, SongStructure.ABABCB),
        opening_technique=opening_map.get(args.opening)
    )
    
    song = assistant.generator.generate(config)
    formatted = assistant.generator.format_song(song)
    
    print(formatted)
    
    tips = assistant.get_tips()
    print("\n" + "="*50)
    print("💡 歌词创作技巧建议：")
    for tip in tips[:5]:
        print(f"  • {tip}")
    
    if args.save:
        with open(args.save, 'w', encoding='utf-8') as f:
            f.write(formatted)
        print(f"\n✅ 歌词已保存到: {args.save}")


if __name__ == "__main__":
    main()
