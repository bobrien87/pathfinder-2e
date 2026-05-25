---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Linguistic]]", "[[Mental]]", "[[Wood]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You share a piece of hidden knowledge with a creature that is both upsetting and intriguing. When you Cast this Spell, choose Arcana, Nature, Occultism, Religion, or Society as the focus of this knowledge. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Fascinated]] by the knowledge you shared for 1 round.
- **Failure** The target is fascinated by the knowledge for 1 minute. The target can end this fascination early by attempting a skill check to Recall Knowledge to understand the knowledge using the chosen skill (using your spell DC as the DC); regardless of the result, the target becomes [[Frightened]] 2, but if they failed the check, they can't reduce their frightened condition below 1 for the remainder of the spell's duration.
- **Critical Failure** As failure, but the target becomes [[Frightened]] 3 if they attempt to Recall Knowledge.

**Source:** `= this.source` (`= this.source-type`)
