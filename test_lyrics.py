#!/usr/bin/env python3
"""
直接测试歌词生成模块
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from heartlib.pipelines.lyrics_generation import (
    LyricConfig, LyricGenerator, LyricsWritingAssistant, 
    SongStructure, OpeningTechnique
)

print("=" * 60)
print("🎵 HeartMuLa 歌词创作辅助模块测试")
print("=" * 60)

print("\n1. 测试 LyricsWritingAssistant - 灵感主题建议")
print("-" * 40)
assistant = LyricsWritingAssistant()
themes = assistant.brainstorm_themes()
for i, theme in enumerate(themes[:5], 1):
    print(f"  {i}. {theme}")

print("\n2. 测试 LyricsWritingAssistant - 创作技巧")
print("-" * 40)
tips = assistant.get_tips()
for i, tip in enumerate(tips[:5], 1):
    print(f"  {i}. {tip}")

print("\n3. 测试 LyricGenerator - 生成歌词")
print("-" * 40)
config = LyricConfig(
    theme="love",
    mood="sad",
    song_structure=SongStructure.ABABCB,
    opening_technique=OpeningTechnique.SCENE
)
generator = LyricGenerator(config)
song = generator.generate()
formatted = generator.format_song(song)
print(formatted)

print("\n4. 保存测试歌词")
print("-" * 40)
test_output = "/workspace/assets/test_lyrics.txt"
with open(test_output, 'w', encoding='utf-8') as f:
    f.write(formatted)
print(f"✅ 歌词已保存到: {test_output}")

print("\n" + "=" * 60)
print("🎉 所有测试完成！")
print("=" * 60)
