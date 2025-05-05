
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# মূল ভিডিও লোড করো (assets ফোল্ডারে রাখতে হবে)
video = VideoFileClip("assets/birthday.mp4")

# টেক্সট তৈরি করো
text = TextClip("Happy Birthday, Rafi!", fontsize=70, color='white', font="Amiri-Bold")
text = text.set_position('center').set_duration(video.duration)

# টেক্সট ও ভিডিও একসাথে
final = CompositeVideoClip([video, text])

# আউটপুট ভিডিও তৈরি করো
final.write_videofile("output/output.mp4", fps=24)
