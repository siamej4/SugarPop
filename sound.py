import pygame as pg
import time


class Sound():
    def __init__(self, duration):
        pg.init()
        pg.mixer
        
       #Make library for the sounds and for the channels 
        self.sounds = {'bucket_ping': pg.mixer.Sound('./sounds/Super Mario Bros. - Coin Sound Effect.mp3'),
                    'boom': pg.mixer.Sound('./sounds/BOOM sound effect.mp3'), 
                    'clapping': pg.mixer.Sound('./sounds/Clapping Sound Effects.mp3')}
        
        self.play_until = 0
        self.play_until = time.time() + duration
        
        
       
    
    def play_sound(self, sound_name, duration):
            self.sounds[sound_name].play()
            
            
    
            
        