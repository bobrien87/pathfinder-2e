---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Reincarnated]]"]
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

It's one thing to remember your previous lives. It's quite another to remember how you died in each of those lives. You can recall dozens, if not more, of excruciating, humiliating, and devastating ends you've suffered over the eons, and you can inflict upon your enemies a vision of these pains. You gain [[Phantasmagoria]] as an occult innate spell that you can cast once per day.

When you gain this feat, choose any two of the following damage types: acid, bludgeoning, cold, electricity, fire, piercing, poison, slashing, or sonic. These damage types caused your deaths more often than not in your previous lives, and whenever a creature takes damage from a *phantasmagoria* spell you cast, you can swap the mental damage that spell normally causes for one of the two damage types you chose.

**Source:** `= this.source` (`= this.source-type`)
