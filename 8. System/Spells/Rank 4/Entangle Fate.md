---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "2 to 4 creatures in range"
defense: "Will"
duration: "3 rounds"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause a swirl of energy to entangle the fates of all caught within the blast. Each creature in the area must attempt a Will save.
- **Critical Success** The creature is unaffected.
- **Success** The creature's fate becomes distorted, and momentary conflicting glimpses of the immediate future cause the creature to become [[Off Guard]] until the start of its next turn.
- **Failure** As success, but the creature is off-guard for the duration of the spell. If more than one of the targets failed to resist this spell, the creature also becomes [[Stupefied 1]] for the duration of the spell as its fate and those of the other creatures continue to clash and strain against each other.
- **Critical Failure** As failure, but any creature that becomes stupefied 1 for the duration of the spell also becomes [[Enfeebled]] 1 and [[Clumsy]] 1 for the spell's duration.

**Source:** `= this.source` (`= this.source-type`)
