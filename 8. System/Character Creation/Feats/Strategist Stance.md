---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Marshal|Marshal]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Marshal Dedication, trained in Society or Warfare Lore"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You find the most strategic options for you and your allies. When you use this action, attempt a [[Society]] check or Warfare lore check. The DC is usually a standard-difficulty DC of your level, but the GM can assign a different DC based on the circumstances.

> [!danger] Effect: Stance: Strategist Stance
- **Critical Success** Your marshal's aura increases to a @Template[type:emanation|distance:20], and it grants you and allies a +1 status bonus to Reflex saving throws. Once per turn, when you succeed or critically succeed at a Recall Knowledge check to gain information about an enemy creature, the target of the Recall Knowledge check becomes [[Off Guard]] to the next attack made against it by you or an ally in your aura.
- **Success** As critical success, but your aura's size doesn't increase.
- **Failure** You fail to enter the stance.
- **Critical Failure** You fail to enter the stance and can't take this action again for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
