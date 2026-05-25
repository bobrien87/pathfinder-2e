---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sanguimancer|Sanguimancer]]"
source-type: "Remaster"
level: "2"
traits: ["[[Dedication]]"]
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The life essence in your blood recovers naturally over time. You gain a special type of temporary Hit Points called sanguimancy Hit Points that follow the normal rules for temporary Hit Points with two exceptions: you can spend them to power some sanguimancy feats, and you can never have a greater number of sanguimancy Hit Points than double your level.

After a full 8-hour rest, you gain sanguimancy HP equal to your level that last for 8 hours. If someone successfully restores HP to you with [[Treat Wounds]], you also gain 1 sanguimancy HP for every 10 Hit Points recovered (minimum 1 sanguimancy HP).

**Special** Sanguimancer actions have the trait matching your spellcasting tradition; if you don't have one, choose divine or occult when you select the Sanguimancer Dedication.

Sanguimancer

**Source:** `= this.source` (`= this.source-type`)
