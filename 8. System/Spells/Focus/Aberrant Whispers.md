---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Focus]]", "[[Mental]]", "[[Sorcerer]]"]
cast: "1 to 3"
area: "5-foot emanation"
targets: "each foe in the area"
defense: "Will"
duration: "1 round"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You utter phrases in an unknown tongue, assaulting the minds of those nearby. Each target must attempt a Will save. Regardless of the result of its save, each target is then temporarily immune for 1 minute. For each additional action you use when Casting the Spell, increase the emanation's radius by 5 feet.
- **Success** The target is unaffected.
- **Failure** The target is [[Stupefied 2]].
- **Critical Failure** The target is [[Confused]].

**Heightened (+3)** The initial radius increases by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
