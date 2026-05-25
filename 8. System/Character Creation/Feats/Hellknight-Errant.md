---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Hellknight Dedication, you’ve refused to take or have failed the Hellknight Test"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Either through unfortunate circumstances or your own choice, you remain a Hellknight armiger instead of entering the true ranks of your order, though you still believe in the tenets of law and order. You likely take on an adventuring life with a group of like-minded individuals who aren't Hellknights. The resistance to mental damage you gained from the Hellknight Dedication feat increases to 5 + your number of archetype class feats from the Hellknight archetype.

You also gain the [[Warding Shift]] action, which allows you to keep your allies from harm.

**Special** You can't take both this feat and [[Hellknight Preferment]] or [[Hellknight Signifer Preferment]].

**Source:** `= this.source` (`= this.source-type`)
