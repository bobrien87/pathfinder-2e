---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Extradimensional]]", "[[Manipulate]]"]
cast: "`pf2:3`"
duration: "24 hours"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Like Vil Seral, you collect information from all around you and store it in book form in an extradimensional library. When you Cast this Spell, choose any skill in which you are at least trained that has the Recall Knowledge action.

During the duration of this spell, you can call forth a tome from the extradimensional library when attempting a Recall Knowledge check using your chosen skill. This is part of the action to Recall Knowledge. You must have a hand free to do so. The tome appears in your hand, open to an appropriate page. This grants you a +1 status bonus to the Recall Knowledge check. If you roll a critical failure on this check, you get a failure instead. If the roll is successful and the subject is a creature, you gain additional information or context about the creature. Once you reference a book from your pocket library, the spell ends.

> [!danger] Effect: Spell Effect: Pocket Library

**Heightened (3rd)** The status bonus increases to +2 and you can reference your *pocket library* twice before the spell ends.

**Heightened (6th)** The status bonus increases to +3 and you can reference your *pocket library* three times before the spell ends.

**Heightened (9th)** The status bonus increases to +4 and you can reference your *pocket library* four times before the spell ends.

**Source:** `= this.source` (`= this.source-type`)
