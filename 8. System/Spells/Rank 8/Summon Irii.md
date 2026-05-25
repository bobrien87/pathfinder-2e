---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "100 feet"
duration: "until the end of your next turn"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cast your spell, whisper your words of power, and find that an irii is already here—indeed, they've always been here, and always were, and always will be. The temporal being occupies the space of a Medium creature and has a Speed of 60 feet and a fly Speed of 60 feet. When you Cast this Spell, choose whether it summons a fate irii or a fortune irii.

- **Fate** The fate stands before you with its stained-glass wings and animal-headed gaze, floating eyes circling about it.

- **Arrive** (fortune, prediction) *Decree the Immutability of Time* While within 30 feet of the fate, you and your allies who roll below 10 on a d20 for an attack roll, Perception check, saving throw, or skill check get a 10 instead.
- **Depart** (misfortune, prediction) *Observe the Inevitability of Destiny* Each enemy within a @Template[type:emanation|distance:30] must attempt a [[Will]] save. If a creature fails its save, until the end of its next turn, any time it rolls above 10 on a d20 for an attack roll, Perception check, saving throw, or skill check, it gets a 10 instead.

- **Fortune** The fortune stands before you with its golden horns and moth-scale wings, a sly smirk on its elfin face.

- **Arrive** (fortune, prediction) *Decree the Chaos of Infinity* While within 30 feet of the fortune, you and your allies roll twice and take the higher roll on all damage rolls, Perception checks, and saving throws.

- **Depart** (misfortune, prediction) *Sunder Eternity's Authority* Each enemy within a @Template[type:emanation|distance:30] must attempt a [[Will]] save. A creature that fails its save must roll twice and take the lower result on all damage rolls, Perception checks, and saving throws until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
