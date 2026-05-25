---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vigilante|Vigilante]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Skill]]", "[[Social]]"]
prerequisites: "animal companion or familiar, expert in Deception, Vigilante Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you are in your social identity, you can also grant a social identity to an animal companion, familiar, or other minion you gained from a class feature.

When changing to your social identity, you also change your minion's appearance to that of a socially acceptable creature of its type, such as grooming a wolf to appear as a large dog or disguising a familiar to appear as an exotic pet.

Commanding your minion to use unusual magical or combat abilities it gained from your class features or feats while in this social identity risks exposing your vigilante identity.

**Source:** `= this.source` (`= this.source-type`)
