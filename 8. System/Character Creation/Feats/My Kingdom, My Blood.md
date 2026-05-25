---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophesied Monarch|Prophesied Monarch]]"
source-type: "Remaster"
level: "16"
traits: ["[[Manipulate]]", "[[Mythic]]"]
prerequisites: "Prophesied Monarch Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The health of the ruler is the health of the kingdom, and the health of the kingdom is that of its ruler, each bound to the other inextricably. Stride. You can Burrow, Climb, Fly, or Swim instead of Striding if you have the corresponding movement type. You then plant your fist or weapon into the ground at your feet, creating a @Template[type:emanation|distance:60] in an aura around you that lasts for 1 minute. Whenever an ally within this aura takes damage, you can use your reaction to take half the damage in their stead while they take the remainder. When you take damage through this link, you don't apply any resistances, weaknesses, or other abilities you have to that damage; you simply take that amount of damage. Whenever you take damage while this effect is active, an ally within the aura can use their reaction to take half the damage for you in the same manner.

The effect ends immediately if you're reduced to 0 Hit Points.

**Source:** `= this.source` (`= this.source-type`)
