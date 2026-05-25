---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Focus]]", "[[Sorcerer]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw forth a hag's innate jealousy to deny a target its greatest attribute. The target is cursed with an adverse condition depending on its highest attribute modifier: Strength ([[Enfeebled]]); Dexterity ([[Clumsy]]); Constitution ([[Drained]]); or Intelligence, Wisdom, or Charisma ([[Stupefied]]). On a tie, the creature decides which of the conditions associated with the tied attributes to take. The target must attempt a Will save. At the start of each of your turns, the target can attempt another Will save, ending the effect on a success.
- **Success** The target is unaffected.
- **Failure** The condition's value is 1.
- **Critical Failure** The condition's value is 2

**Source:** `= this.source` (`= this.source-type`)
