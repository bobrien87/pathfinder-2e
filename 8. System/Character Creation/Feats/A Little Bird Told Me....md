---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Venture Gossip|Venture Gossip]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
prerequisites: "Venture-Gossip Dedication"
source: "Paizo Blog: Foolish Housekeeping and Other Articles"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You transform into a small bird, such as a finch or a sparrow, allowing you to eavesdrop on others and gain information you wouldn't otherwise be able to acquire. You become Tiny, gain the animal trait, and you can't make Strikes. You can Dismiss the effect to return to your normal shape, and you resume your normal shape automatically if you're reduced to 0 Hit Points.

You gain the following statistics and abilities:

AC = 20 + your level. Ignore your armor's check penalty and Speed reduction.

Fly speed 25 feet.

Weakness 5 to physical damage.

Low-light vision and imprecise scent 30 feet.

Acrobatics and Stealth modifiers of +10, unless your own is higher; Athletics modifier –4.

**Source:** `= this.source` (`= this.source-type`)
