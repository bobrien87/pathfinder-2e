---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ulfen Guard|Ulfen Guard]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "member of the Ulfen Guard, trained in Athletics and Intimidation"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** At least one of your parents is Ulfen.

Central to your Ulfen Guard training is the ability to protect an ally. You gain the [[Additional Lore]] skill feat for Warfare Lore. If you were already trained in Warfare Lore, you also become trained in a Lore skill of your choice. You gain the [[Designate Ally]] action.

It's anathema for you to abandon your designated ally or allow your designated ally to die when you can prevent it. If you violate this anathema, you lose the ability to Designate Ally and any feats that use this ability until you spend 1 day of downtime reaffirming your dedication to your allies.

Ulfen Guard

**Source:** `= this.source` (`= this.source-type`)
