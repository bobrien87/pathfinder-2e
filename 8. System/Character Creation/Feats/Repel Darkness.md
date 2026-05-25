---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Nidalese Horselord|Nidalese Horselord]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Aura]]", "[[Concentrate]]", "[[Occult]]"]
prerequisites: "Nidalese Horselord Dedication"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Your stoicism and courage seem to drive off darkness and shadow. For 1 minute, you suppress magical darkness effects of a rank equal to or lower than half your level rounded up within a @Template[type:emanation|distance:10]. This doesn't provide light, but merely restores the area to its natural illumination level. You can Dismiss this aura.

If your horse is at least a mature animal companion, you can use Repel Darkness to cause the aura to emanate from your horse instead of you, as long as your horse is within 100 feet.

**Source:** `= this.source` (`= this.source-type`)
