---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "10-foot burst"
defense: "Fortitude"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You whisper baleful secrets that transcend language and carry magically to the ears of your foes. The words take physical form, weakening the life force of the targets, each of which must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes @Damage[(floor(@item.rank/2))d8[persistent,void]] damage.
- **Failure** The creature takes @Damage[(floor(@item.rank/2)*2)d8[persistent,void]] damage and becomes [[Drained]] 1.
- **Critical Failure** The creature takes @Damage[(floor(@item.rank/2)*2)d8[persistent,void]] damage and becomes [[Drained]] 2 and [[Doomed]] 1.

**Heightened (+2)** The persistent void damage increases by 1d8 on a success, or by 2d8 on a failure or critical failure.

**Source:** `= this.source` (`= this.source-type`)
