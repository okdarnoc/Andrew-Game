init python:
    preferences.language = None

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Andrew = Character("Andrew")
define Bartender = Character("Bartender")
define Anonymous = Character("Anonymous")
define Bouncer = Character("Bouncer")
define Lucifer = Character("Lucifer")
image bg bar ="bg bar.png"
image bg dark ="bg dark.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg dark with dissolve
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "People often say that money can't buy happiness. "
    "That life should be filled with experiences, instead of earthly possessions."
    "After all, said possessions cannot be taken with you into the afterlife."
    "Yet, for every word preached against materialistic desires…"
    "Those doomed to sail the River Styx had better enjoy themselves while they can."
    jump chapter1


label chapter1: 

    scene bg bar with dissolve
    play music "bar.wav"
    Bartender "Another round, Andrew?"  
    Andrew "I don't have anywhere to be."
    Bartender "Don't I know it."

    "I like this bar in particular." 
    "The music is calm, the patrons are well-behaved, and Bartender Rich certainly knows his cocktail recipes." 
    "It's strange to think that I've been coming here for years now."
    "Damn near three years must have gone by at this point."
    "Zzz Zzz"
    play sound "phonevibrate.wav"
    "I check my phone. Cassandar. Ignore."
   
    Bartender "You can't ignore her forever, Andrew."
    Andrew  "You wanna bet my next drink on that?"
    Bartender "...She's your wife. You want little Suzy growing up without a father?"
    Andrew "Please…"
    Andrew "(She already is...)"
    Bartender "Right, I'm cutting you off."
    Bartender "One more drink. What'll it be?"

    menu:
        "What will you drink?"
        
        "Something Strong.":
            Andrew "Something that'll make looking at your ugly mug a little easier.?"
            Bartender "Absinthe it is."
            "Rich moves to the cabinet and removes a dark green liquid."
            "He pours a fraction of the bottle into my glass and slides it down the bar."


        "Somwthing Mild.":
            Andrew "Nothing too strong. I don't want Cassandra to know I was here."
            Bartender "I'll make you something with vermouth, it's pretty herbal."
            Bartender "She'll think you've been sucking down green teas at a brothel all night long!"
            Andrew "What would I do without you…?"
    
    "I take the drink in my hand and choke it down. "
    "I can feel the alcohol coursing through my veins and into his cerebellum."
    "It may not be pretty—this life I've constructed for myself…"
    "But it definitely has its moments."

    Bartender "Are you planning on paying for your drinks this time?"
    Andrew "Can't you put it on my tab?"
    Bartender "If I put any more drinks on your tab, I'm going to have to open a second tab for your original tab!"
    "Zzz Zzz."
    play sound "phonevibrate.wav"

    Andrew "Hold that thought. It's my beloved wife, I have to take this."

    #Scene: Screen cuts to black#
    scene black
    "I lift my phone, ready to decline Cassandra's call."
    "However, only a message icon appears on the screen."
    "Anonymous: I want to save you."
    "Anonymous: Come to this address in fifteen minutes."
    "Anonymous: Should you fail to attend, we'll be sending these along to your wife."
    "Opening the attachment reveals the thousands I've accumulated in gambling debts."
    "With a casino right next door, an intoxicated Andrew can't help but squander what little money I have on a better future."
    "I suppose the reason I return day after day is to test my skill."
    "My high-highs have managed to knock significant chunks off my bar tab."
    "Unfortunately, my low-lows will soon return to bite me in the form of bankruptcy."
    "Anonymous: We're looking forward to meeting with you…"
    "Anonymous: Andrew."
    "Sweat begins to pour from my brow and back."
    "I check the time."
    "18:45."

    #Scene: Screen changes back to bar#
    scene bg bar with dissolve
    Andrew "Rich, I have to go!"
    "I grab my uniform and badge, rushing out of the door."
    Bartender "What about your drinks?!"
    Andrew "Put it on my tab!"

    #Scene: Pool Hall Interior#
    scene bg poolhall with dissolve
    Andrew "Excuse me, sir, I was told to meet someone here."
    Bouncer "You a cop?"
    "I hesitate."
    "My police badge is still in my pocket and my uniform is in my bag."
    Andrew "(I may be able to pass unnoticed.)" 

    menu:
        "What will you do?"
        
        "Lie":
            Andrew "Do I look like a cop to you?"
            Bouncer "Fair point. I ain't never seen no cop that reeks of booze as much as you do."
            Andrew "Well, I only had…"
            Bouncer "And look at your clothes! What, you can't afford to patch these up Mr.'Excuse Me, Sir'?"
            Andrew "Well, I only had…"
            Bouncer "I don't think the boss had any appointments with a homeless guy today. Beat it."
            Andrew "That does it!"
            "I remove my badge from my pocket."
            #Show Item: Badge#
            show item badge at truecenter
            "'Deputy Chief of Police', it reads."
            Andrew "Now how about you take me to where I need to go before I arrest you, and everyone in this joint!"
            hide item badge
        "Tell the truth.":
            Andrew "I am."
            #Show Item: Badge#
            show item badge at truecenter
            hide item badge
            Bouncer "Then you best move along before you get hurt."
            Andrew "I can handle myself just fine."
            Bouncer "Oh yeah, Mr, 'Excuse Me, Sir'...what's the toughest thing you've ever done?"
            Bouncer "Shut down a school raffle for being too disorderly?"
            Bouncer "If it's good, I just might let you through."
            Andrew "I...I killed someone."
            Bouncer "Hah! You're not better than the scum who drink here every night."
            Andrew "It was an accident!"
            Bouncer "Yeah, and so was when I killed my ex-wife for cheating on me."
            Andrew "You better let me in now before I come back here and arrest every last one of you!"
    "I can hear the sound of several tens of triggers being pulled back."
    "I slowly turn around."
    "Nearly every patron of the hall is aiming some kind of firearm in my general direction."        
    Bouncer "We don't like cops around these parts."
    Bouncer "You'd best be moving on before something happens."
    Bouncer "We wouldn't want that now, would we?"
    Bouncer "Don't you have a family to go home to?"
    "I smirk, placing a hand in his pocket."
    "My pistol is back at the station but a good bluff can beat even a straight flush." 
    Andrew "If I go down, I'm at least taking you down with me."
    Bouncer "Feisty."

    "Suddenly, three loud claps emanate from behind the Bouncer."
    "Down the stairs walks a man in an Italian suit."

    Lucifer "That's enough horseplay for one night I think."
    Lucifer "This man is my seven o'clock. Show him in, Ricardo."
    Bouncer "Yes, sir."

    #Scene: Office#
    scene bg office with dissolve

    Lucifer "I’m glad you could finally join us, Andrew."
    "The man sits behind a large coffee table, swirling a glass of whisky."
    Andrew "You said you could help me..."
    Andrew "How do you even know me?"
    "The man taps his head and proceeds to light a cigar."
    Lucifer "All in good time, my boy. All in good time."
    Lucifer "Please,sit."
    Andrew "Wait a minute! You drag me out here and expect to just go along with…"
    "I feel a heavy hand on my shoulder. "
    "I look up at Ricardo staring downwards."
    Lucifer "That wasn't a question."
    "I humbly take a seat"
    Lucifer "Allow me to introduce myself."
    Lucifer "My name is Lucifer. I'm the owner of this establishment, boy."
    Lucifer "While those downstairs partake in the pool hall's merriments, I run a small legal practice in the attic."
    Andrew "What kind of lawyer has an office above a pool hall."
    Lucifer "The kind that doesn't want to be found, boy…"
    "Lucifer pats his chest and removes a cigar."
    "He hands one to me along with a lighter."
    Lucifer "Do you smoke, boy?"

    menu:
        "What should I do?"
        "Agree to smoke":
            Andrew "On special occasions."
            Lucifer "Well then, light up, boy! What could be more special than this?"
            "I light the cigar and hand the lighter back to Lucifer."
            Lucifer "No, no. You keep it. Consider it a welcome gift."
            #Show Item: Lighter#
            show item lighter at truecenter
            "Lighter Acquired"
            hide item lighter

        "Refuse to smoke":
            Andrew "I'm trying to quit."
            Lucifer "You can't make a man smoke a fine Cuban like this all by himself!"
            Andrew "I really shouldn't."
            Lucifer "Well, then I won't say any more about it. Consider my silence a welcome gift."

    "Lucifer lights his own and, after three short puffs, smiles a toothy grin."
    Lucifer "Are you a good person, boy?"

    menu:
        "What should I say?"
        "Yes":
            Andrew "I like to think so."
            Lucifer "Is that right?"
            Lucifer "Were you a good person when you held your neighbor's incriminating laptop for ransom?"
            Andrew "How did you-?"
            Lucifer "What about when you lifted $200 from your local convenience store's cash register?"
            Lucifer "Were you a good person then, boy?"
            Andrew "How do you know all this?"
            Lucifer "You see, boy, I don't think you are a good person…"
            "Lucifer puts out his cigar and slams a fist onto the table."
            Lucifer "And that's exactly why I called you."

        "No":
            Andrew "Maybe I was before."
            Andrew "Now, to say 'yes' would be a bald-faced lie."
            Andrew "I've done so much. Hurt so many people."
            Andrew "I can't go back to the life I used to live."
            Lucifer "Would you like to?"
            Andrew "If I'm going to Hell anyway, I may as well enjoy the ride, right?"
            "Lucifer puts out his cigar and slams his fist onto the table."
            Lucifer "That...is a good answer, boy. Very good indeed."
    
    Lucifer "Take a look at this."
    "Lucifer slides a file across the table."
    "It lands cosily in my lap."
    "I open it to reveal the blurred picture of a man."
    Lucifer "This is one of my clients—Sebastian Mathers."
    Lucifer "He did something very bad and asked me to help with his case."
    Andrew "What did he do?"
    Lucifer "Let's just say, if this were a pissing contest…"
    Lucifer "You'd be a dribble and he'd be a fire hose."
    Lucifer "The only problem is, his case is unwinnable."
    Lucifer "The opposition has concrete evidence."
    Lucifer "As well as a witness who's dying to testify."
    Andrew "So, what do you need me to do?"
    Lucifer "We need you to make him...go away."
    Andrew "Go away? Or go away?"
    Lucifer "The latter. By any means necessary."
    Lucifer "If you do this for us, boy, let's see if we can't make that gambling debt go away in a similar fashion."
    Lucifer "I'm sure your family would like that."
    "Lucifer outstretches his hand."
    Lucifer "Do we have a deal?"

    menu:
        "What should I do?"
        "Accept Lucifer's offer.":
            Andrew "You can erase my entire debt?"
            Lucifer "In the blink of an eye."
            Andrew "..."
            Andrew "Fine. I'll do your dirty work."
            Lucifer "Wonderful!"

        "Reject Lucifer's offer.":
            Andrew "I know I've done some terrible things in my time but…"
            Andrew "I've never willingly taken a man's life."
            Andrew "I have to decline."
            Lucifer "You're rejecting me?"
            Andrew "Send my family the images. I'll find my own way to manage—without violence"
            Andrew "I don't think I have the ability to willingly take someone's life."
            Lucifer "Come on! It's easy!"
            "Before I have time to react, Lucifer lifts a pistol from the nape of his thigh."
            "Hearing the sound of the door lock behind me, I realize the schoolboy error I've just made."
            Lucifer "Let me show you."
            "You have died"
            return

    Lucifer "In that case, I'd like you to pay a visit to the parties involved."
    Lucifer "Both the witness and Sebastian himself. See what you can uncover."
    Lucifer "Perhaps you may be able to solve our problem peacefully."
    Andrew "I'll do my best."
    Lucifer "Then we have nothing more to discuss."
    "Lucifer gestures to the door."
    "I make my way over, cautiously."
    Lucifer "Oh, boy!"
    Lucifer "One last thing."
    Lucifer "You may see it wise to visit your family as well."
    Lucifer "Should you fail to meet my expectations…"
    Lucifer "I doubt you'll be seeing them again."    


        








        



