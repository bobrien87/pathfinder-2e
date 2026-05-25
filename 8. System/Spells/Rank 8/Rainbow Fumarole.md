---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Incapacitation]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "500 feet"
area: "20-foot cylinder"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 20-foot radius, 60-foot-tall cylinder

Multi-hued flames break through cracks in the ground, reaching high into the sky and giving off dangerous fumes. When you cast the spell, roll 1d8 on the table below to determine the effects of the fumarole.

Any creature caught inside the area of *rainbow fumarole* when you cast it takes the indicated damage with a basic Reflex save and, on a failure, takes any added effect listed. Creatures must also attempt a saving throw when they move through the spell's area or end their turn in it. Squares within the area of the *rainbow fumarole* are difficult terrain.

d8ColorDamageAdded Effect1Red@Damage[50[fire],2d6[persistent,fire]]{50 fire plus 2d6 persistent fire}—2Orange50 fireKnocked [[Prone]]3Yellow@Damage[30[fire],20[bludgeoning]]{30 fire plus 20 bludgeoning}Pushed 10 feet4Green@Damage[20[fire],20[acid]]{20 fire plus 20 acid}[[Sickened]] 25Blue30 fire[[Paralyzed]] for 1 round6Indigo30 fire[[Confused]] for 1 minute7Violet30 fire[[Slowed]] 1 for 1 minute8AllChoose the color for each affected creature and use that color's damage and added effect; if a creature is affected again, you can choose a different color.—

**Source:** `= this.source` (`= this.source-type`)
