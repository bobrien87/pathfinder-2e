---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mythic]]"]
cast: "`pf2:3`"
range: "60 feet"
duration: "1 hour"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure an intelligent sea turtle, who agrees to carry you upon its shell on a water journey. This turtle must be conjured into a large body of water within range, such as a lake or broad river. The turtle conjured is Large, is capable of carrying one Medium creature or up to four Small creatures, and has a swim Speed of 30 feet. The turtle doesn't engage in combat and doesn't put itself intentionally into harm's way, but it does convey you to a destination of your choice and follows your suggestions. The turtle otherwise functions as a boat, save that it controls itself and doesn't need to be piloted.

**Heightened (5th)** The turtle's size increases to Huge, making it capable of carrying one Large creature, up to four Medium creatures, or up to 16 Small creatures. Its swim Speed increases to 40 feet, and the duration increases to 1 day.

**Heightened (7th)** The turtle's size increases to Gargantuan, making it capable of carrying one Huge creature, up to four Large creatures, up to 16 Medium creatures, or up to 32 Small creatures. Its swim Speed increases to 50 feet, and the duration increases to 1 week.

**Heightened (9th)** The turtle's size increases to Gargantuan, making it capable of carrying two Huge creatures, up to eight Large creatures, up to 32 Medium creatures, or up to 64 Small creatures. Its swim Speed increases to 60 feet, and the duration increases to 1 month.

**Source:** `= this.source` (`= this.source-type`)
