---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Bard]]", "[[Composition]]", "[[Concentrate]]", "[[Focus]]", "[[Incapacitation]]", "[[Mental]]", "[[Sonic]]"]
cast: "`pf2:2`"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your performance enraptures listeners, compelling them to follow you. Each creature within the emanation must attempt a Will save when you Cast the Spell or the first time they enter the area, after which they become temporarily immune for 1 day. Once per turn, you can Sustain the composition to increase the emanation's radius by 5 feet. You can Dismiss the spell.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Fascinated]] with you.
- **Failure** The creature is fascinated by you and uses all its actions to move toward you and compliment your performance. This effect ends if a hostile action is used against the affected creature.
- **Critical Failure** The target gains the minion trait and is controlled by you. This effect ends if a hostile action is used against the affected creature, or if you direct the creature to use any action that causes it harm.

**Source:** `= this.source` (`= this.source-type`)
