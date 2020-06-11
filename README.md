# EmbedLyricToAudio
Embed lyric to audio files using [mutagen](https://github.com/quodlibet/mutagen).


# Usage

Put lyric file and audio file in a folder (support nested folders) and make sure they have the same main name.

```
PS D:\JX3_Songs> python .\EmbedLyricToAudio.py
[Not supported file] ./EmbedLyricToAudio.py
[OK] .\Misc/Ace组合 - 听说师父在东海.flac
[Not supported file] .\Misc/Ace组合 - 听说师父在东海.lrc.nonkaraoke
[OK] .\Misc/Assen捷&橙翼 - 当归.mp3
[OK] .\Misc/IRiS七叶&曾小Cee - 倾城曲七秀.mp3
[OK] .\Misc/JX3暗箱组合 - 孤独行刑者 (刺客版 和声伴奏).flac
[OK] .\Misc/JX3暗箱组合 - 孤独行刑者 (刺客版).flac
[OK] .\Misc/NL不分 阿睿凌霓剑裳 - 出鞘——浩气盟战歌【纯歌版】.mp3
[OK] .\Misc/NL不分 阿睿凌霓剑裳 - 当战——剑网3竞技大师赛·官方宣传曲.flac
[OK] .\Misc/NL不分&阿睿凌霓剑裳&五音Jw&潮汐-tide&黄诗扶 - 惟侠不败.flac
[Not supported file] .\Misc/NL不分&阿睿凌霓剑裳&五音Jw&潮汐-tide&黄诗扶 - 惟侠不败.lrc.nonkaraoke
[OK] .\Misc/NL不分&阿睿凌霓剑裳&忘月幽 - 何曾惧.mp3
[OK] .\Misc/Vk&五音Jw&Aki阿杰 - 何曾惧.flac
[Not supported file] .\Misc/Vk&五音Jw&Aki阿杰 - 何曾惧.lrc.nonkaraoke
[OK] .\Misc/剑网3&JX3暗箱组合 - 少年狂想录.mp3
...
[OK] .\剑网3·侠肝义胆沈剑心/小爱的妈&雨洛Huge - 在下，沈剑心！.mp3
[No lyric found] .\剑网3·侠肝义胆沈剑心/西山居音频中心 - 一触即发.flac
[No lyric found] .\剑网3·侠肝义胆沈剑心/西山居音频中心 - 全村的希望.flac
[No lyric found] .\剑网3·侠肝义胆沈剑心/西山居音频中心 - 剑心很忙.flac
[No lyric found] .\剑网3·侠肝义胆沈剑心/西山居音频中心 - 在下，沈剑心！ (壮阔变奏).flac
[No lyric found] .\剑网3·侠肝义胆沈剑心/西山居音频中心 - 在下，沈剑心！ (柔情变奏).flac
[No lyric found] .\剑网3·侠肝义胆沈剑心/西山居音频中心 - 在下，沈剑心！ (燃版变奏).flac
...
```
