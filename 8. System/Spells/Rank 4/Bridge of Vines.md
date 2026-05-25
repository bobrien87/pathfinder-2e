---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:3`"
range: "60 feet"
defense: "Reflex"
duration: "10 minutes"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Vines sprout beneath your feet and extend away from you in a straight line up to 60 feet, forming a 10-foot-wide bridge that can cross over difficult terrain and low obstacles, as well as reach higher ground. The bridge has an AC equal to your spell DC, Hardness 10, and 20 Hit Points. It is immune to critical hits and precision damage. The bridge lasts either for the duration of the spell, until it is destroyed, or until you Dismiss the spell.

While the spell is active, you and your allies can use the bridge normally. If any other creatures attempt to use the bridge, the vines attempt to trip and entangle them. They must attempt a Reflex save against your spell DC.
- **Critical Success** The target is unaffected.
- **Success** The target treats the length of the bridge as difficult terrain.
- **Failure** As success, and the target is knocked [[Prone]].
- **Critical Failure** As success, and the target is knocked prone and [[Grabbed]] until it Escapes (with a DC equal to your spell DC) or the spell ends.

**Heightened (+1)** The bridge's Hit Points increase by 10.

**Source:** `= this.source` (`= this.source-type`)
