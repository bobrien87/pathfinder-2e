---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Prediction]]"]
cast: "1 minute"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You've learned to read the future in the patterns of flames and smoke. Though inexact and often symbolic, these readings help prepare you for upcoming events. When Casting this Spell, you must be near a fire (of any size) for the duration. Upon completion, roll 1d4 for your prediction. The benefit lasts for 10 minutes or until expended, whichever comes first. After casting cinder gaze, you can't cast it again for 10 minutes.

- **Terrible Danger** You gain a +2 status bonus to your next initiative roll.
- **New Life** The next time you take damage, just before taking the damage, you gain 6 temporary Hit Points.
- **Vivid Insight** (fortune) The next time you attempt a check to Recall Knowledge, roll twice and take the higher result.
- **Good Fortune** (fortune) The next time you attempt a saving throw, roll twice and take the better result.
**Heightened (+1)** The number of temporary Hit Points from new life increases by 2.

> [!danger] Effect: Spell Effect: Cinder Gaze

**Source:** `= this.source` (`= this.source-type`)
