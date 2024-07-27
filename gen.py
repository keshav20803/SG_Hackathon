import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


text= """
        Based on the following diary entry, provide suggestions on how the person can improve their 
        mental health. The suggestions should be practical, empathetic, and supportive. Consider areas such
        as daily routine, self-care, social interactions, and seeking professional help.
      """
text_diary="""
Dear Diary,

I felt a good but down and couldn't quite pinpoint why. Work was fine, but I couldn't shake off this lingering sense of melancholy. I tried to focus on my tasks, but my mind kept drifting to a conversation I had with a friend recently. They seemed distant, and I'm worried I might have said something wrong.

During lunch, I went for a walk to clear my thoughts. The weather was nice, but even the sunshine didn't lift my spirits much. I saw a few people out with their friends, and it reminded me of how I haven't been as social lately. It feels like I've been drifting apart from some of my close friends, and that thought makes me sad.

When I got home, I made a simple dinner and watched a movie, hoping to distract myself. It helped a little, but I still feel a bit lonely. I know these feelings will pass, but right now, it's hard not to dwell on them.

I'll try to get a good night's sleep and see if that helps. Maybe tomorrow will be a better day.

Goodnight, Diary.
"""

question=text+text_diary
print(get_gemini_response(question))