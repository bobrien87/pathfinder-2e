---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Shadow]]", "[[Witch]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your patron warps the target's shadow into a deadly form, such as strangling hands, a dangerous weapon, harrying runes, or the like. The shadow moves along with the target, always remaining within reach. When you Cast the Spell, and each time you Sustain it, the shadow Strikes the target. The shadow's Strikes are melee spell attacks that deal 2d10 damage. You choose the type of damage (bludgeoning, piercing, or slashing) when you Cast the Spell. The shadow uses and contributes to your multiple attack penalty. The shadow doesn't take up space, grant flanking, or have any other attributes a creature would. The shadow can't make any attacks other than its Strike.

The shadow vanishes if the target ceases to cast a shadow (usually if it moves into complete darkness or light). If another effect is controlling the target's shadow when you cast *malicious shadow*, you can attempt to counteract that effect to temporarily take control of the shadow for *malicious shadow*'s duration.

**Heightened (+2)** The Strike damage increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
