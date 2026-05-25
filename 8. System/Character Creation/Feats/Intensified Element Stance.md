---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Druid]]", "[[Ranger]]", "[[Stance]]"]
prerequisites: "trained in Medicine"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin

**Requirements** You were the recipient of elemental medicine (see [[Prepare Elemental Medicine]]) during your last daily preparations.

You expend the elemental medicine in your body to empower your attacks, though you can't consume any more elemental medicine until the next day. While in Intensified Element Stance, your strikes and damaging spells deal an additional 1d6 damage against certain creatures, depending on the type of elemental medicine you expended. If the person who crafted the elemental medicine expended was legendary in the skill they used, increase this damage to 2d6.

- **Earth** acid damage against water creatures
- **Fire** fire damage against metal creatures and constructs that are primarily metallic
- **Metal** electricity damage against wood or plant creatures and constructs primarily made of wood or plant matter
- **Water** sonic damage against fire creatures
- **Wood** cold damage against earth creatures and constructs that are primarily made of rock or earth

**Source:** `= this.source` (`= this.source-type`)
