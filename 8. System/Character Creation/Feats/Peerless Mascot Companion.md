---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Commander]]"]
prerequisites: "Battle-Hardened Companion"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As veterans of countless battles, you and your companion share an indomitable strength. The companion you gained with [[Commander's Companion]] is now a specialized animal companion. You can select one of the usual specializations or the peerless mascot specialization. A commander's companion with the peerless mascot specialization gains the following benefits.

- It gains a 30-foot aura that grants the same benefits as your banner, effectively acting as a second banner. If you have your actual banner affixed to your companion, the aura is a single 60-foot aura (this includes the increased aura benefit from Battle-Tested Companion). If you later gain the Glorious Banner feat, your banner has a 100-foot aura while it is affixed to your peerless mascot companion.
- It gains the beast trait.
- Its Intelligence modifier increases by 2 and its Wisdom modifier increases by 1.
- It is an expert in Warfare Lore.
- It can speak one language that you also speak (chosen at the time you gain this feat).
- Its maximum Hit Points increase by 20, increasing to 25 at 18th level, and 30 at 20th level.
- Its mastery of all kinds of battlefields grants it a climb Speed and swim Speed equal to its land Speed; if it already had a Speed that was greater than its land Speed, then it has a climb Speed, swim Speed, and land Speed that are all equal to the highest Speed it has.

**Source:** `= this.source` (`= this.source-type`)
