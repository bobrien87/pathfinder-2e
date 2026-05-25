---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An enemy's Strike would hit you and you weren't already [[Concealed]], [[Hidden]], or [[Undetected]] by that enemy.

Your body flickers momentarily into the Ethereal Plane. You become concealed for 1 round, and the flat check for concealment applies to the Strike that would have hit you. If the flat check fails, the Strike misses you.

**Awakening** When your body flickers, you momentarily assume a terrifying form. If a creature fails the flat check against concealment from your Eerie Flicker, it becomes [[Frightened]] 1, and it doesn't reduce the frightened condition from this effect at the end of the same turn it gained the condition.

**Awakening** You can choose to compress your flickering movement into a single moment, increasing your chance to avoid the triggering attack in exchange for a shorter-lived effect. If you choose to do so, the flat check for concealment against the triggering attack increases to DC 9 flat check, but the concealment affects only the triggering Strike.

**Source:** `= this.source` (`= this.source-type`)
