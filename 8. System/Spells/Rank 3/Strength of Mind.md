---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Mental]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 willing creature"
duration: "10 minutes"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You bolster your ally with reminders of their physical prowess, granting them additional defenses against harmful mental effects. The target gains a +1 status bonus to saving throws against mental effects and against effects that hinder movement (including those that reduce Speed or apply the [[Grabbed]], [[Immobilized]], or [[Restrained]] conditions). This bonus increases to +2 if the source of the effect has the fear trait.

> [!danger] Effect: Spell Effect: Strength of Mind

**Source:** `= this.source` (`= this.source-type`)
