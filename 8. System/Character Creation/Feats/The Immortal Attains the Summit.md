---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cultivator|Cultivator]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Three Pecks of Dew"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your cultivation bearing glorious fruit, you behold Heaven's will. Returning from your vision of the Holy Mountain, you become an immortal with mystic potency over the terrestrial realms of wind and water.

You cease aging and, regardless of your actual existential state, now register as a living being to effects that can detect living creatures (such as lifesense or spiritsense).

In addition, you learn the [[Control Weather]] and [[Plant Growth]] rituals. You can use Occultism instead of Nature for these rituals. On a success with one of these rituals, you gain the effects of a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
