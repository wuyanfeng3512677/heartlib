#!/usr/bin/env python3
"""
HeartMuLa 专业进阶歌词创作功能演示
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.heartlib.pipelines.lyrics_pro import (
    ProfessionalLyricAssistant,
    LyricQualityEvaluator,
    RhymeManager,
    EmotionCurve,
    HookType,
    NarrativePerspective,
    EmotionLevel
)


def print_separator(title):
    print("\n" + "=" * 80)
    print(f"  {title}".center(80))
    print("=" * 80)


def test_emotion_curve_design():
    """测试情感曲线设计"""
    print_separator("🎭 情感曲线设计")
    
    assistant = ProfessionalLyricAssistant()
    
    for song_type in ["love", "sad", "courage", "dream"]:
        curve = assistant.design_emotion_curve(song_type)
        print(f"\n📀 {song_type.upper()} 歌曲情感曲线:")
        
        sections = [
            ("Intro", curve.intro_level),
            ("Verse 1", curve.verse1_level),
            ("Pre-Chorus", curve.pre_chorus_level),
            ("Chorus", curve.chorus_level),
            ("Verse 2", curve.verse2_level),
            ("Bridge", curve.bridge_level),
            ("Final Chorus", curve.final_chorus_level)
        ]
        
        for section, level in sections:
            bar = "█" * level.value + "░" * (5 - level.value)
            print(f"  {section:15} [{bar}] {level.name}")


def test_hook_design():
    """测试Hook设计"""
    print_separator("🎣 Hook记忆点设计")
    
    assistant = ProfessionalLyricAssistant()
    
    print("\n情感Hook示例:")
    print(f"  {assistant.create_professional_hook(HookType.EMOTIONAL, '梦想')}")
    
    print("\n重复Hook示例:")
    print(f"  {assistant.create_professional_hook(HookType.REPETITIVE, '爱')}")
    
    print("\n独特视角Hook示例:")
    print(f"  {assistant.create_professional_hook(HookType.UNIQUE, '')}")
    
    print("\n疑问Hook示例:")
    print(f"  {assistant.create_professional_hook(HookType.QUESTION, '离别')}")


def test_inspiration_generator():
    """测试灵感火花生成器"""
    print_separator("💡 灵感火花生成")
    
    assistant = ProfessionalLyricAssistant()
    
    print("\n生成5组灵感火花:\n")
    
    for i in range(5):
        inspiration = assistant.get_inspiration()
        print(f"第{i+1}组灵感:")
        print(f"  情绪组合: {inspiration['emotion_combination']['emotion']}{inspiration['emotion_combination']['subject']}")
        print(f"  场景提示: {inspiration['scene_prompt']}")
        print(f"  比喻句: {inspiration['metaphor']}")
        print(f"  Hook: {inspiration['hook']}")
        print()


def test_quality_evaluation():
    """测试歌词质量评估"""
    print_separator("📊 歌词质量评估")
    
    # 示例歌词
    sample_lyrics = {
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
    
    evaluator = LyricQualityEvaluator()
    evaluation = evaluator.evaluate_song(sample_lyrics)
    
    print("\n📝 示例歌词:")
    for section, lines in sample_lyrics.items():
        print(f"\n  [{section}]")
        for line in lines:
            print(f"    {line}")
    
    print("\n📈 质量评估报告:")
    print(f"\n  综合评分: {evaluation['overall_score']:.2f}/1.00")
    print(f"\n  押韵质量: {evaluation['rhyme']['score']:.2f} - {evaluation['rhyme']['detail']}")
    print(f"  意象密度: {evaluation['imagery']['score']:.2f} - {evaluation['imagery']['detail']}")
    print(f"  节奏感: {evaluation['rhythm']['score']:.2f} - {evaluation['rhythm']['detail']}")
    
    print("\n💡 改进建议:")
    for suggestion in evaluation['suggestions']:
        print(f"  {suggestion}")


def test_rhyme_management():
    """测试韵脚管理"""
    print_separator("🎵 智能韵脚管理")
    
    manager = RhymeManager()
    
    print("\n📚 韵脚数据库包含18种韵脚组")
    
    print("\n根据情绪匹配韵脚:")
    for emotion in ["happy", "sad", "love", "courage", "nostalgia"]:
        rhyme = manager.get_rhyme_for_emotion(emotion)
        words = manager.get_rhyme_words(rhyme, 5)
        print(f"\n  {emotion}情绪 → 韵脚「{rhyme}」")
        print(f"    示例词: {', '.join(words)}")
    
    print("\n\n🔍 韵脚匹配测试:")
    test_words = ["爱", "在", "看", "来", "心"]
    for word in test_words:
        rhyme = manager.match_rhyme(word)
        print(f"  「{word}」 → 韵脚「{rhyme}」")


def test_section_guidance():
    """测试段落写作指导"""
    print_separator("📖 段落写作指导")
    
    assistant = ProfessionalLyricAssistant()
    
    for section in ["Verse", "Pre-Chorus", "Chorus", "Bridge"]:
        print(f"\n🎯 {section}写作技巧:")
        tips = assistant.generate_writing_tips(section)
        for tip in tips:
            print(f"  {tip}")
        
        guidance = assistant.get_verse_guidance(1 if section == "Verse" else 0)
        if section == "Verse":
            print(f"\n  递进设计: {guidance['guidance']}")


def test_narrative_perspective():
    """测试叙事视角"""
    print_separator("👁️ 叙事视角示例")
    
    perspectives = {
        NarrativePerspective.FIRST_PERSON: "我看见了你的笑容",
        NarrativePerspective.SECOND_PERSON: "你看见了自己的影子",
        NarrativePerspective.THIRD_PERSON: "他站在街角等待",
        NarrativePerspective.OMNISCIENT: "这座城市里，每个人都有自己的故事"
    }
    
    print("\n不同叙事视角的表达:")
    for perspective, example in perspectives.items():
        print(f"\n  {perspective.value}:")
        print(f"    示例: {example}")


def main():
    print_separator("🎵 HeartMuLa 专业进阶歌词创作功能演示")
    
    print("\n本演示包含以下专业功能:")
    print("  1. 情感曲线设计")
    print("  2. Hook记忆点设计")
    print("  3. 灵感火花生成")
    print("  4. 歌词质量评估")
    print("  5. 智能韵脚管理")
    print("  6. 段落写作指导")
    print("  7. 叙事视角切换")
    
    # 运行所有测试
    test_emotion_curve_design()
    test_hook_design()
    test_inspiration_generator()
    test_quality_evaluation()
    test_rhyme_management()
    test_section_guidance()
    test_narrative_perspective()
    
    print_separator("✨ 所有专业功能演示完成！")
    print("\n🎯 使用建议:")
    print("  1. 使用灵感火花生成器获取创作起点")
    print("  2. 根据情感曲线设计整体情绪走向")
    print("  3. 参考Hook设计打造记忆点")
    print("  4. 生成歌词后使用质量评估系统检查")
    print("  5. 根据建议进行优化")
    print("\n🚀 祝创作愉快！")


if __name__ == "__main__":
    main()
