---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 living humanoid"
defense: "Fortitude"
duration: "varies"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You tap into the target's inner being and curse it to become a bestial version of itself. The effect is based on its Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target's body gains minor bestial features. Its insides churn as they partially transform, causing it to be [[Clumsy]] 1 for 1 round. When it recovers from the clumsy condition, its features revert to normal, and the spell ends.
- **Failure** The target transforms into a bestial form for 1 hour. The target becomes clumsy 1 and gains weakness 1 to silver. It gains a claw, hoof, horn, or jaws Strike (your choice) that uses the target's unarmed Strike statistics except that the damage type changes to bludgeoning, piercing, or slashing, as appropriate. Whenever the target attempts to use any manipulate action, it must succeed at a DC 5 flat check or the action is lost.

> [!danger] Effect: Spell Effect: Bestial Curse (Failure)
- **Critical Failure** As failure, but the duration is unlimited.

> [!danger] Effect: Spell Effect: Bestial Curse (Critical Failure)

**Source:** `= this.source` (`= this.source-type`)
