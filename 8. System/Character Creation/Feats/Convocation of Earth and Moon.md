---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Concentrate]]", "[[Occult]]", "[[Polymorph]]", "[[Sarangay]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You call upon Mother Earth and Father Moon to fill you with light. A cocoon of moonlight momentarily envelops you, and you emerge in a towering form made of swirling energy, tattooed in stardust and clad in regalia of silver and mother of pearl. When you use this ability, you gain the benefits of both the 4th-rank [[Enlarge]] and [[Fly]] spells. This form lasts for 5 minutes or until you use this action again to return to your normal form.

If you have your head gem, it radiates an aura of moonlight, causing creatures that start their turn adjacent to you to become [[Dazzled]] until the beginning of their turn unless they succeed at a [[Will]] save against your class DC or spell DC, whichever is higher.

**Source:** `= this.source` (`= this.source-type`)
