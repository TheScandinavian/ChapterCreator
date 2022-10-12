# ChapterCreator
STEP 1 - DOWNLOAD THE SCRIPT

STEP 2 - DOWNLOAD PYTHON

STEP 3 - ENSURE SCRIPT IS IN NON-CLUTTERED FOLDER FOR SAKE OF CONVENIENCE

STEP 4 - EXECUTE SCRIPT; IT WILL GENERATE A .TXT FILE NAMED "YOUR CHAPTER" IN THE SAME FOLDER

STEP 5 - IF YOU WANT TO KEEP THE .TXT FILE, RENAME IT OR MOVE IT BEFORE EXECUTING THE SCRIPT AGAIN





Hello,
I am the Scandinavian, the creator of this script.
Chances are you haven't heard of me until now.
The script is the work of an amateur with a slightly-more-than-passing interest in the Warhammer 40,000 setting.

The creation table I worked off of was originally made by the anons on 4chan's /tg/.
If you're curious, it can be found on 1d4chan.org.
I have never personally visited /tg/, unless after the time of writing this I shared this script there.
If anyone from /tg/ reads this, thanks for the inspiraton guys.
I manually rolled 52 Chapters on the table before I got the idea to automate the process.

Most of the sources I've used for the roll results are from 1d4chan, Lexicanum, or the Warhammer 40k Wiki.
Perhaps unsurprisingly, cross-referencing was a mess. I can now sympathize with the Adeptus Administratum.

Prior to writing this, I had very little coding experience, and none at all in Python.
With that in mind, please be aware that the script is not at all perfect, but it does work.
It will allow you to automatically generate a Space Marine Chapter in the form of a text document.
(Names are not generated, you'll have to do that part.)

The script's only requirement is that Python is installed.
Without Python installed, the script will not work.

The text file generated by the script will be put in the same folder as the script itself.
It will be called "Your Chapter.txt" - I recommend that you store the script in its own folder.

VERY IMPORTANT:

BE AWARE THAT RUNNING THE SCRIPT TWICE DOES NOT CREATE 2 TEXT FILES.
THE 2ND TEXT FILE WILL OVERRIDE THE 1ST.
IF YOU WANT TO KEEP THE TEXT FILE, YOU SHOULD RENAME IT OR MOVE IT.

The script is easily modifiable.
Simply alter the generated text (the green codelines in the f.writelines("") sections).
Be aware that \n is a function that writes text on a new line. Without it, the text output would all be on one line.

The code should be fairly easy to read.
To a seasoned coder, I'm sure many parts of it appear crude or inefficient, but I tried to at least make it legible.

Mandatory disclaimer:
My work on this project is unpaid.
If you paid for this script, you've been tricked.

DISCLAIMER SPECIFICALLY FOR GAMES WORKSHOP:

THIS IS IN NO WAY, SHAPE OR FORM ENDORSED, SPONSORED, APPROVED, BACKED, SANCTIONED, ADVOCATED, SUPPORTED OR LICENSED BY GAMES WORKSHOP OR ANY ONE INDIVIDUAL OFFICIALLY ASSOCIATED WITH THAT COMPANY IN ANY WAY, SHAPE OR FORM.
THIS IS NOT AN OFFICIAL PRODUCT OF GAMES WORKSHOP OR ANY ONE INDIVIDUAL OFFICIALLY ASSOCIATED WITH THAT COMPANY.
THIS IS NOT INTENDED TO INFRINGE UPON THE COPYRIGHTS OR TRADEMARKS OF GAMES WORKSHOP OR ANY ONE INDIVIDUAL OFFICIALLY ASSOCIATED WITH THAT COMPANY.
THIS IS A NON-PROFIT FAN-MADE SCRIPT, CREATED SOLELY AS A NON-PROFIT HOBBYIST TOOL.
THE CONTENTS OF THIS SCRIPT ARE NOT SUBJECT TO ANY COPYRIGHT OR TRADEMARK ON MY PART.
THE MATERIAL FROM WHICH THIS SCRIPT DRAWS INSPIRATON ARE NOT SUBJECT TO ANY COPYRIGHT OR TRADEMARK ON MY PART.
I MAKE NO CLAIMS TO WARHAMMER 40,000 OR ANY PART THEREOF IN ANY WAY, SHAPE OR FORM.

TO THE BEST OF MY KNOWLEDGE, THIS SCRIPT ADHERES TO THE INTELLECTUAL PROPERTY GUIDELINES LAID OUT BY GAMES WORKSHOP.
TO THE BEST OF MY KNOWLEDGE, THIS SCRIPT:
- DOES NOT INCLUDE TEXT, ARTWORK OR IMAGERY FROM ANY OFFICIAL GAMES WORKSHOP MATERIAL.
- IS NON-COMMERCIAL, WITH NO MONEY BEING RECEIVED OR PAID ON MY PART. THIS INCLUDES ALL FORMS OF FUNDRAISING ACTIVITY, AND GENERATION OF ANY ADVERTISING REVENUE.
- IS NOT PUBLICLY DISTRUBUTED, EXCEPT FOR NO-CHARGE DIGITAL DISTRIBUTION.
- IS CLEARLY UNOFFICIAL, AND USES NO GAMES WORKSHOP LOGOS.
- IS NOT PREJUDICIAL TO THE GOODWILL, REPUTATION OR INTEGRITY OF GAMES WORKSHOP OR ITS INTELLECTUAL PROPERTY.
- DOES NOT POST OR DISPLAY ANY RULES OR STATS COPIED FROM ANY OFFICIAL GAMES WORKSHOP MATERIAL.

GAMES WORKSHOP RETAINS OWNERSHIP IN RESPECT OF THE UNDERLYING INTELLECTUAL PROPERTY RIGHTS OF WARHAMMER 40,000.
THIS CONTENT CANNOT BE SOLD OR OTHERWISE MONETISED.

ADDITIONALLY, TO THE BEST OF MY KNOWLEDGE, THIS SCRIPT:
- IS NOT CAPABLE OF, NOR INVOLVED IN, COUNTERFEITING GAMES WORKSHOP PRODUCTS.
- IS NOT CAPABLE OF, NOR INVOLVED IN, IMITATING GAMES WORKSHOP PRODUCTS.
- IS NOT CAPABLE OF, NOR INVOLVED IN, RECASTING OR 3D PRINTING GAMES WORKSHOP PRODUCTS.
- IS NOT CAPABLE OF, NOR INVOLVED IN, ILLEGALLY DOWNLOADING, UPLOADING, SHARING, OR DISTRUBUTING GAMES WORKSHOP PUBLICATONS, AUDIO BOOKS, OR OTHER MATERIALS PROTECTED BY COPYRIGHTS.
- IS NOT CAPABLE OF, NOR INVOLVED IN, UNAUTHORISED USE OR REGISTRATION OF GAMES WORKSHOP TRADEMARKS IN RESPECT TO SIMILAR PRODUCTS OR SERVICES.
- IS NOT CAPABLE OF, NOR INVOLVED IN, CREATING FAN FILMS OR ANIMATIONS BASED ON GAMES WORKSHOP SETTINGS OR CHARACTERS.
- IS NOT CAPABLE OF, NOR INVOLVED IN, CREATING COMPUTER GAMES OR APPS BASED ON GAMES WORKSHOP CHARACTERS OR SETTINGS.

THIS SCRIPT DOES:
- ALLOW USERS TO EASILY GENERATE THEIR OWN CHAPTER OF SPACE MARINES BASED ON A RANDOM NUMBER GENERATOR.

THIS SCRIPT DOES NOT:
- DO ANYTHING ELSE.

To clarify: a script is not an app.
A script is a non-compiled sequence of instructions or commands for a computer to execute. I have, in effect, created a document which a computer can read and interpret to perform an action. This particular script instructs a computer on opening a .txt file, what to name it, what to write in it, how to format it and how to save it.
It is code that acts upon some system in an external or independent manner and can be removed or disabled without disabling the system itself.                                                                         
An app, or a program, is code that constitutes a system. The program's code may be written in a modular manner, with good separation of concerns, but the code is fundamentally internal to, and a dependency of, the system itself.

There are other distinctions between a script and an app, but further elaboration is unnecessary here. 
This script, being a script and not an app, to the best of my knowledge, does not break the intellectual property guidelines as laid out by Games Workshop here: https://www.games-workshop.com/en-US/Intellectual-Property-Guidelines

In closing, I have no idea how many people will ever use my script, let alone take the time to read all this.
If you find this message, I appreciate you.                                                                  And, if you so desire, do share my script with your friends.       
