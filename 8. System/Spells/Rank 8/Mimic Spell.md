---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:r`"
range: "120 feet"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature you're aware of within range Casts a Spell of the same tradition as *mimic spell* and of the same or lower rank.

You learn the secrets of a spell just by watching someone else cast it. Attempt to counteract the spell cast by the triggering creature. If the spell would be counteracted, you instead gain the ability to Cast that Spell without expending a slot.

On your next turn, you spend the same number of actions to Cast the Spell as the triggering creature, but you choose the targets (if any) and use your spell attack modifier or spell DC as appropriate. The spell is heightened to the same rank as mimic spell. The mimicked spell is of the same tradition as the spells you normally cast.

If you don't Cast the mimicked Spell by the end of your next turn, it is lost, unless you Sustain the knowledge of it. You can Sustain this knowledge for up to 1 minute, after which it is lost.

**Source:** `= this.source` (`= this.source-type`)
