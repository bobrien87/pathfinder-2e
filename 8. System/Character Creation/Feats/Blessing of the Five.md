---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "0"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
prerequisites: "Order of the Godclaw"
frequency: "once per day"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Effect** You call out to [[The Godclaw]] to heal your allies. You cast the 3‐action version of [[Heal]], heightened to a rank one lower than half your level rounded up. You can select up to five creatures in the area to remain unaffected by the spell. You can instead use this ability to bring a creature within 30 feet that has died within the last round back from the dead. If you do, the creature is restored to 1 Hit Point and is [[Doomed]] 1.

**Source:** `= this.source` (`= this.source-type`)
