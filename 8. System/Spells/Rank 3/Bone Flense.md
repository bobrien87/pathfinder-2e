---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 weapon that is either wielded by a member of the Red Mantis or is a praying mantis's leg Strike"
duration: "1 minute"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target weapon becomes imbued with Achaekek's power and glows softly with crimson light akin to that shed by a candle. When a creature with a skeleton or exoskeleton takes damage from a Strike delivered by this weapon, the creature's bones nearest to the wound instantly sprout jagged, razor-sharp spurs that flense the muscle and flesh from inside out. The creature takes an additional 1d6 persistent bleed damage from the Strike. You can use the [[Erupting Spurs]] reaction.

> [!danger] Effect: Bone Flense (Damage)

> [!danger] Effect: Bone Flense (Reaction)

**Heightened (+2)** The persistent bleed damage increases by 1d6. The damage from Erupting Spurs increases by 4d6.

**Source:** `= this.source` (`= this.source-type`)
