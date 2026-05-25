---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Reflex"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Barnacles, coral, and other rough aquatic creatures grow on the target's body, getting in between their joints and stiffening their movement. This impedes the target's movement depending on the result of its saving throw.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Clumsy]] 1. The target can Interact to scrape the coral growths from its body, decreasing the clumsy condition to 0 and ending the spell.
- **Failure** The target is [[Clumsy]] 2. Each round at the beginning of its turn, the target becomes clumsy 1 or increases its clumsy condition by 1, to a maximum of 4. The target can Interact to scrape the coral growths from its body, decreasing the clumsy condition to 0 and ending the spell. If the target's clumsy condition caused by *coral scourge* reaches 4, the growths spread to cover the target's entire body, and the target becomes [[Paralyzed]].
- **Critical Failure** As failure, but when the target Interacts to scrape the coral growths from its body, it reduces its clumsy condition by 1, instead of decreasing it to 0, and decreasing the clumsy condition to 0 doesn't end the spell.

**Source:** `= this.source` (`= this.source-type`)
