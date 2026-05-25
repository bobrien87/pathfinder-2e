---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Linguistic]]", "[[Manipulate]]", "[[Mental]]"]
cast: "1 hour"
range: "1 mile"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth numerous breezes in which you weave gossip, whispering subtly into the ears of those around. Choose a rumor or information you wish to spread, which may or may not be true, about a single subject. Those within range of the spell overhear the rumor at some point over the next hour, though they'll be unable to pin it down to a source. Attempt a check with a modifier equal to your spell DC - 10 against a hard DC for your level. The GM might modify the DC depending on how plausible the rumor is. Repeated castings to spread the same rumor or information have no effect unless circumstances have substantially changed, as determined by the GM.
- **Critical Success** Your rumor spreads far and wide, and it's at the tip of people's tongues. For 1 week, anyone who succeeds at a check to Gather Information on the specific subject learns your rumor in preference to other rumors about the subject. Skill checks to convince people that the rumor is true get a +2 circumstance bonus.
- **Success** Enough people take note of the rumor that it begins to spread, though those who heard the rumor aren't necessarily convinced. For 1 week, anyone who succeeds at a check to Gather Information on the specific subject adds your rumor to the list of rumors they could learn about the subject, and skill checks to convince people that the rumor is true get a +1 circumstance bonus.
- **Failure** Most in the area dismiss the rumor as wild gossip and pay it little mind, granting no effect.
- **Critical Failure** The winds' gossip is misinterpreted and spreads information contradictory to the rumor you were attempting to spread. A contradictory rumor spreads, and skill checks to convince others that your original rumor is true take a -2 circumstance penalty.

**Source:** `= this.source` (`= this.source-type`)
