---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
duration: "10 minutes (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure up to six 5-foot stone cubes you can gently move with a gesture. Each cube appears in any space within range, and they're capable of levitating. If you conjure a cube in an occupied space or in a space that can't accommodate it, it fails to appear. Each 5-foot cube can be Climbed with a successful DC 10 [[Athletics]] check and has AC 10, Hardness 10, and 40 Hit Points. If any of the cubes is ever farther away from you than the range of this spell, it immediately crumbles into dust.

Each time you Sustain this spell, you can move up to two of the conjured cubes up to 10 feet each in any direction, including vertically. You can choose different cubes to move each time you Sustain.

**Heightened (+2)** The cubes have 10 additional Hit Points, and you can move the chosen cubes an additional 5 feet each time you Sustain this Spell.

**Source:** `= this.source` (`= this.source-type`)
