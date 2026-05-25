---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]", "[[Mythic]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 intelligent creature"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a gleeful cackle, you seize an individual's voice and swallow it. For the duration, you look and sound like the target, and the target can't speak. The effects depend on the result of the target's Will saving throw.
- **Critical Success** The creature is unaffected.
- **Success** You take on the target's appearance, with the same effects of a 3rd-rank [[Illusory Disguise]] spell, and the target can't speak, with the same effects of a 2nd-rank [[Silence]] spell.
- **Failure** As success, but the target also takes 4d6 mental damage from the transformation.
- **Critical Failure** As success, but the target also takes 8d6 mental damage from the transformation.

The first time each round you Sustain this spell after you cast this spell, the target ages rapidly, taking @Damage[(ternary(gte(@item.rank,9),3,2))d8[void]] damage ([[Will]] save). On a failure, the target also becomes [[Enfeebled]] 1 or increases the value of its enfeebled condition by 1.

**Heightened (9th)** The mental damage increases by 4d6, and the void damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
