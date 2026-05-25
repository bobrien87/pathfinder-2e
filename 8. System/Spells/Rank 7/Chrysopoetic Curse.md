---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "one creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grant the target the gift of riches, giving them the power to turn anything they touch to gold. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target's skin turns their armor and clothing partially to gold. If the target is wearing any armor or clothing, they become [[Encumbered]].
- **Failure** As success, but the curse extends to the target's held weapons and other gear. If the target is holding any weapons or other objects, they become [[Clumsy]] 3, and the objects' Hardness is reduced by 5.
- **Critical Failure** The curse becomes even stronger, extending to the surrounding terrain. As failure, and if the creature is standing on a solid surface, the ground in their space transmutes itself into a quagmire of liquid gold. The gold is greater difficult terrain. If the creature leaves its square (or when the curse ends), any affected terrain returns to its original shape and substance and the terrain in the new square transmutes to gold.

Any objects that were turned to gold return to their previous form and original shape when they leave the target's possession or the spell ends. As long as the target did not critically succeed on their saving throw, 2d6 gp worth of gold flakes and dust are left behind as the curse recedes.

**Source:** `= this.source` (`= this.source-type`)
