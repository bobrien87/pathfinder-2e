---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Poppet]]"]
prerequisites: "tsukumogami poppet heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can use your body as a deadly weapon. You gain one of the following melee unarmed attacks, which must be one that matches your body (for instance, tsukumogami wrap for a tsukumogami that's a bolt of cotton).

- A blade unarmed attack that deals 1d6 slashing, has the versatile P trait, and is in the sword weapon group.
- A spoke unarmed attack that deals 1d4 piercing, has the agile and finesse traits, and is in the knife weapon group.
- A wrap unarmed attack that deals 1d4 bludgeoning, has the grapple, nonlethal, and trip traits, and is in the flail weapon group.

**Special** You can take this feat only at 1st level, and you can't retrain into or out of this feat.

**Source:** `= this.source` (`= this.source-type`)
