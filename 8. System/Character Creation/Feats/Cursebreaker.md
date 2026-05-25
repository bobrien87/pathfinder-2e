---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Palatine Detective|Palatine Detective]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Healing]]", "[[Manipulate]]"]
prerequisites: "Palatine Detective Dedication"
frequency: "once per day"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Using various implements and esoteric methods, you can attempt to remove a curse from an unfortunate victim. It takes 10 minutes to perform these rites on a willing creature, who must remain within your reach the entire time.

Attempt to counteract one curse afflicting the creature; your counteract rank is half your level rounded up, and you use either your [[Occultism]] check or [[Religion]] check modifier as your counteract modifier. If the afflicted creature or the individual who placed the curse on the afflicted creature is the target of your active investigation through Pursue a Lead, you gain a +1 circumstance bonus to this counteract check.

If the curse comes from a cursed item or other external source, a success indicates that the target creature can rid itself of the cursed item, but it doesn't remove the curse from the item.

**Source:** `= this.source` (`= this.source-type`)
