---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "15-foot burst"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A sickly yellow light fills the area as entropic forces prevent healing. When a creature within the area would regain Hit Points, such as from a healing effect or an ability like fast healing or regeneration, it must attempt a Will save.
- **Critical Success** The creature regains the full number of Hit Points that would be restored by the healing effect and is temporarily immune for 1 minute.
- **Success** The creature regains the full number of Hit Points that would be restored.
- **Failure** The creature regains only half the number of Hit Points that would be restored.
- **Critical Failure** The creature doesn't regain Hit Points from the healing effect.

**Source:** `= this.source` (`= this.source-type`)
