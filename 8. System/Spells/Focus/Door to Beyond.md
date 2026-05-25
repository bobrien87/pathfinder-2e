---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "5 feet"
area: "20-foot emanation"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Striking at thin air, you create hairline cracks in an unoccupied adjacent space that lead somewhere outside reality. Air rushes through the cracks, drawing Large or smaller creatures and objects of light Bulk or less toward the center. Large or smaller creatures in the area must attempt a Fortitude save at the start of their turn; creatures that move into the area must attempt the save upon entering.

The cracks of the door to beyond are too thin for anything to fully slip through, but decompressive effects deal 4d6 slashing damage to any creature or object that ends its turn adjacent to the door. You are unaffected by your own door to beyond. You can Dismiss the spell.
- **Success** The creature is unaffected.
- **Failure** The creature is pulled 10 feet toward the door.
- **Critical Failure** The creature is pulled 20 feet toward the door.

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
