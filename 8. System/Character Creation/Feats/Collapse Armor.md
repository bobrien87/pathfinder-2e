---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Inventor]]", "[[Manipulate]]", "[[Modification]]"]
prerequisites: "armor innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wearing your armor innovation, or holding it in both hands in its compact form (see text).

You've modified your armor innovation to collapse into a more compact form so you can don or remove it in an instant. If you're wearing your innovation when you Collapse your Armor, you remove it instantly, and it compresses into its compact form, after which it latches onto your body, typically by attaching to a belt, bandolier, or other convenient carrying surface as a nondescript satchel. If your armor is stowed and carried on your person in its compact form when you take this action, it unfolds back into its armor form onto your body. In compact form, your armor innovation is easier to carry, with a Bulk 1 lower than the Bulk listed for it, to a minimum of light Bulk (carried armor normally has a Bulk 1 higher than listed in the armor entry).

**Source:** `= this.source` (`= this.source-type`)
