import random
subjects = ["boy","monkey","teacher","robot"]
verbs = ["eating","dancing","running","reading"]
places=["park","classrooom","market","beach"]
s = random.choice(subjects)
v = random.choice(verbs)
p = random.choice(places)
story = s +" "+v+" "+p
print("Your random story:")
print(story)