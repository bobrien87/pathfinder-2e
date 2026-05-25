---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lineage]]", "[[Talos]]"]
frequency: "once per day"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The elemental metal in your bloodline literally courses through your veins in the form of liquid metals like mercury, rubidium, gallium, and djezet, giving your actions a languid fluidity. You gain the trained proficiency rank in Acrobatics. If you would automatically become trained in Acrobatics (from your background or class, for example), you instead become trained in a skill of your choice. As these metals are largely toxic to organic life, you also gain the Toxic Touch action.

**Toxic Touch** `pf2:1` (poison)

**Frequency** once per day

**Requirements** Your most recent action was to [[Tumble Through]], and you successfully moved through an enemy's space

**Effect** Make a melee unarmed Strike against the enemy whose space you moved through. On a hit, the target takes 1d6 persistent,poison damage and is [[Sickened]] 1 (or takes 2d6 persistent poison and is [[Sickened]] 2 on a critical hit).

**Source:** `= this.source` (`= this.source-type`)
