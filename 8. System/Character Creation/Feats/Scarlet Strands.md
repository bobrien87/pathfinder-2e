---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Gnome]]"]
prerequisites: "kijimuna gnome heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The innate magic in your blood turns your signature crimson tresses into more than just a stylish coiffure. If you pluck three strands of your bright red hair and spend 1 minute braiding them together, they magically transform into a strong, 50-foot, crimson rope. This rope can hold 1,000 pounds—great for lashing down sails in a storm, rappelling down a cliff to a hidden treasure, or tying up a Minkaian criminal with a sizable bounty on her head. You can have only one hair rope in existence at a time; if you braid a second, your first rope unravels back into three hairs.

Your hairs can also form a net to catch fish or foes. Once per day, you can cast 4th-rank [[Web]] as an innate primal spell, which takes the form of a crimson fishing net. You must have a hand free to pluck a few strands of your hair that you throw as part of the spell. The hairs regrow when the spell ends.

**Source:** `= this.source` (`= this.source-type`)
