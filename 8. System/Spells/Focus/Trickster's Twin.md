---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Illusion]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You rarely settle for being in just one place. Choose a location within 100 feet of the target that the target can see. You create an illusion of yourself there that only it can see and that mimics all your actions. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target believes you're in the designated location and can't see you in your actual location. The target automatically disbelieves the illusion when you use an action that doesn't make sense in the illusion's position, or if the target attacks, touches, Seeks, or otherwise engages with the illusion. If you use a hostile action against the target, the spell ends.
- **Failure** As success, but the target must succeed at a Will save to disbelieve the illusion when one of the listed events occurs.
- **Critical Failure** As success, but the target must critically succeed at a Will save to disbelieve when one of the listed events occurs.

**Source:** `= this.source` (`= this.source-type`)
