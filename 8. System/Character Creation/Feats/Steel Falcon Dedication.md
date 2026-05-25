---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Steel Falcon|Steel Falcon]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "expert in Diplomacy"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're invited by a current member of the Eagle Knights or the People's Council.

You serve as an envoy of the ideals of Andoran, whether it's in a foreign court or on the field of battle. Your training in the Steel Falcons enables you to anticipate the attitudes of others to achieve your goals. You gain the [[Size Up]] action.

**Special** You can take this dedication even if you haven't taken more than two non-dedication feats from the Eagle Knight archetype.

Steel Falcon

**Source:** `= this.source` (`= this.source-type`)
