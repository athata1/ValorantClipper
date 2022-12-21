from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip;
import sys;

args = sys.argv;
print(len(args));
ffmpeg_extract_subclip(str(args[1]),int(args[2]), int(args[3]), targetname= str(args[4]))
