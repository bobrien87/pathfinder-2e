---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Living Vessel|Living Vessel]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whether willingly or not, you've become a vessel for a being of unimaginable power. You and your GM should work together to determine the being's nature and decide how much you know and how much remains a mystery to you for now. Some decisions might influence your options later. You might need to decide whether the entity is a demon, for instance, to know if you qualify for later feats.

You need to spend at least an hour each day assuaging the entity within you or you take a –1 penalty to Will saves for 24 hours. The process of assuaging the entity is determined together between you and the GM. It might be as simple as meditating with the entity to learn more about them, but it might be as extreme as committing gruesome, unspeakable sacrifices to keep their unknowable blessings. After a full week of failing to assuage your entity, you become [[Doomed]] 1, and you can't remove or ameliorate the condition until you allow your entity to take full possession of your body for 24 hours, during which time it pursues its own agenda.

You also gain the [[Entity's Resurgence]] reaction, allowing you to unleash your entity in lieu of falling [[Unconscious]], though at the risk of letting it enact its will.

Living Vessel

**Source:** `= this.source` (`= this.source-type`)
