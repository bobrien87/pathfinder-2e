---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Occult]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature Casts a Spell with the mental trait.

**Requirements** You have an unexpended spell slot you could use to Cast a Spell with the mental trait.

When a foe Casts a Spell that has the mental trait and you can see its manifestations, you can use your own mental magic to disrupt it. You expend one of your spell slots to counter the triggering creature's casting of a spell with the mental trait. You lose your spell slot as if you had cast the triggering spell; this spell slot must be one for which you could Cast a Spell with the mental trait. You then attempt to counteract the triggering spell.

**Source:** `= this.source` (`= this.source-type`)
