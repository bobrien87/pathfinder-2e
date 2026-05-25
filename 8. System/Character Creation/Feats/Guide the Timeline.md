---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Chronoskimmer|Chronoskimmer]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Chronoskimmer Dedication"
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You know the result you want and subtly nudge the timeline to your intended destination. Choose an ally or a foe. If you choose an ally, the next time within the next round that ally makes an attack roll or skill check, they roll it twice and take the higher result; this is a fortune effect. If you choose a foe, the next time within the next round that foe makes an attack roll or skill check, they must roll twice and take the lower result unless they succeed at a [[Will]] save against your chronoskimmer DC; this is a misfortune effect. Regardless of your choice, the target becomes temporarily immune for 24 hours.

> [!danger] Effect: Guide the Timeline

**Source:** `= this.source` (`= this.source-type`)
