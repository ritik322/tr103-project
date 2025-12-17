import asyncio
import edge_tts
import pygame
import os

VOICE = "en-US-AriaNeural"  
BUFFER_FILE = "ai_voice.mp3"

async def _generate_audio(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(BUFFER_FILE)

def say(text):
    print(f"AI: {text}") 
    try:
        asyncio.run(_generate_audio(text))
    except Exception as e:
        print(f"Error generating voice: {e}")
        return

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(BUFFER_FILE)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload() 
        pygame.mixer.quit()        
        
        if os.path.exists(BUFFER_FILE):
            os.remove(BUFFER_FILE)
            
    except Exception as e:
        print(f"Error playing audio: {e}")

if __name__ == "__main__":
    say("Hello sir, I have updated my voice module. How do I sound?")