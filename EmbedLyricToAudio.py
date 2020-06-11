import mutagen
import os

SUPPORTED_FILE_EXTENSIONS = [".MP3", ".AAC", ".APE", ".FLAC", ".OGG", ".WAV"]
LYRIC_EXTENSION = ".LRC"
FORCE_UPDATE_IGNORE_LAST_MODIFY = True

for currentDir, subDirs, files in os.walk("."):
    for file in files:
        audioFullPath = currentDir + "/" + file
        audioMainName, audioExt = os.path.splitext(file)
        audioExt = audioExt.upper()
        # is it not lyric?
        if audioExt != LYRIC_EXTENSION:
            # is it supported?
            if audioExt in SUPPORTED_FILE_EXTENSIONS:
                lyricFullPath = currentDir + "/" + audioMainName + LYRIC_EXTENSION
                # is coresponding lyric exists?
                if os.path.exists(lyricFullPath):
                    # is lyric newer than itself?
                    audioLastModify = os.path.getmtime(audioFullPath)
                    lyricLastModify = os.path.getmtime(lyricFullPath)
                    if FORCE_UPDATE_IGNORE_LAST_MODIFY or lyricLastModify > audioLastModify:
                        try:
                            fileObj = mutagen.File(audioFullPath)
                            lyricContent = open(lyricFullPath, "r", encoding="utf-8").read()
                            # is ID3?
                            if isinstance(fileObj.tags, mutagen.id3.ID3):
                                # remove any existing lyric tags
                                fileObj.tags.delall("USLT")
                                fileObj.tags.delall("TXXX:LYRICS")
                                fileObj.tags["TXXX:LYRICS"] = mutagen.id3.TXXX(encoding=3, desc="LYRICS", text=lyricContent)
                            else:
                                fileObj.tags["LYRICS"] = lyricContent
                            fileObj.save()
                            print("[OK] " + audioFullPath)
                        except Exception as ex:
                            print("[Error] " + audioFullPath)
                            print(ex)
                    else:
                        print("[Lyric not new] " + audioFullPath)
                else:
                    print("[No lyric found] " + audioFullPath)
            else:
                print("[Not supported file] " + audioFullPath)
