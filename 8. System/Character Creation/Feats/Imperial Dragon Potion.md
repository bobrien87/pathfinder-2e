---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Kobold]]"]
prerequisites: "heavenscribe kobold heritage, expert in Crafting"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

During your daily preparations, you can spend 10 minutes to create a variant *energy breath potion*, which has the kobold trait in addition to its normal traits. The variant potion is influenced by imperial dragon magic, granting it the effect corresponding to your dragon benefactor; the DC for the breath is the higher of your class DC or spell DC. The potion becomes inert if not used by your next daily preparations, so it has no value if sold.

DragonEffect (Save)ForestInsects dealing piercing damage in a @Template[cone|distance:15] ([[Reflex]] save)SeaWater dealing bludgeoning damage in a @Template[line|distance:30] ([[Reflex]] save)SkyLightning dealing electricity damage in a @Template[line|distance:30] ([[Reflex]] save)SovereignA psychic roar dealing mental damage in a @Template[cone|distance:15] ([[Will]] save)UnderworldFlames that deal fire damage in a @Template[cone|distance:15] ([[Reflex]] save)

**Source:** `= this.source` (`= this.source-type`)
