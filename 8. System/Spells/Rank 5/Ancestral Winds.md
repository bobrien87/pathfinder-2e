---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Manipulate]]", "[[Mental]]", "[[Void]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "20-foot burst"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call on the same energies that manifest ancestor storms, summoning wailing spirits to terrorize your foes. Living creatures in the area take 5d6 void damage and 1d6 mental damage and must attempt a Will save. Nonliving creatures are immune to this spell's effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Frightened]] 1.
- **Failure** The creature takes full damage and is [[Frightened]] 2.
- **Critical Failure** As failure, but the creature takes double damage and is [[Stunned]] 1.

The first time each round you Sustain the spell, you can move the area up to 30 feet within the range of the spell. Living creatures in the new area must attempt saves with the same effects as above.

**Source:** `= this.source` (`= this.source-type`)
