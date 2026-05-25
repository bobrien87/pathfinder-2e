---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Psychic]]", "[[Scrying]]"]
cast: "`pf2:1`"
area: "30-foot emanation"
targets: "1 ally and 1 enemy"
duration: "until the start of your next turn"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You quickly view your surroundings from a variety of angles, your senses constructing an overall mental picture. You can choose to `act seek` the entire emanation of the spell.

Regardless of whether you seek, target one ally and one enemy in the area; if a target is [[Concealed]] or [[Hidden]] from you, you automatically succeed at the flat check to target it with this spell. You prepare to [[Aid]] the target ally on an attack roll against the target enemy. If you take this Aid reaction, you use your spell attack modifier and proficiency rank on your check to Aid. If you critically fail the roll to Aid, you get a failure instead.

**Source:** `= this.source` (`= this.source-type`)
