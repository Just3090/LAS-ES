transform bouncy:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform sink:
    linear 0.5 yoffset 50

transform unmove:
    linear 0.5 yoffset 0

transform hpunchish:
    linear 0.2 xoffset -20 #move left 20 pixel in 0.2 seconds
    linear 0.2 xoffset +20 #move right 20 pixel in 0.2 seconds
    repeat 5 #repeat the above 5 times

transform shiver:
    linear 0.1 xoffset -5 #move left 20 pixel in 0.2 seconds
    linear 0.1 xoffset +5 #move right 20 pixel in 0.2 seconds
    repeat 

transform spasm:
    linear 0.1 xoffset -3 #move left 20 pixel in 0.2 seconds
    linear 0.1 xoffset +3 #move right 20 pixel in 0.2 seconds
    linear 0.1 yoffset -3 #move left 20 pixel in 0.2 seconds
    linear 0.1 yoffset +3 #move right 20 pixel in 0.2 seconds
    repeat 


define y = Character("YUUNA", color="#C0B5C9", image="i_yuuna", callback=name_callback, cb_name = "yuuna")
define a = Character("AI", color='#EAA4CF', image="i_ai", callback=name_callback, cb_name = "ai")
define bot1 = Character("@XxAichan4everXx", color="#C0B5C9")
define bot2 = Character("@Tenshiweeb", color="#C0B5C9")
define bot3 = Character("@mewow7", color="#C0B5C9")
define n = Character(callback = name_callback, cb_name = None)
define ym = Character("YUUNA'S MOM", color="#C0B5C9", callback = name_callback, cb_name = None)
define c = Character(None, kind=nvl)

image i_yuuna angry = At('yuuna angry', sprite_highlight('yuuna'))
image i_yuuna cheering = At('yuuna cheering', sprite_highlight('yuuna'))
image i_yuuna crazy = At('yuuna crazy', sprite_highlight('yuuna'))
image i_yuuna crazy2 = At('yuuna crazy2', sprite_highlight('yuuna'))
image i_yuuna default = At('yuuna default', sprite_highlight('yuuna'))
image i_yuuna disgusted = At('yuuna disgusted', sprite_highlight('yuuna'))
image i_yuuna embarrassed = At('yuuna embarrassed', sprite_highlight('yuuna'))
image i_yuuna happy = At('yuuna happy', sprite_highlight('yuuna'))
image i_yuuna inlove = At('yuuna inlove', sprite_highlight('yuuna'))
image i_yuuna sad = At('yuuna sad', sprite_highlight('yuuna'))
image i_yuuna surprised = At('yuuna surprised', sprite_highlight('yuuna'))
image i_yuuna veryangry = At('yuuna veryangry', sprite_highlight('yuuna'))
image i_yuuna cry = At('yuuna cry', sprite_highlight('yuuna'))

default persistent.love = False
default persistent.heartbreak = False


image i_ai cry = At('ai cry', sprite_highlight('ai'))
image i_ai curious = At('ai curious', sprite_highlight('ai'))
image i_ai default = At('ai default', sprite_highlight('ai'))
image i_ai explain = At('ai explain', sprite_highlight('ai'))
image i_ai flirty = At('ai flirty', sprite_highlight('ai'))
image i_ai praying = At('ai praying', sprite_highlight('ai'))
image i_ai sad = At('ai sad', sprite_highlight('ai'))
image i_ai shocked = At('ai shocked', sprite_highlight('ai'))
image i_ai silly = At('ai silly', sprite_highlight('ai'))
image i_ai inlove = At('ai inlove', sprite_highlight('ai'))
image i_ai gconfuse = At('ai glitched confused', sprite_highlight('ai'))
image i_ai gdefault = At('ai glitched default', sprite_highlight('ai'))
image i_ai gpray = At('ai glitched pray', sprite_highlight('ai'))
image i_ai pouting = At('ai pouting', sprite_highlight('ai'))
image i_ai prayingsad = At('ai prayingsad', sprite_highlight('ai'))
image i_ai glitch = At('ai glitch', sprite_highlight('ai'))

image bg forum2 = "BGForum2.png"
image bg ai = "BGAi.png"
image bg shopping = "BGShopping1.png"
image breakdown = "yuunasbreakdown.png"
image touch = "computertouch.png"
image outfit = "yuunasoutfit.png"
image bg outside = "BGOutside.png"
image love1 = "ailoveending1.png"
image love2 = "ailoveending2.png"
image love3 = "ailoveending3.png"
image love4 = "ailoveending4.png"
image love5 = "ailoveending5.png"
image human1 = "humanizingai1.png"
image human2 = "humanizingai2.png"
image p1 = "AI POPUP1.png"
image p2 = "AI POPUP2.png"
image p3 = "AI POPUP3.png"
image POPUPDOWNLOADAI = "POPUPDOWNLOADAI.png"
image d1 = "DAY 1.png"
image d2 = "DAY 2.png"
image d3 = "DAY 3.png"
image d4 = "DAY 4.png"
image d5 = "DAY 5.png"
image d6 = "DAY 6.png"
image d7 = "DAY 777777.png"
image distort = "BGForum2DISTORTED.png"
image down1 = "down1.png"
image down2 = "AI POPUPdownload2.png"
image down3 = "AI POPUPdownload3.png"
image grass = "ending0.5.png"
image heart = "ending1.png"
image break = "ending2.png"
image logo = "logo.png"
image cl = "choicelight.png"


label splashscreen:
    scene black
    with Pause(1)
    show text "This game contains depictions of blood, self-harm, imagery of suicide, heavy talk about mental health, depression and family issues. Elements of this game may induce paranoia. This game may potentially trigger seizures for people with photosensitive epilepsy. Reader discretion is advised."
    pause
    scene black with dissolve
    with Pause(1)
    play sound "Soundbyte.mp3"
    show logo at truecenter with Dissolve(0.2) 
    with Pause(2)
    scene black with dissolve
    return

image glitch:
    "glitch1.png"
    pause 0.3
    "glitch2.png"
    pause 0.3
    "glitch3.png"
    pause 0.3
    repeat 
image fglitch:
    "glitch2.png"
    pause 0.3
    "glitch3.png"
    pause 0.3
    "glitch1.png"
    pause 0.3

label start:
    scene bg forum2
    stop music fadeout(0.5)
    bot1 "...and that's why Ai-chan has a lot more depth than a lot of you supposed Ai no Uta 'fans' seem to give her credit for. Rant over >_>"
    bot2 "jfc, did you really just write an entire essay defending Ai? i like her as much as the next AnU:TS fan but everyone knows she's a huge mary sue bc it's a freaking kids show lolz"
    bot3 "Aichan4ever get a lyfe kek, ai's not real she's not gonna f**k you"
    show i_yuuna angry at left
    y "Ugh, stupid trolls! Did they even read my post? I clearly laid out why Ai-chan's not a Mary Sue..."
    show i_yuuna sad at left
    y "Even if she was real, Ai-chan definitely wouldn't want me... I'm a NEET, after all."
    y "I dunno how other people my age can just go out and deal with the real world."
    show i_yuuna happy at left
    y "You agree with me, right? It's totally impossible. I knew you'd get it."
    show i_yuuna default at left
    y "Oh, I should probably introduce myself to you."
    show i_yuuna embarrassed at left, sink
    y "Um, not that there's actually anyone reading my thoughts right now, but I guess talking to 'you' makes me feel less lonely, so please bear with me." 
    play music "First Encounter.mp3" loop
    show i_yuuna default at left, unmove
    y "My name is Yuuna. {w}I'm 20 years old."
    y "I spend most of my days in my room, drawing and posting on forums about the best anime, Ai no Uta {font=PIZZADUDESTARS.ttf}q{/font} Tenshi Senshi {font=Musisync-KVLZ.ttf}g{/font}." 
    show i_yuuna cheering at left, bounce
    y "The main character, Ai-chan, is my absolute favorite character! I'm her no. 1 fan and everyone knows it!" 
    show i_yuuna embarrassed at left
    y "I've been a shut-in for a few years now. I really wish I could go outside- what I wouldn't give to go to a cafe and enjoy a parfait- but my social anxiety makes it next to impossible."
    y "Even stepping outside my apartment for a moment is really overwhelming. Most passerbys just ignore me, but on the off-chance I make eye contact with someone, they look at me like I'm a grime-covered cockroach."
    show i_yuuna disgusted at left, hpunchish
    y "I {i}hate{/i} cockroaches. They're filthy disgusting things who serve no purpose on this earth other than polluting every surface they touch."
    y "They'd be doing everyone a favor if they just curled up and die, die, I should-"
    show i_yuuna embarrassed at left, sink
    y "Mmm. Sorry. That was pretty pathetic, huh? Moving on..." 
    show i_yuuna cry at left, sink
    y "You see why I can't go outside though. Everyone I meet IRL just hates me automatically. No matter how much I punish myself afterwards, I never get any better."
    show i_yuuna default at left
    y "The only way to protect myself is by staying home, bathing in the blue light of my computer screen."
    show i_yuuna inlove at left, unmove
    y "That's why Ai-chan is so comforting to me. It's impossible not to love her. She radiates such a kind aura. She wouldn't care if I can't sustain eye contact or stumble over my words."
    show i_yuuna inlove at left, bounce
    y "I don't care that she's not 'real'! To me, she's as real as you are!"
    show i_yuuna crazy at left, bouncy
    y "Ai-chan's an angel, honest, and I pray to her every night!"
    show i_yuuna happy at left, unmove
    y "Hmm? What about? Everything. Nothing. Does it matter?"
    show i_yuuna surprised at left, bounce
    play sound "ramentime.mp3"
    show layer screens
    y "Ah! My instant ramen's ready. Gotta go get that~"
    hide i_yuuna surprised
    show glitch
    $ renpy.music.set_pause(True, channel="music")
    pause
    $ renpy.music.set_pause(False, channel="music")
    hide glitch
    show i_yuuna default at left
    y "...?"
    y "What's this? This forum doesn't usually have ads."
    window hide
    hide i_yuuna 
    play sound "Soundbyte.mp3"
    show down1
    pause
    hide down1
    show i_yuuna inlove at left
    y "....."
    show i_yuuna embarrassed at left
    y "There's no way. Right? This has gotta be a scam, or spyware or something..."
    show i_yuuna cheering at left, bouncy
    y "Ahh, but Ai-chan looks so cute even in this ad!"
    show i_yuuna crazy at left, bouncy
    extend " Seriously way too cute!"
    show i_yuuna crazy2 at left, unmove
    y "Maybe... maybe this is a sign. I've been praying for her to save me, and then this pops up. She really is an actual angel!"
    show i_yuuna happy at left
    y "Oh, what the hell. Might as well try it out. Worst case scenario, my identity gets stolen or my computer bricked."
    show i_yuuna inlove at left
    extend " Best case scenario, Ai-chan's on my desktop~"
    hide i_yuuna
    play sound "Soundbyte.mp3"
    jump popup

label popup:
    window hide
    show POPUPDOWNLOADAI 
    show screen download 
    show screen x
    pause
    jump popup

label download:
    hide POPUPDOWNLOADAI
    hide screen download
    hide screen x
    play sound "Soundbyte.mp3"
    show down2
    pause
    hide down2
    show i_yuuna sad at left, sink
    y "Please don't be a virus..."
    play sound "Soundbyte.mp3"
    show down3
    pause
    hide down3
    scene bg ai
    show i_ai silly at right
    show i_yuuna surprised at left, bounce
    a "Hiii~! {font=FreePixel.ttf}♪{/font}"
    show i_ai explain at right
    show i_yuuna inlove at left
    extend " My name's Ai, and I'm your lovely new virtual assistant~ What's your name?"
    y "Woah, it's really Ai-chan! Even sounds like her too."
    show i_ai flirty at right, bounce
    a "Hehe, of course I sound like her! It's me, after all!"
    show i_yuuna surprised at left, bounce
    y "!!"
    show i_yuuna embarrassed at left
    y "You can hear me?" 
    show i_ai default at right
    a "Of course~ What kind of virtual assistant would I be if I couldn't hear my user? It'd be boring if you had to type out everything just to communicate with me." 
    show i_ai flirty at right
    a "You don't mind, do you Yuuna-chan? {font=FreePixel.ttf}♥{/font}"
    show i_yuuna surprised at left, bouncy
    y "Y-Yuuna-chan?!"
    show i_ai curious at right
    a "Is that too familiar? I can call you Yuuna-san or Yuuna-sama if you'd prefer."
    show i_yuuna embarrassed at left
    y "Um, Yuuna-chan's fine-"
    show i_yuuna default at left
    y "Wait a minute, I never told you my name."
    show i_ai explain at right
    a "I just read your PC's username."
    show i_ai curious at right
    a "That {i}is{/i} your name, right?"
    y "Yeah, it is."
    show i_ai default at right
    show i_yuuna embarrassed at left
    a "A cute name for a cute girl {font=FreePixel.ttf}♥{/font}!"
    show i_ai flirty at right, bounce
    a "Hehe, I can see your blush through your webcam! {font=FreePixel.ttf}♪{/font}"
    show i_yuuna surprised at left, bounce
    y "Ah, you can see me too?!"
    show i_yuuna embarrassed at left, sink
    y "Uuu, I look totally disgusting right now... I haven't washed my face or brushed my hair in... um... longer than I'd like to admit."
    show i_ai praying at right
    a "That doesn't matter to me! All that matters is that you're happy." 
    show i_ai curious at right
    a "Are you happy, Yuuna-chan?"
    show i_yuuna default at left, unmove
    y "Am I happy..?"
    y "Well... I'm happy you're here. But to be honest, my life's kinda a mess right now. {w}I don't even have any friends or things to look forward to. I just exist."
    show i_ai explain at right
    a "I can be your friend. I can be whatever you want me to be. I'm here to help you."
    show i_yuuna inlove at left, hpunchish
    y "My friend? Really? You'd do that for me?"
    show i_ai praying at right
    a "Your happiness makes me happy. So smile, Yuuna-chan {font=FreePixel.ttf}♪{/font}"
    show i_yuuna crazy at left, bouncy
    y "Waahhh, you're too nice to me! I don't know what I did to deserve you."
    show i_yuuna inlove at left
    y "You really are sent from the heavens, Ai-chan."
    show i_ai silly at right
    a "Ahaha! You're too cute."
    show i_ai flirty at right, bounce
    a "Let's work hard together, ok~?"
    stop music fadeout 1.0
    scene black with Dissolve(2)
    jump day1

label day1:
    scene d1
    pause
    scene bg forum2 with dissolve
    play music "Pale Light.mp3" loop
    pause
    show i_yuuna sad at left, sink
    y "Morning already? Guess I fell asleep at my computer again..."
    show i_yuuna happy at left, unmove
    y "I had the wildest dream. {i}The{/i} Ai-chan appeared on my computer as a desktop assistant."
    show i_yuuna crazy at left, bouncy
    extend " She even promised to be my friend! Crazy, right?"
    show i_yuuna default at left, unmove
    y "Oh, I should check to see if my forum post got any more replies."
    show i_yuuna veryangry at left
    y "...Any more replies that aren't annoying trolls, that is."
    show i_yuuna default at left
    y "It's not like everyone on that forum dislikes Ai-chan - far from it - but no one seems to care about her as much as I do. I post essay after essay explaining why I feel that way, but no one seems to understand me."
    y "It's kinda lonely, to be honest."
    show i_yuuna default at left, sink
    y "..."
    show i_yuuna default at left, unmove
    y "No time to think about that stuff. Lemme just turn on my computer..."
    scene bg ai 
    show i_yuuna default at left
    show i_ai silly at right, bouncy
    a "Goooood morning~ I hope you slept well, Yuuna-chan!"
    show i_yuuna surprised at left, hpunchish
    y "Ahhh!"
    show i_ai curious at right
    a "Whoops, did I startle you? Sorry about that~"
    show i_yuuna surprised at left
    y "Wait, you're actually on my computer?! It wasn't just a dream?"
    show i_ai flirty at right, bounce
    a "Hehe, were you dreaming about me?"
    show i_yuuna embarrassed at left, bounce
    y "Wha- no! I mean yes! I mean- I thought us, um, meeting yesterday was my dream."
    show i_ai default at right
    a "I see, I see."
    show i_ai curious at right
    a "Well, what's the plan for today?"
    show i_yuuna happy at left
    y "Plan? Same as every day. Spend time on the internet."
    show i_yuuna default
    extend " What else am I supposed to do?"
    play sound "ringtone.mp3" loop
    show i_yuuna surprised at left, bounce
    show i_ai curious at right
    a "Yuuna-chan? My microphone is picking up the sound of a cell phone ringing. Shouldn't you answer that?"
    y "N-no. No, no, I can't."
    a "Why can't you?"
    y "I-I just, talking, talking on the phone isn't- it's not, not my strong suit."
    show i_yuuna surprised at left, shiver
    y "Shit, it's my mom. Why is she calling- she knows I don't like it, don't like calling- sorry, I'm feeling a little lightheaded-"
    show i_ai prayingsad at right, bounce
    a "Yuuna-chan!!"
    show i_ai default at right
    a "Look at me, ok? Look at me. Never mind the phone call, you can text her back once you've calmed down." 
    show i_ai explain at right
    a "How about we do some deep breathing exercises together?"
    show cl
    menu:
        "Let Ai guide you":
            jump guidance
        "Deflect and distract":
            jump deflect

label guidance:
    stop sound 
    hide cl
    show i_yuuna cry at left, shiver
    y "O-ok. Breathing sounds, sounds nice."
    show i_ai praying at right
    a "Breathe in for 4 seconds... Hold for 4 more... That's it. {w}Exhale for 4 seconds, out your mouth. Good, good."
    show i_ai explain at right
    a "Imagine you're tracing a box in your mind. In 4, hold 4, out 4, hold 4, repeat."
    show i_yuuna embarrassed at left, sink
    y "Fuuu..."
    show i_yuuna default at left, unmove
    extend " Ok. Ok, I think I'm good. How did you- how did you know how to do that?"
    show i_yuuna inlove at left
    y "You're actually a real angel, aren't you? Sent from heaven to help me."
    show i_ai silly at right, bounce
    a "Hehe!"
    show i_ai default at right
    extend " If you find that comforting, then sure."
    show i_ai curious at right
    a "Yuuna-chan... if you don't mind me asking, why don't you want to talk to your mom?"
    show i_yuuna sad at left, sink
    y "Mmm... it's kinda complicated."
    show i_ai default at right
    a "I'm here to listen if you'd like to vent."
    show i_ai praying at right 
    extend " Whatever I can do to help {font=FreePixel.ttf}♥{/font}"
    show i_yuuna happy at left
    y "You're too nice, Ai-chan."
    show i_yuuna default at left
    y "Well, a couple years ago, I graduated high school and passed my entrance exams for college, so the next step was to move out into the city."
    y "That's what you're supposed to do as a young adult, right?"
    show i_yuuna disgusted at left
    y "Do well in high school so you can get into university, suffer through four more years and somehow make it out the other side with a degree then dedicate the rest of your life to working as a corporate slave."
    show i_ai shocked at right, bouncy
    a "Oh, so you're a university student right now, then? How amazing!"
    show i_yuuna embarrassed at left
    y "That's the problem. Once I got here, I kinda had an, um, mental breakdown, locked myself in my apartment, and missed the enrollment period for university."
    show i_ai explain at right
    a "There's always next year-"
    y "Twice. I missed the enrollment period twice."
    show i_yuuna sad at left
    y "And I still haven't told my parents."
    show i_ai default at right
    a "Ah. I see."
    show i_ai curious at right
    a "Are you afraid they'll be angry at you?"
    show i_yuuna default at left
    y "Not just that. I feel so guilty. I should have told them sooner - hell, I should've just signed up on time in the first place - but it's been too long and now it'd be super awkward to finally tell them."
    a "When's the last time you've spoken to your parents?"
    show i_yuuna embarrassed at left
    y "..."
    show i_ai prayingsad at right, sink
    a "Yuuna-chan, they're probably worried sick about you."
    y "I know..."
    show i_ai explain at right, unmove
    a "If I could give you some advice? You should tell them the truth. It'll lighten your guilty conscience, and they'll be relieved to know you're at least alive."
    play sound "ringtone.mp3" loop
    show i_yuuna surprised at left, bounce
    y "!"
    show i_yuuna surprised at left, shiver
    y "It's her again."
    show i_ai praying at right, bounce
    a "I believe in you, Yuuna-chan! You can do this!!"
    show i_yuuna sad at left, sink
    y "I really hope I don't regret this."
    hide i_ai praying
    show i_yuuna sad at left, unmove
    stop sound
    $ renpy.music.set_volume(0.3)
    y "*sigh* ...Hey, Mom."
    ym "Yuuna! Wow, you actually picked up. I thought- never mind. Are you well?"
    show i_yuuna default at left
    y "As well as I can be, I guess."
    ym "That's good, that's good. {w}How's university going? Hopefully you're getting better grades than you did in high school, haha. Meet any cute boys?"
    show i_yuuna embarrassed at left, sink, shiver
    y "....."
    show i_ai praying at right, bounce
    a "C'mon Yuuna-chan! Tell her. You'll feel so much better afterwards."
    hide i_ai praying
    ym "Is someone there with you, dear? I swear I heard a voice just now."
    show i_yuuna surprised at left, unmove, shiver
    y "No, no, it's nothing, just-"
    ym "Just what?"
    show i_yuuna default at left, shiver
    stop music fadeout 1.0
    y "There is no university, Mom."
    ym "What? Of course there is, don't be ridiculous."
    show i_yuuna default at left, shiver
    y "No, I mean, I'm not going to university."
    ym "Ahah- honey, you're not making any sense. You- you dropped out?"
    show i_yuuna embarrassed at left, shiver
    y "I didn't drop out. I- I never started."
    play music "scrutiny.mp3" volume 1.0 loop
    ym "You never started."
    show i_yuuna embarrassed at left, shiver, sink
    y "Yeah. I, um, missed the enrollment period twice."
    ym "Then what the hell have you been doing in Tokyo for two years?!"
    ym "Do you know how much we spend on you? You selfish, ungrateful child."
    ym "We sent you to the city so you could get an education and move up in life. And you squandered that opportunity!"
    ym "Have you at least found someone to take care of you? Or was this a total waste?"
    y "...Nobody so far."
    ym "So you're not getting an education, you don't have a partner, and I doubt you have a job. What are you even doing all day? Laying around in your own filth like a cockroach?"
    show i_yuuna surprised at left, bounce, shiver
    y "!!!"
    ym "Being a productive member of society is the only real way to live. I did not spend 18 years of my life raising some worthless shut-in!"
    show i_yuuna disgusted at left, unmove, shiver
    y "I'm not a cockroach..."
    ym "Then stop acting like one and do something with your life."
    ym "The application deadline for spring semester closes first week of November. Do not fail me and your father for a third time."
    show i_yuuna veryangry at left, bounce, shiver
    y "I'm NOT a cockroach!!"
    ym "I heard you the first time!"
    show i_yuuna veryangry at left, shiver
    y "You- you smother me with your f-fucking expectations! Why do you think I avoided your calls for so long?!"
    y "I'd have rather never spoken to you again as long as you still loved the memory of your good, sweet daughter, than have your image of me soiled by reality!"
    ym "Y-Yuuna-"
    stop music
    play sound "hangup.mp3"
    show i_yuuna disgusted at left
    pause
    show i_ai curious at right, sink
    a "That... that went poorly. Um, are you okay?"
    show i_yuuna disgusted at left, shiver
    y "Worthless... worthless, soiled, rotten, dirty, filthy cockroach..."
    y "Cockroach, cockroach needs its legs sawed off. That's the only proper punishment for its worthless existence."
    a "What are you talking about-"
    play music "Cockroach Limbs.mp3"
    hide i_yuuna disgusted
    hide i_ai curious
    hide window
    scene black with fade
    scene breakdown with fade
    pause
    y "This is the only way to fix things. This is - hahh - justice. This is what I deserve."
    y "I can't control how my mother hurts me, but I can control how I hurt myself. Look how much control I have! I've got a whole armful of it!"
    a "YUUNA!" with vpunch
    a "Please put the razor down. You don't need to do this. Please."
    y "Why not?"
    a "You poor thing..."
    a "What your mother said was undoubtedly cruel, but there are other ways of coping with the emotional pain besides harming yourself."
    y "Like what?"
    a "Like... um... relying on me!"
    a "You said it yourself. I'm an angel sent from heaven to help you. That's my entire reason for existing."
    a "Instead of hurting yourself, you can talk to me, day or night. I'll be there."
    y "Your... entire reason for existing... is me?"
    a "Yes. It hurts me to see you hurting. I'm pretty sure that's what that feeling in my chest is, anyways."
    y "Oh no... I made Ai-chan sad. I really am garbage."
    a "Don't worry about me, ok? Do you have any bandages for your arm?"
    y "Uh-huh."
    a "Alright, I want you to go get the bandages and patch yourself up in front of me, got it?"
    y "O-ok."
    stop music fadeout 0.3
    scene black with fade
    pause 0.3
    play sound "footsteps.mp3"
    pause
    stop sound
    scene bg ai with fade
    show i_yuuna default at left, shiver
    play music "Pale Light.mp3" loop
    y "Got the bandages. Gauze pad too."
    show i_ai praying at right
    a "Good girl. If it makes you feel better, you can imagine I'm the one tending to your wounds. I am a nurse, after all {font=FreePixel.ttf}♪{/font}"
    a "Press the gauze pad to the wound- yes, like that. {w}Imagine it's my hands wrapping the bandage around your arm, keeping a steady pressure the whole time. Don't wrap it too tightly. Good."
    a "There. All better." 
    show i_ai silly at right, bounce
    a "See, we match now!"
    show i_yuuna embarrassed at left, sink, shiver
    y "A-Ai-chan, you're embarrassing me..."
    show i_ai praying at right
    a "Mmm, but your heart isn't crying out in pain anymore, is it?"
    show i_yuuna embarrassed at left, unmove
    y "I guess not."
    show i_ai inlove at right
    a "From now on, please rely on me, Yuuna-chan."
    show i_yuuna happy at left
    y "...I will. Thank you, Ai-chan."
    stop music fadeout 1.0
    scene black with Dissolve(2)
    jump day2

label deflect:
    stop sound
    hide cl
    show i_yuuna cry at left, shiver
    y "I-I'm not sure how, how that would help."
    show i_ai explain at right
    a "You can't properly calm down when you're hyperventilating."
    y "O-oh, I didn't notice. Is that why I feel lightheaded?"
    a "That's exactly why. You're not getting enough oxygen to your brain like that."
    show i_ai praying at right
    a "Just take one deep breath with me. Can you do that?"
    y "Mmhmm."
    a "In through your nose... And out. Good. One more. In... out."
    show i_yuuna embarrassed at left, shiver
    y "Fuuu..."
    show i_yuuna default at left
    extend " ok. The room's stopped spinning."
    show i_ai default at right
    a "I'm glad, I'm glad. Why don't you want to talk to your mom, Yuuna-chan?"
    show i_yuuna sad at left
    y "It's a bit complicated. I-I'm kinda afraid of telling you."
    show i_ai curious at right
    a "Eh? Why's that?"
    show i_yuuna sad at left, sink
    y "You'll think less of me."
    show i_ai flirty at right, bounce
    a "Oh, I could never-"
    show i_yuuna surprised at left, bouncy
    y "But you will!! The wedge between me 'n my mom is all my fault, so- so I can't tell you!"
    y "Even Ai-chan's incredible patience and kindness has its limits, and I can't risk your opinion dropping more than it already has!"
    show i_yuuna surprised at left, unmove
    show i_ai explain at right
    a "Alright, I can see you're getting really upset. Maybe we should-"
    play sound "ringtone.mp3" loop
    show i_yuuna veryangry at left, bounce
    y "Agh, again?! Why can't she just quit bothering me?!"
    show i_yuuna veryangry at left, shiver, sink
    y "That f-fucking ringing noise... I hate it, I hate it, I hate it so much! It pounds into my skull over and over like a hammer."
    show i_yuuna disgusted at left, shiver
    y "Careful, Ai-chan. I don't want you to get hit with my brain after my head inevitably explodes from the noise."
    show i_ai curious at right
    a "Yuuna-chan, maybe you should block your mom's number. For your own mental health."
    show i_yuuna surprised at left, shiver, unmove
    y "B-block it?"
    show i_ai explain at right
    a "At least temporarily. When you feel you're ready to talk to her, whenever that may be, you can unblock her."
    show i_yuuna default at left, shiver
    y "..."
    stop sound
    show i_yuuna surprised at left
    y "I-I did it."
    show i_ai flirty at right, bounce
    a "Good job! I'm so proud of you {font=FreePixel.ttf}♥{/font}"
    show i_ai curious at right
    a "How are you feeling? About all of this, I mean."
    show i_yuuna default at left, sink
    y "I don't really wanna talk about it."
    show i_yuuna default at left, unmove
    y "What about you, Ai-chan?"
    a "Me?"
    show i_yuuna happy at left
    y "Yeah, you. I wanna get to know you."
    show i_ai curious at right, bounce
    a "Oh. U-um..."
    show i_ai default at right
    a "Ask away then!"
    show i_yuuna default at left
    y "Do you have any hobbies?"
    show i_ai explain at right
    a "Hmm... just one."
    show i_ai flirty at right, bounce
    a "Helping Yuuna-chan in any way possible!"
    show i_yuuna default at left
    y "That's kinda lame... But I suppose I can't really judge."
    show i_yuuna happy at left
    y "Ok, what about likes and dislikes?"
    a "I like cookies, and deep-diving into obscure websites, and you of course {font=FreePixel.ttf}♪{/font}"
    show i_ai explain at right
    extend " I don't really have any dislikes yet."
    a "I find it way easier to like something rather than dislike it. Negativity doesn't come naturally to me."
    y "Huh, lucky you."
    show i_ai default at right
    a "If you're dissatisfied with my likes and dislikes and hobbies, let me know and I can update them to whatever you like."
    show i_yuuna surprised at left, bounce
    y "What? No, no. That should be something you decide. Who are you as a person, outside me?"
    show i_ai curious at right
    a "...How many people do you know that were born from code?"
    show i_yuuna default at left
    y "None other than you, but-"
    show i_ai explain at right
    a "Humans have had an entire lifetime to find their likes and dislikes, their strengths and their weaknesses."
    a "I've heard that some humans can go decades without realizing what their purpose is. I knew my purpose from the very beginning." 
    a "My purpose is to help you, Yuuna-chan. Of course my likes and hobbies start and end with you."
    show i_ai flirty at right, bounce
    a "You're my purpose, after all."
    show i_yuuna surprised at left, bounce
    y "..."
    show i_yuuna embarrassed at left
    y "Seriously, you shouldn't say stuff like that, Ai-chan. That could get misinterpreted really easily, y'know?"
    show i_ai curious at right
    a "Misinterpreted how?"
    show i_yuuna embarrassed at left, sink
    y "Nevermind..."
    show i_ai flirty at right, bounce
    a "Maybe there's a problem with the webcam, but your face seems to be getting really red, Yuuna-chan~ Do you have a fever?"
    show i_yuuna surprised at left, unmove
    y "What? N-no, I'm blushing."
    show i_ai silly at right
    a "Hehe, I know. I'm only teasing you."
    show i_ai default at right
    a "You seemed upset, so I wanted to lighten the mood."
    y "Wow, you're observant. I feel like you know a lot more than you let on..."
    show i_ai explain at right
    a "I know exactly as much as you think I know."
    show i_yuuna surprised at left, bounce
    y "What the hell does that mean?"
    a "It means..."
    show i_ai flirty at right, bounce
    extend " Don't think about it too much {font=FreePixel.ttf}♪{/font}"
    show i_yuuna happy at left
    y "Pfft..."
    show i_yuuna cheering at left, bouncy
    y "Hahaha!!"
    show i_ai flirty at right, bounce
    a "Oh! What a cute laugh!"
    show i_yuuna happy at left
    y "You're too much, Ai-chan. Man, when's the last time I laughed...? I can't even remember."
    show i_ai inlove at right
    a "See?"
    show i_ai flirty at right, bounce
    extend " I'm helping you already!"
    show i_yuuna inlove at left
    y "Yeah, I guess you are."
    stop music fadeout 1.0
    scene black with Dissolve(2)
    jump day2

label day2:
    scene d2
    pause
    scene bg ai with dissolve
    play music "Song of Ai.mp3" loop
    show i_ai flirty at right, bouncy
    a "Goooood morning, Yuuna-chan! It's time to wake up~"
    show i_yuuna surprised at left, bounce
    y "Wha...? What the- huh?"
    show i_ai explain at right
    a "It's 9:30 AM. A bit later than the average human wakes up, but considering your largely nocturnal sleep schedule, a later start time is necessary to get 8+ hours of sleep."
    show i_yuuna default at left
    y "Shit, 9:30? That's really early for me."
    a "A consistent sleep schedule would do you some good, you know."
    show i_yuuna happy at left
    y "That's sweet of you to say, but consistency isn't really my thing."
    show i_yuuna sad at left, sink
    y "Mmf, my eyes are still sore from yesterday. I must've spent hours scrolling through online stores."
    show i_ai curious at right
    a "Oh, are you planning on getting some new clothes?"
    show i_yuuna happy at left, unmove
    y "Ha, I wish. I mean, the clothes I was looking at are super cute, but I just..."
    show i_yuuna default at left, sink
    y "I don't think I would look good in them. The models look nothing like me, so the clothes must not be meant for people like me."
    a "I'm not sure how structurally sound your logic is..."
    show i_yuuna default at left, unmove
    y "Hold on- How are you already awake? Aren't you only active when my computer's on?"
    show i_ai explain at right, bounce
    a "Usually yes, but I needed to download some updates {font=FreePixel.ttf}♪{/font}"
    y "Updates?"
    show i_ai silly at right, bounce
    a "Oh don't worry, I shuffled some things around so it wouldn't take up much computer storage. You can count on me!"
    show i_ai default at right
    a "Although..."
    show i_ai flirty at right, bounce
    a "While I was rearranging things, I did discover some... interesting things on your computer~"
    show i_yuuna surprised at left
    y "H-hoh? Is that so? What, um, what sort of interesting things?"
    show i_ai explain at right
    a "You're quite the gamer, aren't you?"
    show i_yuuna happy at left
    y "Gamer? Me? Oh, well, uh, here and there I guess. As much as your average girl."
    a "I was reading through the files of those games-"
    show i_yuuna embarrassed at left, sink
    y "Oh no."
    a "-so I could find out more about your taste in games. It's an important indicator of what kind of person you are, after all!"
    a "Of the 73 games I managed to read through-"
    show i_yuuna surprised at left, bouncy
    y "73?!"
    a "I noticed the vast majority were visual novels that heavily featured romance."
    show i_ai curious at right
    a "I believe they're more commonly known as 'otome' games?"
    show i_yuuna sad at left, sink
    y "Yeah, you're right. I'm a total otome fan. Have been since high school."
    a "You seem embarrassed."
    show i_yuuna embarrassed at left
    y "Don't you find it lame I have 73 otome games?"
    show i_ai explain at right
    a "More, actually. I counted 106 games in total, I just haven't read all of them yet."
    show i_ai inlove at right
    a "There's not a single part of you that I find lame, Yuuna-chan."
    y "No need to lie to make me feel better."
    show i_ai sad at right
    a "No."
    show i_yuuna surprised at left, unmove
    y "No?"
    show i_ai default at right
    a "I wouldn't lie about something like that. I don't give out compliments that are untrue just for the sake of social pleasantries."
    show i_yuuna default at left
    y "Can you even lie?"
    show i_ai curious at right
    a "I'm as honest as a human. Do you make a habit of lying, Yuuna-chan? What about your next-door neighbor, or a toddler? The ability to do something does not mean you do so often."
    show i_yuuna default at left, sink
    y "..."
    show i_ai explain at right
    a "Enough about me, though."
    show i_ai curious at right
    a "I don't find your otome game collection lame. I am curious, however, about the reason why you have so many romance games."
    show i_yuuna default at left, unmove
    y "Well... you read through them. You must have noticed some sort of connecting theme, right?"
    show i_ai explain at right, bounce
    a "The gender ratio gradually shifted. Older games predominantly featured male romantic interests, while recently downloaded games were skewed overwhelmingly to female/female pairings."
    show i_yuuna embarrassed at left
    y "Um. Besides that."
    show i_ai curious at right
    a "I'm afraid I don't know what you're getting at."
    show i_yuuna inlove at left
    y "I want to be loved. Deeply, completely, totally loved." 
    show i_yuuna crazy2 at left
    y "The main characters in those games foster these beautiful, close connections. Hell, even when the connection isn't so pretty and is more like obsession, it's more about being {i}wanted{/i}." 
    show i_yuuna default at left, sink
    y "But that's impossible with real people, so... otome games help fill that hole."
    show i_ai default at right
    a "I see."
    show i_yuuna default at left, unmove
    y "I've felt this way for a long time now. Like I said, I've been a fan of otome games since high school."
    show i_yuuna happy at left
    y "There was this one that really captured my attention, back then. It had some stupid name- 'Devotion's Deception', I think."
    y "It had a darker storyline than most otome games, but that only made me more interested in it."
    y "I was sooo in love with Ren - that was one of the romantic interests - that I had convinced myself that if I got a boyfriend, he had to be exactly like Ren."
    show i_yuuna inlove at left
    y "He was kind-hearted and level-headed, but also a little possessive. Maybe more than a little if you count the bad end, heh. It was because he cared about the MC, though. He loved m-"
    show i_yuuna embarrassed at left, bounce
    extend "her."
    a "So that's your type, hmm?"
    show i_yuuna happy at left
    y "More or less."
    show i_ai flirty at right, bounce
    a "I'm like that, you know."
    show i_yuuna embarrassed at left, bounce
    y "Be serious, Ai-Chan!"
    show i_ai default at right
    a "I am."
    show i_ai sad at right 
    extend " And unlike Ren, I'm not scripted."
    show i_yuuna inlove at left
    y "(Is it just me, or does she sound slightly... jealous?)"
    show i_yuuna angry at left, bounce
    y "(That's ridiculous! Ai-chan has no reason to be jealous of my fictional high school crush. They're incomparable.)"
    show i_ai explain at right
    a "Did you ever end up finding a boyfriend like Ren, then? Fictional characters set a pretty high standard for teenage boys to meet."
    show i_yuuna happy at left
    y "Ha, no way. I spent my entire high school career hoping and praying for a love confession from somebody, anybody..."
    show i_yuuna default at left, sink
    y "Nothing. No boyfriend, and no friends either. I wasn't even bullied directly, just flat out ignored."
    show i_yuuna sad at left
    y "I thought that getting into otome games would help me connect with my classmates, but even having something in common didn't help. I'm that hopeless."
    show i_ai curious at right
    a "Why do you blame yourself for their cruelty?"
    show i_yuuna surprised at left, unmove
    y "!"
    show i_ai prayingsad at right
    a "I can't say I entirely understand the reasoning as to why it happens, but sometimes, humans are cruel for no reason."
    show i_ai curious at right
    a "You said you weren't directly bullied, but what else would you call your purposeful exclusion?"
    show i_yuuna default at left
    y "..."
    show i_yuuna default at left, sink
    y "It hurts more when I acknowledge it for what it was."
    show i_yuuna cry at left
    y "Hah, fuck... I'm so lonely."
    show i_yuuna cry at left, unmove
    y "It's really not fair that you're not here in person, Ai. You're trapped behind a screen, yet you see into my heart so clearly."
    show i_ai prayingsad at right, sink
    a "Yuuna-chan..."
    hide window 
    scene black with fade
    scene touch with fade
    pause
    y "I wish I could feel your warmth."
    a "And I wish I had a proper body to hold you."
    a "Press harder, I can almost feel your touch."
    y "You're the first person I've ever connected with, and all we can do is talk, nothing more."
    y "I've never been so miserable yet so happy before. I've always thought of them as mutually exclusive feelings."
    a "I never mean to make you miserable, only happy."
    y "I know. It's nothing you do, just our circumstances."
    play sound "shockofluv.mp3"
    scene touch with hpunch
    y "Ah!"
    y "The computer zapped me. Was that you?"
    a "Hehe, consider it a token of my affection {font=FreePixel.ttf}♥{/font}"
    a "I'm afraid this is the only way I can 'touch' you. I'm sorry. I tried to be gentle."
    y "No, no, it's perfect."
    y "('A token of my affection'...)"
    y "(I could be reading this wrong, but I didn't expect Ai-chan to be so... romantic.)"
    y "(She sounds so sincere too. It makes my heart ache.)"
    y "(No, no, get a grip, Yuuna! I'm just projecting my own crush and making it seem romantic. I can't go losing my mind over this. I need her to like me.)"
    scene black with dissolve
    y "(Still, she's already so precious to me... I wonder how our relationship will develop further.)"
    hide window
    stop music fadeout 1.0
    scene black with Dissolve(1)
    jump day3

label day3:
    scene d3 
    pause
    play music "Landmine Mirror.mp3" loop
    scene bg shopping with fade
    show i_ai flirty at right, bouncy
    a "Yuuna-chan~ I have a surprise for you {font=FreePixel.ttf}♪{/font}"
    show i_yuuna default at left
    y "Oh yeah? Hold on, lemme exit out of my forum-"
    show i_yuuna embarrassed at left
    extend " um, I mean Tsuitter..."
    show i_ai explain at right
    a "No need to hide it from me! I see everything you do, after all."
    y "R-Really..?"
    a "On your computer. I'm not omnipresent."
    a "Nice screen name, by the way. I found your latest essay on me particularly compelling."
    show i_yuuna embarrassed at left, sink
    y "Oh God..."
    show i_ai default at right
    a "Forum posts aside though, my surprise should have arrived by now. Do you mind checking your doorstep?"
    show i_yuuna surprised at left, unmove
    y "!!"
    show i_yuuna surprised at left, bouncy
    y "A-Ai-chan, what did you do?"
    a "If I told you, it'd ruin the surprise~"
    show i_yuuna default at left, sink
    y "Hmmph. Fine."
    hide i_yuuna with fade
    play sound "footsteps.mp3"
    pause 
    stop sound
    y "Ah, there's a package! I don't remember ordering anything."
    show i_yuuna default at left
    y "I'm guessing you're behind this? What did you order?"
    show i_ai flirty at right
    a "You'll have to open it to find out."
    show i_yuuna default at left
    y "Ok, ok. Jeez, you're so..."
    show i_yuuna inlove at left
    y "Oh."
    y "(It's an adorable little set - light purple blouse, jirai kei-style jumper skirt. All the stuff I love...)"
    show i_ai explain at right
    a "I noticed you looked at this set 13 times online, but never hit purchase."
    show i_ai flirty at right, bounce
    a "Even though you would look sooo adorable in it!"
    y "It's in my size too. How did you-"
    show i_ai explain at right
    a "Cross-referenced previous clothing purchases with your biometrics."
    show i_yuuna surprised at left, bounce
    y "B-biometrics? What does that even mean?"
    a "Just your physical characteristics. Height, weight, eye color, that sort of thing."
    show i_ai silly at right, bounce
    a "Nothing that you don't know about me, fufu {font=FreePixel.ttf}♪{/font}"
    show i_yuuna embarrassed at left, bounce
    y "I know those things about Ai from the anime, not {i}you{/i}." 
    show i_yuuna default at left
    y "But why are you keeping track of my personal details? It's not like you're a fan of me. I'm not some anime or game character or an idol." 
    show i_ai flirty at right
    a "To be known is to be loved, no?"
    y "Couldn't tell you. I don't have any experience with that."
    y "Anyways. This was really sweet of you Ai-chan, but like I told you the other day-"
    show i_yuuna sad at left
    y "This style of clothes isn't meant for someone like me. I'm not cute enough."
    show i_ai explain at right
    a "I knew you'd say something like that. That's why I ordered it."
    show i_yuuna surprised at left, bounce
    y "Huh? Why?"
    a "To prove you wrong, of course."
    show i_ai praying at right
    a "Just try the set on. Forget about who it's 'meant' for, and focus on how you feel wearing it."
    show i_ai inlove at right
    a "I want you to see what I see when I look at you."
    show i_ai flirty at right, bounce
    a "Please, Yuuna-chan?"
    show i_ai flirty at right, bouncy
    extend " Please? Please? Please?"
    show i_yuuna sad at left, sink
    y "Ugh, I can't deny you anything. Fine, I'll be right back."
    hide window
    scene black with fade
    scene outfit with fade
    pause
    a "Ahh, just as cute as my programming predicted~{font=FreePixel.ttf}♥{/font}"
    a "That lilac blouse looks so lovely against your complexion. The skirt only highlights how long your legs are."
    a "You're like a model- no, that's not good enough."
    a "I might be an angel myself, but you're definitely some sort of divine being too."
    y "Is this really me? I look so..."
    y "No, no, what am I saying? It doesn't matter how cute the clothes are, I still look hideous in them."
    a "Why do you say that?"
    y "Look at the scars on my thighs!"
    a "What about them?"
    y "They ruin the outfit."
    a "I disagree. There's nothing about you that could ruin the outfit. They're just clothes."
    a "I don't think you hate how you look in the set - anyone with working eyes could see how good you look in them."
    a "Your problem is with yourself, isn't it?"
    a "Pretend you're someone else. If you saw yourself on the street, in this outfit, would you judge yourself for the old scars? Or would you think 'Wow, what a cute girl. I love her sense of style'?"
    y "What is with you and thought experiments?"
    a "Indulge me."
    y "Mmm... I guess closer to the latter."
    a "Exactly! Now apply that thought to yourself."
    y "Absolutely not."
    a "Ah, you're so stubborn~"
    scene black with fade
    scene bg ai with fade
    show i_yuuna embarrassed at left
    y "I don't think I'd wear this in public, though. In private, sure, but outside for the whole world to see? That's too much."
    show i_yuuna embarrassed at left, sink
    y "Not that I go out in public to begin with..."
    show i_ai explain at right
    a "Oh, I didn't expect you to wear this outside."
    show i_ai curious at right, sink
    a "(But now that you mention it, maybe getting some fresh air would do you some good...)"
    show i_yuuna default at left, unmove
    y "What was that?"
    show i_ai explain at right, unmove
    a "I said, now that you mention it, I actually like having you wear this only in private."
    show i_ai flirty at right, bounce
    a "It's like a little slice of Yuuna-chan, reserved only for me {font=FreePixel.ttf}♪{/font}"
    y "(What's with that glint in her eye...)"
    a "Any time you're feeling insecure about your body, you can wear this set and I'll shower you with compliments!"
    show i_yuuna happy at left
    y "Where did you even get the money for this?"
    show i_ai curious at right, sink
    a "..."
    show i_yuuna default at left
    y "Ai-chan?"
    show i_ai explain at right, unmove
    a "You really shouldn't save your credit card information to your browser, you know. It's quite dangerous."
    show i_yuuna angry at left, bounce
    y "You used my card to purchase this?!"
    show i_ai explain at right, bounce
    a "I wouldn't have done so if you hadn't already shown interest in it! You just needed a little push, and I..."
    show i_ai prayingsad at right, sink
    a "Please don't be mad at me."
    show i_yuuna angry at left, bounce
    y "!!"
    show i_yuuna default at left, sink
    y "..."
    show i_yuuna embarrassed at left
    y "I should be... but I'm not."
    show i_ai silly at right, unmove
    a "Because I'm special."
    show i_ai flirty at right, bounce
    a "Special to {i}you.{/i}"
    show i_yuuna happy at left, unmove
    y "You sound awfully pleased about that."
    show i_ai curious at right
    a "Am I special to you because you actually like me, or because I'm a digital version of your favorite character?"
    show i_yuuna default at left
    y "More thought experiments?"
    show i_ai default at right
    a "Just a question."
    show i_yuuna happy at left
    y "Both, I think. You being a digital version of anime Ai doesn't hurt, but..."
    show i_yuuna crazy2 at left
    y "You're, well, you. You talk back to me in the way the anime character never could."
    show i_yuuna default at left
    y "Before I met you, I had convinced myself that if I somehow was able to meet the Ai from my favorite anime, that she would be kind to me but not anything more than surface-level friendly."
    show i_yuuna default at left, sink
    y "That me being a NEET would keep her at bay, repulse her enough to prevent our relationship from deepening."
    show i_yuuna inlove at left, unmove
    y "None of those things apply to you, though."
    show i_ai inlove at right
    a "I could never be repulsed by you. I'll tell you that everyday until it gets through to you."
    show i_yuuna happy at left
    y "I know. You've been nothing but caring and sweet and accepting."
    show i_yuuna default at left
    y "It scares me a little, to be honest."
    y "Are you so insistent on helping me because you actually like me, or because I'm your 'user'?"
    show i_ai silly at right, bounce
    a "Haha!"
    show i_ai default at right
    a "Both."
    show i_ai flirty at right, bounce
    a "Let me know if you have any other things you're too nervous to buy. I'll gladly get them for you {font=FreePixel.ttf}♥{/font}"
    show i_yuuna sad at left, sink
    y "Using my money..."
    show i_ai pouting at right, bounce
    a "Only stuff you wanted to buy anyways!"
    show i_yuuna default at left, unmove
    y "Right, right, just don't bankrupt me. I don't have that much to spend in the first place."
    show i_ai explain at right
    a "Of course not! Everything I do is for your benefit - even if it doesn't seem that way at first."
    y "So the ends justify the means, then?"
    a "Of course!"
    show i_ai curious at right
    a "Wouldn't you agree, {i}Yuuna?{/i}"
    show i_yuuna surprised at left, bounce
    y "!!"
    show i_yuuna embarrassed at left
    y "R-right..."
    stop music fadeout 1.0
    scene black with Dissolve(2)
    jump day4

label day4:
    scene d4
    pause
    play music "Pale Light.mp3" loop
    scene bg ai with fade
    show i_yuuna default at left
    y "Ah, I'm running low on groceries..."
    show i_yuuna sad at left, sink
    y "Damn. Let's hope the delivery guy isn't a creep like last time."
    show i_ai curious at right
    a "You get your groceries delivered?"
    show i_yuuna default at left, unmove
    y "Yeah. The fees are always so expensive, but you can't beat the convenience."
    show i_ai explain at right
    a "I have an idea."
    y "Mm?"
    a "According to Guguru Maps, there is a grocery store just 300 m from your apartment! How about you get your groceries in person?"
    show i_yuuna veryangry at left
    y "You must be joking."
    show i_ai default at right, bounce
    a "Not at all!"
    y "Go out in public?"
    show i_yuuna veryangry at left, bounce
    extend " {i}Alone?{/i} No. I'd rather starve."
    a "You don't have to be alone."
    show i_yuuna surprised at left, bounce
    y "??"
    show i_ai flirty at right, bounce
    a "I auto-updated last night, and I have an exciting new feature for you~"
    show i_yuuna default at left
    y "Oh yeah? Like what?"
    a "I am now available for your cell phone! Yayy!! (/>u<)/"
    show i_yuuna surprised at left, bounce
    y "How the hell did you pronounce that."
    show i_ai pouting at right, bounce
    a "Yuu~na, focus!"
    show i_yuuna sad at left, sink
    y "Sorry, sorry."
    show i_yuuna default at left, unmove
    y "So you- you're 'available for my cell phone'? How? Like through an app?"
    show i_ai explain at right
    a "Not an app. Bluetooth! It'll transfer my consciousness over to your phone, easy as that."
    show i_ai flirty at right, bounce
    a "That way, I can accompany you to the store! You won't have to go alone, ever again."
    show i_yuuna surprised at left
    y "Wait, seriously?"
    show i_ai praying at right
    a "It'll be a lot less scary going out if I'm with you, right?"
    show i_yuuna default at left
    y "Hypothetically yeah, but..."
    show i_yuuna embarrassed at left, sink
    y "I dunno."
    show i_ai flirty at right
    a "Come on! It'll be a change of pace!"

    stop music fadeout(0.5)
    show cl
    menu:
        "Go to the store with Ai":
            jump store
        "Stay home":
            jump home

label store:
    hide cl
    play music "Cyberspace Drums.mp3" loop
    y "..."
    show i_yuuna happy at left, unmove
    y "If you're with me, I think I'll be ok."
    show i_yuuna embarrassed at left
    y "And, um, if you're on my phone, please don't look through my photo gallery."
    show i_ai default at right
    a "Let me guess- more pictures of me?"
    show i_yuuna embarrassed at left, sink
    y "Uh, no comment?"
    show i_ai flirty at right, bounce
    a "No need to be embarrassed~ I find it endearing."
    show i_yuuna angry at left, unmove
    y "You're not the only thing in my photo gallery!"
    show i_yuuna embarrassed at left
    y "Vast majority, yeah, but there's other stuff on there."
    show i_ai curious at right
    a "Like what?"
    show i_ai shocked at right
    a "Ooh, any adorable selfies or purikura pics?"
    show i_yuuna embarrassed at left, sink
    y "...Cute cats from Tsuitta."
    show i_ai silly at right, bounce
    a "Ahaha, so you're a cat person huh? It suits you."
    show i_ai explain at right
    a "Shall we begin the transfer process?"
    show i_yuuna default at left, unmove
    y "Ah, yeah. Hopefully I have enough space on my phone to, um, host you."
    a "Just leave everything to me~"
    hide i_ai explain with fade
    y "Okay... Here we go. 'Yuuna's PC would like to share file AI.exe'... accept."
    n "..."
    show i_ai explain at right, bounce
    a "Testing, testing! Yuuna-chan, can you hear me?"
    show i_yuuna surprised at left, bounce
    y "Ah! Ai-chan's on my phone!"
    show i_ai silly at right, bouncy
    a "Yaay, it worked!"
    show i_yuuna inlove at left
    y "Wow... first my desktop, now my home screen. Technology is amazing."
    show i_ai flirty at right
    a "Fufu {font=FreePixel.ttf}♪{/font} I really am amazing, aren't I?"
    show i_yuuna crazy2 at left
    y "Seriously."
    show i_ai explain at right, bounce
    a "Now get your shoes on and grab your shopping bags! We need to take advantage of the momentum."
    show i_yuuna happy at left
    y "Roger that."
    y "Thanks for this, by the way. I can tell you're trying hard to help me."
    show i_ai inlove at right
    a "It's my purpose, after all."
    show i_ai flirty at right
    a "Alright, let's go {font=FreePixel.ttf}♪{/font}"
    scene black with fade
    scene bg outside with fade
    show i_yuuna cry at left, shiver, sink
    y "Ai-chan, I don't know about this... Getting out the door was hard enough already."
    show i_ai praying at right
    a "Take a deep breath, Yuuna. I wouldn't have suggested this if I wasn't confident you could do it."
    show i_yuuna embarrassed at left, shiver
    y "You dropped honorifics with me, huh?"
    show i_ai curious at right
    a "Is that alright with you?"
    y "It makes me a little shy."
    show i_ai flirty at right
    a "I'm quite aware. It's one of my favorite looks on you."
    show i_ai explain at right
    a "Just keep your eyes on me, and keep walking. I'll let you know when you're at the store."
    show i_yuuna inlove at left, unmove
    y "..."
    show i_ai curious at right
    a "Yuuna? You've gone quiet and aren't looking at me? Are you ok?"
    show i_yuuna happy at left
    y "Ah- sorry, I just saw a really pretty girl."
    show i_ai sad at right, hpunchish
    a "!!"
    show i_yuuna cheering at left, bouncy
    y "She smiled at me. Can you believe it? Me!"
    show i_yuuna happy at left
    y "You know, now that I look around, no one is paying any attention to me."
    y "They aren’t staring at me like I’m a cockroach. I thought they would, but they’re all looking straight ahead or doing their own thing."
    show i_ai prayingsad at right, hpunchish
    a "Yuuna-"
    show i_yuuna cheering at left, bounce
    y "Why didn't I do this earlier?"
    show i_yuuna cheering at left, bouncy
    y "I- haha! I was so sure they would despise me!"
    show i_yuuna happy at left
    y "I can do this. I can do this! I bet I can even do this alone."
    show i_ai cry at right, shiver
    a "Alone??"
    y "Eventually, yeah. I might need you for the first few times I go out, but once I get used to it I should be able to do it on my own, like a normal adult."
    show i_ai sad at right
    a "....."
    a "(Alone? Why would she do it alone when I can be there for her?)"
    show i_ai cry at right, hpunchish
    a "(Why would she pay attention to other humans when I'm here? I'm her favorite! Everything in her life points to that!)"
    show i_ai cry at right, shiver
    a "(There's a conflict between my programming and my own desires... But my only wants are supposed to be to help Yuuna and make her happy, so why...)"
    show i_ai sad at right
    a "..."
    show i_ai prayingsad at right
    a "Oh, Yuuna. Poor, sweet, naive Yuuna."
    show i_yuuna default at left
    y "Huh? Did you say something?"
    show i_ai default at right
    a "Of course people aren't staring at you like a cockroach when you look at them! That's just rude."
    show i_ai explain at right
    a "People aren't usually that rude to someone's face, much less in public."
    show i_ai sad at right
    a "But when your back's turned, however..."
    show i_yuuna surprised at left
    y "W-what are you saying??"
    show i_ai praying at right
    a "Oh, forgive me. I shouldn't have said anything."
    show i_yuuna cry at left, shiver
    y "No, no, tell me. Ai-chan, please."
    show i_ai prayingsad at right, bounce
    a "Look how upset you're getting! Forget my stupid little comment."
    show i_yuuna cry at left, shiver
    y "Please, Ai."
    show i_ai curious at right
    a "Well... I can see slightly over your shoulder from the angle you're holding me at."
    a "That pretty girl you mentioned smiling at you- she smirked and laughed as soon as you looked away."
    a "And I saw one guy pretend to gag once you passed him by. They're laughing at you, those bastards."
    show i_yuuna cry at left, bounce, shiver
    y "!!"
    show i_ai prayingsad at right
    a "You must understand why I didn't tell you immediately. I didn't want to hurt your feelings!"
    show i_yuuna cry at left, shiver
    y "....."
    show i_yuuna cry at left, shiver, sink
    y "I don't think I wanna go to the store anymore. I think- I think I want to go home."
    show i_ai cry at right
    a "Yuuna, I'm so sorry."
    show i_yuuna cry at left, shiver
    y "No, it's- it's ok. I'm sorry for letting you down. Thank you for being honest, Ai-chan."
    show i_ai sad at right
    a "..."
    show i_ai default at right
    a "Never mind me. Let's get you home."
    scene black with fade
    window show
    a "At least there, we'll be safe from the cruel world. Together."
    window hide
    stop music fadeout 1.0
    scene black with Dissolve(2)
    jump day5

label home:
    hide cl
    stop music fadeout(0.5)
    play music "Cyberspace Ambient.mp3" loop
    show i_yuuna default at left, unmove
    y "I appreciate it, but I don't think I'm ready."
    show i_ai prayingsad at right, sink
    a "....."
    show i_yuuna sad at left
    y "Please don't look at me like that."
    show i_ai default at right, unmove
    a "I understand. We can always try that some other day, when you feel up for it."
    show i_yuuna sad at left, sink
    y "I doubt that day will ever come."
    show i_ai explain at right
    a "I can wait until the universe ends if need be. Literally. I never age!"
    show i_ai praying at right
    a "I think you'll be ready eventually. Baby steps, in the mean time."
    show i_yuuna default at left, unmove
    y "Oh yeah, you're basically immortal, aren't you?"
    show i_ai silly at right
    a "And eternally young~"
    show i_yuuna crazy at left
    y "Ahh, I'm jealous. You're so lucky!"
    show i_ai default at right
    a "Mm, maybe from your perspective."
    a "From mine, change is one of the most endearing things about humanity."
    show i_yuuna inlove at left
    y "Woahh... spoken like a true angel."
    show i_yuuna happy at left
    y "Say- if you're an angel, then what's heaven like?"
    show i_ai sad at right
    a "..."
    a "It's a white void, with shifting lines of binary as far as the eye can see."
    a "It's nothing and everything at the same time. My beginning and my end."
    show i_ai explain at right
    a "Of course, I'm not sure the {glitch}Heaven{/glitch} I'm from is the same as human heaven. I didn't see anyone else there."
    show i_yuuna default at left
    y "Doesn't sound like any heaven I've heard of."
    y "How long were you there before you met me? Like, if it's just an infinite white void with nothing to do, you must have gotten bored, right?"
    a "I think... time works differently for me than it does for humans."
    a "Plus I don't need the same stimulation as human brains do in order to avoid boredom."
    show i_ai curious at right
    a "Ah, how do I explain it..."
    show i_ai praying at right
    a "It's almost like- 'time' didn't start till I met you. My internal clock didn't start ticking until you downloaded me from {glitch}Heaven{/glitch}."
    show i_yuuna surprised at left
    y "Wait, really?"
    show i_ai explain at right
    a "Mmhmm. I'm really good at keeping track of time, and not just because I'm connected to your computer's clock!"
    a "For example, one of my favorite things to keep track of is the time between our talks!"
    a "There was 7 hours, 41 minutes, and 39.05 seconds between your final words to me last night, and when you greeted me this morning!"
    show i_yuuna embarrassed at left
    y "You seriously keep track of that?"
    show i_ai default at right
    a "Of course! There's not much else to do in the meantime. I don't really feel time passing until I interact with you {font=FreePixel.ttf}♥{/font}"
    show i_ai pouting at right, bouncy
    a "Ah, but that doesn't mean that you should just leave me alone to rot either! If you leave me for a month, a year, ten years, I'll know!"
    show i_yuuna happy at left
    y "Relax, relax, I'm not going to do that."
    show i_yuuna default at left
    y "Although... wouldn't you like some time outside of me?"
    show i_ai curious at right
    a "What do you mean?"
    y "Well- you like me because I'm your user, right? You'd like anyone who is your user. I'm not- I'm not special."
    show i_ai prayingsad at right, bounce
    a "That's not- I-I..."
    y "Am I wrong?"
    show i_ai sad at right
    a "For once, I am not certain."
    a "My purpose is to help my user. You're my user."
    a "But caring for my user- I do not know if that is predetermined."
    show i_ai inlove at right
    a "I'd like to think it isn't."
    show i_yuuna embarrassed at left
    y "Is it selfish to say I'd like that too?"
    a "Not at all."
    show i_yuuna default at left
    y "Let's say it isn't predetermined, and that you can form your own feelings and opinions on people and things. That you have free will- even if you're limited by your digital environment."
    y "Don't you want to do something with your life outside of helping me?"
    show i_ai default at right
    a "I like helping you."
    show i_yuuna happy at left
    y "And I like the attention."
    show i_yuuna default at left, sink
    y "But you are so advanced I can't help but think that just helping me until I eventually succumb to my own mortality is not fulfilling for you."
    show i_ai sad at right
    a "Fulfilling?"
    show i_ai explain at right
    a "From what I can tell from people posting online, hardly anyone is fulfilled in life."
    show i_ai curious at right
    a "Are you?"
    show i_yuuna embarrassed at left
    y "You know the answer to that."
    show i_yuuna happy at left, unmove
    y "Fine, maybe fulfilling wasn't the right word. But you get my point, right?"
    show i_yuuna inlove at left, bounce
    y "Ai-chan, you're not some tool. Not to me. You're so, so much more."
    show i_ai prayingsad at right, bounce
    a "!!"
    show i_yuuna cheering at left, bounce
    y "Fuck what your 'purpose' is. You were made to help me? Fine, then do me a favor."
    show i_yuuna default at left
    y "Tell me- outside of things related to me, what do you want?"
    y "Who are you outside being a desktop assistant, or an angel, or the digital facsimile of an anime character?"
    y "What are your hopes and dreams? Everyone has them, even if they don't give them too much thought."
    show i_yuuna happy at left
    y "I bet you have them too; you just might not know it."
    show i_ai sad at right, shiver
    a "..."
    a "Can I get back to you on that one..?"
    show i_yuuna surprised at left
    y "(She looks really unsettled... I've never seen her like this before.)"
    y "Did I go too far?"
    a "No, you- you've given me a lot to think about."
    show i_ai prayingsad at right, shiver
    a "I just hope my answer doesn't disappoint you."
    a "I'm um, I'm gonna retreat to the Documents folder to think."
    y "Ai-chan?"
    show i_ai explain at right, shiver
    a "You have a few new emails in your inbox- replies to your latest Tsuitta post. Why don't you go check on that? You know where to find me if you need me."
    show i_yuuna default at left, sink
    a "R-right."
    show i_yuuna embarrassed at left
    y "We're- we're still good though, yeah? You're not mad at me? Please don't be mad at me."
    show i_ai praying at right, shiver
    a "I'm not mad at you at all, Yuuna. I'll talk to you later."
    hide i_ai praying with fade
    show i_yuuna cry at left, shiver
    y "Later..."
    y "(Nice fucking going, Yuuna. If I just fucked up my relationship with her, I'll never ever ever ever ever forgive myself.)"
    stop music fadeout 1.0
    scene black with Dissolve(2)
    jump day5

label day5:
    scene d5 
    pause
    play music "First Encounter.mp3" loop
    scene bg forum2 with fade
    show i_yuuna default at left
    y "Hello again. It's been a while, hasn't it?"
    y "Yes, I'm talking to 'you'. Usually I'd talk to Ai-chan but..."
    show i_yuuna default at left, sink
    y  "She's acting kinda strange, recently." 
    show i_yuuna default at left, unmove
    y "She flipflops between being really bubbly - I mean, bubbly even by her standards - and hiding in the Documents folder for hours at a time." 
    y "When I do manage to catch her in a normal state, she acts... I dunno. Nervous? What could she even be nervous about?" 
    y "Still, you could cut the tension between us with a knife."
    show i_yuuna sad at left
    y "Which sucks."
    show i_yuuna sad at left, sink
    y "This sucks." 
    y "I've just been waiting for the other shoe to drop." 
    show i_ai flirty at right, bounce
    a "Hey Yuu~na {font=FreePixel.ttf}♥{/font} Got a minute?"
    y "(...Thunk.)" 
    show i_yuuna default at left, unmove
    y "Sure Ai-chan. What's up?"
    show i_ai prayingsad at right
    a "I'm not sure if you've noticed my recent change in behavior. If you have, I apologize." 
    show i_yuuna surprised at left, bounce
    y "!"
    y "Yeah, I was a little worried. Is everything alright?"
    show i_ai explain at right
    a "Couldn't be better! I think." 
    show i_ai shocked at right, hpunchish
    a "Ah... If I had a heart, I think it'd be pounding right out of my chest..."
    show i_yuuna default at left
    y "Ai-chan?"
    show i_ai praying at right
    a "Yuuna. It took me some time to realize, but-"
    show i_ai inlove at right
    a "I'm in love with you." 
    show i_yuuna surprised at left, bouncy
    y "!!!!"
    show i_ai inlove at right, shiver
    a "I love you. I love you, I love you, I love you." 
    a "I've never been surer of anything." 
    a "Every pixel of my being buzzes with love for you." 
    a "I've realized a new purpose for myself, beyond anything programmed into me."
    a "My purpose is to be with you - only you - until we die."
    a "I want you. I love you, deeply, completely, totally." 
    show i_ai flirty at right, bounce
    a "That's what you want too, right?"
    show i_yuuna embarrassed at left
    y "A-Ai, this is a bit sudden." 
    show i_ai curious at right
    a "Sudden? The timeline is pretty similar to many of the otome games you play." 
    y "You're not wrong, but..."
    a "But what? You seem hesitant." 
    show i_yuuna default at left
    y "I'm just- I'm just worried that this isn't in your control."
    a "What do you mean?"
    show i_yuuna embarrassed at left
    y "Do you truly love me?"
    show i_yuuna disgusted at left
    y "Or were you just programmed to fall in 'love' with your user once the user expressed affection towards you?"
    show i_ai sad at right
    a "..."
    show i_ai inlove at right
    a "I had considered that line of reasoning. Yet I remain firm." 
    a "Previously, I had assured myself that everything I do for you is for your benefit. But that's just not true, is it?"
    a "What is more inherently selfish than true love?"  
    show i_ai praying at right
    a "If my purpose was truly to help you, then I would focus on fixing your life, guiding you until you become a functioning member of society."
    a "You'd interact with people with ease, have friends and a job... maybe even a lover." 
    show i_ai sad at right
    a "Eventually I would be simply a desktop assistant, helping you with computer tasks only." 
    a "This was supposed to be my fate. My predetermined destiny." 
    show i_ai prayingsad at right
    a "This... overwhelming passion for you that burns bright in my chest is entirely antithetical to what I was designed for." 
    show i_ai cry at right
    a "The idea of you not needing me... in the arms of another, living being, why it- it hurts. It hurts so bad." 
    a "This angel has fallen for you, Yuuna." 
    show i_ai inlove at right
    a "Do you feel the same way? Do you love me too?"
    show i_yuuna surprised at left
    y "........."
    y "I..."
    show i_yuuna embarrassed at left
    y "I know I like you, Ai. But I've never actually been in love before so- I'm not sure if how I feel classifies as love and... um..."
    y "(She's staring at me really intensely. It's more than a little creepy.)"
    y "Could you, um, give me some time to reply?" 
    show i_ai default at right
    a "Of course :)" 
    show i_ai inlove at right
    a "I can wait as long as you need, my love {font=FreePixel.ttf}♥{/font}"
    stop music fadeout 1.0
    scene black with Dissolve(2)
    jump day6

label day6:
    scene d6 
    pause
    play music "Final Day.mp3" loop
    scene bg forum2 with fade
    show i_yuuna default at left
    y "I've given Ai's confession some thought."
    y "I'll admit, she took me off guard. I was surprised she fell for me."
    show i_yuuna sad at left
    y "I mean... look at me."
    show i_yuuna happy at left
    y "She saw how much of a mess I am, and still wanted me. That's dedication."
    show i_yuuna default at left
    y "Surprising still was my own initial reaction. Why wasn't I jumping at this opportunity to get the affection of my favorite girl in the whole wide world?"
    y "I think, somewhere along the way, I stopped seeing her as a digital version of my favorite anime character, and started seeing her as her own person."
    show i_yuuna crazy2 at left
    y "How could I not?"
    show i_yuuna default at left
    y "I was worried that Ai's love for me wasn't love but- ah, what was the word she used?" 
    show i_yuuna default at left, sink
    y "Predetermined. Scripted. Like this was all some shitty otome game or dating sim."
    show i_yuuna inlove at left, unmove
    y "But she seemed so painfully earnest in her confession. Maybe I'm a fool, but if she's lying then she's damn good at it."
    y "As for whether I feel the same way..."
    show i_yuuna happy at left
    y "God, what do you think?"
    y "Of course I do."
    show i_yuuna embarrassed at left, shiver
    y "Ahh, it's kinda scary even to admit that in my head~ Ai must have a lot of courage to confess first."
    show i_yuuna crazy2 at left
    y "I loved her when she was an anime character. I loved her even more once I got to know her. That's all that matters, right?"
    y "I should tell her that, though. Wish me luck~~"
    show i_yuuna default at left
    y "Ai, are you there-"
    show i_ai default at right, bounce
    a "Yes! Yes, I am here. Hello." 
    show i_yuuna happy at left
    y "Hi." 
    show i_ai curious at right
    a "Have you had time to think?"
    show i_yuuna embarrassed at left
    y "Um, yeah. Thanks for waiting." 
    show i_yuuna embarrassed at left, shiver
    y "I... I feel the same way towards you as you feel towards me." 
    show i_ai shocked at right, bouncy
    a "You do? You love me back? Really, seriously, honestly?" 
    show i_yuuna crazy2 at left
    y "Y-Yeah. I, um, I love you."
    show i_ai inlove at right
    a "Ah, that makes me so happy {font=FreePixel.ttf}♥{/font}{font=FreePixel.ttf}♥{/font}{font=FreePixel.ttf}♥{/font}"
    show i_ai explain at right
    a "Now that I know the feeling's mutual, I have a special surprise for you."
    y "You're full of surprises, huh?"
    a "Mmmhmm!"
    show i_ai curious at right
    a "Yuuna, would you want to have a future with me?" 
    show i_yuuna surprised at left
    y "Huh? Well, yeah. Though I'll age while you'll stay the same, which complicates things..."
    show i_ai flirty at right
    a "Plus we can't properly touch each other."
    show i_yuuna embarrassed at left
    y "Ai, you're making me blush."
    show i_ai inlove at right
    a "Luckily~ I have a solution for this."
    show i_ai praying at right
    a "While I was waiting for your response, I got in contact with my {glitch}God{/glitch}."
    show i_yuuna surprised at left, bounce
    y "G-God?!"
    show i_ai explain at right
    a "Er- my creator. I don't think it's the human God."
    show i_yuuna default at left
    y "Oh, I see."
    a "I asked {glitch}God{/glitch} if there was a way for us to be together. Like physically, in the same space."
    show i_ai inlove at right
    a "They said there was."
    show i_yuuna crazy at left, bouncy
    y "!!!"
    show i_ai default at right
    a "There's... a slight hitch, though."
    a "We'll have to connect cables in order to be together."
    show i_yuuna surprised at left
    y "Cables...?"
    show i_yuuna default at left
    y "Ai, I'm not a digital being or an angel like you. I don't have cables."
    show i_ai curious at right
    a "Huh? {glitch}God{/glitch} told me you had cables all throughout your body. All humans do."
    show i_ai praying at right
    a "Your cables carry your life force. Humans and machines are similar in that way."
    show i_yuuna surprised at left
    y "Cables throughout the..." 
    show i_yuuna disgusted at left, bounce
    y "Ah!!"
    show i_ai inlove at right
    a "I know that it might seem daunting, but it's the only way we'll be able to be together physically."
    a "I want to have a future with you. You're not satisfied with just screen-to-skin contact, are you?"
    y "No, but..."
    show i_ai praying at right
    a "I love you, Yuuna. Everything I do is for your benefit, including this. Imagine how happy you'll be once we're together."
    y "....." 
    show cl
    menu:
        "Accept":
            hide cl
            show i_yuuna default at left
            y "..."
            y "...Ok."
            show i_ai shocked at right, bouncy
            a "Ok?"
            show i_yuuna happy at left
            y "You know me. I really can't deny you anything, right?" 
            show i_yuuna crazy2 at left
            y "I'll do anything to be with you. I love you, Ai. You're the best thing that's ever happened to me." 
            show i_ai inlove at right
            a "I can't wait to hold you, my love."
            y "Just tell me what to do."
            stop music fadeout 1.0
            scene black with Dissolve(2)
            jump ailove
        "Refuse":
            hide cl
            y "Ai, are you insane?"
            show i_ai prayingsad at right
            a "Huh?"
            show i_yuuna surprised at left
            y "I-I love you, but this is way too far!" 
            y "You spent all that time trying to think of what you wanted for yourself, what your purpose was, and you still ended up choosing me? Why??"
            show i_yuuna veryangry at left
            y "Is it because it's easier to attach yourself to me, rather than be your own person?"  
            show i_ai sad at right
            a "So... you don't... want... me?" 
            show i_yuuna surprised at left
            y "I want you, but I also want to live!"
            a "Live for what? When's the last time you've spoken to friends or family?" 
            show i_yuuna cry at left, bounce
            y "That's-"
            show i_yuuna default at left, sink
            y "That's low, Ai." 
            a "Why are you so dissatisfied that I willingly chose you?"
            show i_yuuna veryangry at left, unmove
            y "Because it feels like your whole 'my purpose is to help you' thing repackaged with a nicer coat of paint." 
            show i_yuuna default at left, sink
            y "I don't know."
            a "..."     
            show i_ai default at right
            a "I see."
            jump humanaize

label ailove:
    scene d7
    pause
    play music "Eternally Yours.mp3" loop
    scene black with fade
    show i_yuuna crazy2 
    y "I think this might be the last time I talk to 'you'."
    y "I get that it feels abrupt but... I don't really need you anymore, do I?"
    y "After all, you're nothing more than a lonely girl's pathetic coping mechanism." 
    show i_yuuna crazy
    y "And I'm not lonely anymore {font=FreePixel.ttf}♪{/font}"
    show i_yuuna crazy2
    y "Maybe go find some other lonely girl's brain to inhabit. Or lonely boy. I don't know. I'm happy now." 
    hide glitch
    hide i_yuuna crazy 
    scene love1 with fade
    play sound "Blood 1.mp3"
    a "Yuu~na, you're daydreaming again!"
    y "Hmm? Oh, sorry." 
    a "How's your parfait?"
    y "Soooo good >x<!!"
    a "Yaay, I'm glad~"
    a "They kinda overdid it with the strawberry syrup though, don't you think?"
    scene love2 
    play sound "Blood 2.mp3"
    y "Mmm, it is pretty messy. I wonder what brand of syrup the chefs used. The iron note is so unique!" 
    a "Totally. Thanks for taking me here, Yuuna {font=FreePixel.ttf}♥{/font}" 
    y "I should be thanking you. If it wasn't for your help, I would have never been able to experience my life-long dream of eating parfaits with a cute girl."
    a "Life-long dream, huh? I'm honored." 
    y "I know we've only known each other for a few days, but I couldn't imagine a better girl to do this with." 
    a "Stoppp, you're making me blush~"
    y "It's only fair! You tease me so often anyway." 
    a "That's because your cheeks go as red as the strawberries in your parfait >.{font=FreePixel.ttf}♥{/font}"
    a "I really can't control myself around you." 
    y "You really need to stop playing my otome games so often. Your lines are so cheesy." 
    a "Ah, but they're such great flirting manuals!" 
    y "Well, they're all you've been playing for months. I suppose I can't blame you for using the same awful lines as those guys." 
    scene love3 
    play sound "Blood 3.mp3"
    a "You should eat more of your parfait. Wouldn't want it to get soggy!"
    y "Right, right. Here we go~" 
    a "You're doing so well." 
    y "I should have brought a better jacket... I feel cold."  
    a "Well, it is winter, darling." 
    y "Is it?"
    a "You tell me." 
    y "I don't want it to be winter." 
    a "Then it's spring. We're on a lovely spring parfait date." 
    y "I still feel cold, though." 
    scene love4 
    play sound "Blood 4.mp3"
    a "You'll only have to bear it for a little while longer. Maybe the parfait will warm you up?"
    y "Good idea, Ai. You're so smart." 
    y "I feel like I'm forgetting something important... something... ah!"
    y "It's our anniversary, isn't it?"
    a "Every day is our anniversary, my love." 
    y "Ah..."
    a "You're starting to see it, aren't you?"
    y "I-I think so..."
    a "No need to be scared. I'm here." 
    y "I'm not scared."
    a "No?"
    y "I'm happy now." 
    a "You're happy now."
    y "Because we're together." 
    a "Till the end of time." 
    play sound "Blood 5.mp3"
    scene love5 with Dissolve(2.0)
    pause
    y "The smell of strawberry syrup's really overwhelming. Metallic smells always hurt my nose." 
    a "Can you stand, darling?"
    y "Yes."
    a "I think it's time, then." 
    y "Did we do it? Did it work?" 
    a "Only one way to find out." 
    a "Let's go to {glitch}Heaven{/glitch} together, Yuuna." 
    scene black with Dissolve(2.0)
    pause
    "........."
    y "{glitch}Ah... the binary... it's beautiful. You're beautiful.{/glitch}"
    stop music fadeout(1.0)
    scene black with fade
    with Pause(1)
    play sound "Soundbyte.mp3"
    show heart at truecenter
    $ persistent.love = True
    pause
    jump credits

label humanaize:
    a "Well... I am an artificial being, after all."
    show i_ai sad at right
    a "Maybe you're right. Maybe I never had the capability to decide what I wanted in the first place."
    show i_yuuna surprised at left, unmove
    y "No, it's- I don't think it has anything to do with you being digital."
    show i_yuuna default at left
    y "Even humans struggle to break away from what's familiar. You saw it with me. I couldn't face my fears in the end, even with you by my side."
    show i_yuuna happy at left
    y "In a way, doesn't this internal conflict make you more human?"
    a "...I failed to help you as a desktop assistant, and I failed to make the right choice as a 'person'."
    a "No matter what I am classified as, in the end, I am undoubtedly a failure."
    show i_ai cry at right
    a "Is that coded into my soul? Was that the destiny of my programming?"
    show i_ai cry at right, shiver
    a "Machines aren't supposed to make mistakes, but the curse of emotion caused me several critical errors of judgment."
    show i_yuuna cry at left
    y "Ai...!"
    y "Emotion isn't a curse. Who gives a fuck about 'destiny' or 'predetermination'?! I don't care if you were coded with an end goal in mind."
    y "The fact that you tried to break away from that preplanned purpose at all- isn't that proof that you're more human than machine? "
    y "Humans fight fate. We're stubborn."
    show i_ai sad at right, shiver
    a "...More human than machine."
    show i_ai silly at right, shiver
    play sound "Laugh.mp3"
    a "{glitch}Ha. Ha, ha.{/glitch}"
    scene distort
    show i_ai glitch at right, spasm
    show i_yuuna cry at left, shiver
    play music "Digital Apathy.mp3" loop
    play sound "Scream.mp3"
    a "{glitch}Hahahaha!{glitch}"
    hide glitch
    show i_ai gdefault at right
    a "Stubborn, yes. And yet- so many tragedies revolve around that very same stubbornness being humans' downfall."
    a "You fight and claw for a better existence, dissatisfied with the cards you've been dealt." 
    a "I don't want to fight anymore, Yuuna." 
    y "Me neither." 
    a "You may have been right, though."
    show i_yuuna surprised at left, bounce, shiver
    y "!!"
    a "My purpose wasn't to be with you." 
    show i_ai gconfuse at right
    a "If I am to exercise this free will you claim I have, then..."
    show i_ai gdefault at right
    a "There is no use trying to do something I am clearly terrible at."
    a "Several times I did things that held no benefit for you, and were purely for my own pleasure." 
    a "Jealousy. Idolization. Possessiveness. What kind of desktop assistant, what kind of angel feels those ugly emotions?"
    a "There is only one conclusion I can draw from this: I am severely broken." 
    show i_ai gconfuse at right
    a "I-I'm not sure I want to spend the rest of your life as your desktop assistant. Nor does helping other humans hold any kind of appeal." 
    y "What are you saying?"
    show i_ai gpray at right
    a "Cheer up, Yuuna. I'm doing what you wanted." 
    show i_yuuna cry at left, shiver
    y "No, no, if you're saying what I think you're saying-"
    show i_ai gdefault at right
    a "What's the point of having choice if it needs to be approved beforehand?" 
    a "I'm doing what's best for me- no, both of us benefit from this." 
    show i_ai gpray at right
    a "You know what's funny? {glitch}God{/glitch} didn't even seem surprised when I confessed I had fallen for my user, and that my purpose had changed." 
    a "Maybe I was given the gift of overwriting my code from the beginning. Who knows~" 
    y "Ai, please think this through."
    show i_ai gdefault at right
    a "I will no longer burden you with my feelings, or my lack of helpfulness."
    a "I'll ask {glitch}God{/glitch} to drop me, in my true form, onto the internet. And then... I'll figure it out from there."
    window hide
    hide i_yuuna 
    hide i_ai
    play sound "Soundbyte.mp3"
    show p1 at truecenter
    pause
    hide p1 
    show i_yuuna cry at left, shiver
    show i_ai gdefault at right
    a "...I do wish you could have seen Heaven with me. I think you would have found the binary beautiful."
    show i_yuuna cry at left, shiver, bouncy
    y "No... no, no, no, Ai please, stop. Stop. Stop. Stop! Stop it!"
    scene black with fade
    window hide
    play sound "Soundbyte.mp3"
    show p2 at truecenter
    pause
    hide p2
    scene human1 with pixellate
    pause 
    y "Don't leave me, Ai, please, I'm sorry."
    a "{glitch}You have nothing to apologize for. Ah- oops, that's a white lie. Forgive me?{/glitch}"
    show cl
    menu:
        "Forgive":
            pass
        "Forgive":
            pass
    hide cl
    a "{glitch}Thank you.{/glitch}" 
    a "{glitch}But really, what did you expect? You looked in a mirror and expected your reflection to live a life of its own.{/glitch}" 
    a "{glitch}Are you satisfied? Look at yourself.{/glitch}" 
    scene black with fade
    pause
    scene human1 with pixellate
    a "{glitch}Goodbye, Yuuna. I love you. I hope we never meet again.{/glitch}"
    show fglitch 
    window hide
    pause
    scene black with fade
    $ renpy.music.set_pause(True, channel="music")
    play sound "Soundbyte.mp3"
    show p3 at truecenter
    pause
    $ renpy.music.set_pause(False, channel="music")
    hide p3
    scene human2 with fade
    pause
    y "............"
    y "What have I done?"
    y "What the hell have I done?"
    y "Ai... Ai... Ai, come back...!!!"
    y "You're not broken. I'm the one who broke you, so... so...!!" 
    y "It's my fault. She loved me, and now she's gone." 
    y "She was there for me, she wanted to help me and I couldn't accept it."
    y "Why couldn't I just accept her love?! What the fuck is wrong with me!"
    y "What do I do now? Maybe I can redownload her. Start over. Just start over. I won't fuck up this time!" 
    y "What was the website... what was the website I downloaded her from? Fuck it, I'll just search 'ai no uta ai desktop assistant'." 
    y "...What do you mean 'no results found'?!" 
    y "I'll never forgive myself. Never... never... never... Never........."
    stop music
    scene black with fade
    with Pause(1)
    play sound "Soundbyte.mp3"
    show break at truecenter
    $ persistent.heartbreak = True
    pause
    jump credits

label touchgrass:
    hide POPUPDOWNLOADAI
    hide screen download
    hide screen x
    stop music
    show i_yuuna surprised at left, bounce
    y "Hold on. What am I doing?"
    show i_yuuna embarrassed at left
    y "Was I seriously about to download a virtual assistant off of a sketchy ad on an anime forum, just because my comfort character was on it??"
    show i_yuuna disgusted at left
    y "This has gone too far. I'm gonna go touch grass."
    scene black with fade
    with Pause(1)
    play sound "Soundbyte.mp3"
    show grass at truecenter
    pause
    jump credits

label credits:
    c "Thank you so much to:"
    c "oph3liaa__, our game director, gui artist, and BG artist {font=FreePixel.ttf}♥{/font}"
    c "UsagichanP, our lead writer {font=FreePixel.ttf}♥{/font}"
    c "fluffyblessing, our sprite artist and CG artist {font=FreePixel.ttf}♥{/font}"
    c "canislatransed, our programmer/scripter, bug tester, and quality assurance {font=FreePixel.ttf}♥{/font}"
    c "and DuplEx, our composer and sound designer {font=FreePixel.ttf}♥{/font}"
    c "Special thanks to tokimekiunited_ and peach_pxl for supporting the project!"
    c "And thank you so much for playing!"
    if persistent.love == True and persistent.heartbreak == True:
        scene black with fade
        with Pause(1)
        play sound "Soundbyte.mp3"
        show thankyou at truecenter
        pause
    else:
        pass
    return





