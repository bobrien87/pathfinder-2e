---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Divine]]", "[[Esoterica]]", "[[Manipulate]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

From your collection of religious trinkets, you pull out opposing divine objects-such as the religious symbols of two deities that are hated enemies-and combine them in a display that causes discordant clashes of divine energy that are especially distracting to the faithful. Roll your choice of a [[Deception]] check or [[Intimidation]] check against the Will DC of a creature you can see within 60 feet, with the following results. If the creature is particularly devoted to a deity, such as a cleric, celestial, monitor, fiend, or other creature with divine spells, you gain a +2 circumstance bonus to your skill check. The GM might determine that a creature that despises all deities, such as an alghollthu, is unaffected.
- **Critical Success** The creature is [[Off Guard]] to your attacks until the end of your next turn.
- **Success** The creature is off-guard to your attacks until the end of your current turn.

**Source:** `= this.source` (`= this.source-type`)
