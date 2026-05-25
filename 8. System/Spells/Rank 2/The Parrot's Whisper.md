---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth an echo of the gossiping parrot from the tale of the Witch and the Weaver to whisper the secrets of a creature you can see within range. The garrulous parrot is known to chatter on for some time while deciphering the information you seek. The target must attempt a Will saving throw.
- **Critical Success** The parrot chatters about various random topics for 1 round and reveals no relevant information.
- **Success** The parrot tells you the target's highest weakness at the start of your next turn. In the meantime, the parrot chatters about various random topics.
- **Failure** The parrot tells you the target's highest weakness immediately, but sticks around for 1 round to chatter.
- **Critical Failure** The parrot tells you the target's highest weakness immediately, and you can ask the parrot one question about the target creature. You might need to collaborate with the GM to narrow down the question. At the start of your next turn, the parrot answers the question truthfully.

**Source:** `= this.source` (`= this.source-type`)
