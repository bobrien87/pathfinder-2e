---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You try to fool someone with an untruth. Doing so takes at least 1 round, or longer if the lie is elaborate. You roll a single Deception check and compare it against the Perception DC of every creature you are trying to fool. The GM might give them a circumstance bonus based on the situation and the nature of the lie you are trying to tell. Elaborate or highly unbelievable lies are much harder to get a creature to believe than simpler and more believable lies, and some lies are so big that it's impossible to get anyone to believe them.

At the GM's discretion, if a creature initially believes your lie, it might attempt a Perception check later to [[Sense Motive]] against your Deception DC to realize it's a lie. This usually happens if the creature discovers enough evidence to counter your statements.
- **Success** The target believes your lie.
- **Failure** The target doesn't believe your lie and gains a +4 circumstance bonus against your attempts to Lie for the duration of your conversation. The target is also more likely to be suspicious of you in the future.

**Source:** `= this.source` (`= this.source-type`)
