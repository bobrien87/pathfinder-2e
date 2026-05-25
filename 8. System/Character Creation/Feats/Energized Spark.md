---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Exemplar]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The energy of your spirit manifests as crackling lightning, the chill of winter, or the power of an element. Choose one of the following traits: air (slashing), cold, earth (bludgeoning), electricity, fire, metal (slashing), poison, sonic, vitality, void, water (bludgeoning), or wood (piercing). You can choose for any spirit damage dealt by your exemplar abilities to instead gain the trait and deal the corresponding damage type.

**Special** You can select this feat multiple times, choosing a different damage type each time.

**Source:** `= this.source` (`= this.source-type`)
