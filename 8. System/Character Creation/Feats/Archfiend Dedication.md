---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archfiend|Archfiend]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Driven by your Calling, you've begun to make plans for your own personal realm from whence you're destined to rule over an army of fiends. Name your realm and describe its eventual appearance. Whether it contains raging hellfire, ponds of caustic acid, or banks of poisonous fog, your realm should be marked by distinctive terrain. Select one of the following damage types associated with your realm's environmental dangers: acid, cold, electricity, fire, or poison. This is your realm's damage type. You gain resistance to the selected damage type equal to half your level. If you already have resistance to this damage type, increase your resistance by 5.

The certainty of your will is such that you can temporarily bring forth a portion of your realm into this world. You gain the [[Manifest Realm]] ability. Other feats allow you to further manipulate your manifested realm.

Archfiend

**Source:** `= this.source` (`= this.source-type`)
