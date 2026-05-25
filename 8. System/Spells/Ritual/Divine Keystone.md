---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
traits: ["[[Consecration]]", "[[Holy]]"]
cast: "4 days"
area: "100-foot emanation"
duration: "1 week"
requirements: "cornerstone from the structure of the casting area used as a locus"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You magically remove and consecrate the cornerstone of a building or ruin in the center of a settlement before returning the stone to its structure to spread its divine protection into the settlement around it. Once the final hammer strike returns the stone to its structure, the area protected by the sanctified stone becomes a sacred space, protecting the living from undead. Within the protected area, the consecrated site is holy, undead creatures can't be created or raised, and living creatures are [[Invisible]] to the undead.

A successful [[Dispel Magic]] used on a specific effect removes only that effect (such as the invisibility effect). However, destroying or removing the keystone ends the entire ritual and all its effects.
- **Critical Success** You create the effects described above, and the keystone's consecration effect doubles its radius.
- **Success** You create the effects described above.
- **Failure** The ritual has no effect.
- **Critical Failure** The area becomes a font of power for undead for the next month. All undead creatures in the ritual's area gain fast healing 3 and resistance 3 to holy.

> [!danger] Effect: Spell Effect: Divine Keystone (Critical Failure)

**Heightened (+1)** The emanation protected by the keystone increases by 20 feet.

**Source:** `= this.source` (`= this.source-type`)
