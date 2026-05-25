---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Arcane]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have claimed an area or location as your demesne, granting you the ability to ward and protect it. When you select this feat, choose a demesne, an area of no more than 2,000 square feet. You must legitimately own the area or, if its a public area, you must lay claim to the area without anyone contesting it.

Once you've chosen your demesne, it's automatically protected by an arcane [[Peaceful Bubble]] spell with an unlimited duration, heightened to half your level rounded up and using your thaumaturge class DC in place of a spell DC, if necessary. Additionally, the demesne is attended by three unseen custodians, as a successful [[Unseen Custodians]] ritual, and one object in the area gains an elemental sentinel, as a successful [[Elemental Sentinel]] ritual.

**Source:** `= this.source` (`= this.source-type`)
