---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You surround yourself in a bubble-like shroud of seawater that fills your space completely and moves with you. You can breathe, speak, and perceive normally while within your personal ocean, and you gain a swim Speed equal to your land Speed if you don't have one. The rules of aquatic combat apply to you, attacks targeting you, or attacks passing through your square. For instance, a bludgeoning or slashing melee attack targeting you would take a –2 circumstance penalty, and you can't cast fire spells or use actions with the fire trait.

Each time you move, you extinguish non-magical fires in spaces you pass through and can attempt to counteract magical fires you move through. If you successfully counteract a fire larger than the spaces you moved through, you merely push it out of the spaces along your path. If you fail to counteract a given fire, you can't counteract that fire for the duration of the spell.

You can Dismiss the spell.

**Source:** `= this.source` (`= this.source-type`)
