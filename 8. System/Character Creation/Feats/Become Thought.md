---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Psychic]]"]
frequency: "once per P1Y"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You shed some of your material form, becoming a being of pure thought. This has the following effects.

- You gain resistance 10 to physical damage but weakness 5 to mental damage.
- You can change your appearance on a whim. This takes a single action, which has the concentrate trait, has the effects of [[Illusory Disguise]], and lasts until you change your appearance again.
- Once per year, when you die, you automatically return to life the next day as long as one living sentient creature on your plane remembers you; the memories enable you to reconstruct yourself from their thoughts. You appear in the vicinity of the creature that remembers you most strongly.

**Source:** `= this.source` (`= this.source-type`)
