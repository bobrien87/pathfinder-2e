---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Time Mage|Time Mage]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "You have a spellcasting class feature."
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You might be a novice in the temporal arts now, but in the future, you'll hold time in the palm of your hand. As some of your future knowledge leaks back to your present self, you gain the [[Delay Consequence]] domain spell. You can Refocus by revisiting moments from your past and contemplating futures yet to come. If you already knew *delay consequence* from a feat or ability that allows you to gain your choice of domain spell, such as the [[Domain Initiate]] feat, then when you take Time Mage Dedication, you can retrain that option to select a different domain spell instead as your personal timeline rearranges itself. You also gain [[Time Sense]] as an innate cantrip usable at will. This innate spell and your focus spells from the time mage archetype are of the same tradition as the spells you used to meet the archetype's prerequisites.

Time Mage

**Source:** `= this.source` (`= this.source-type`)
