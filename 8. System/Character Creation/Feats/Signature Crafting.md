---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "master in Crafting, Magical Crafting"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Magic items you create bear a stamp specific to your handiwork. When you successfully Craft a permanent magic item, roll a DC 9 flat check when the item is fully complete. Any benefit a creature gains from an item quirk applies only while the creature wears the item (for a worn item) or holds it (for a held item). The GM might allow custom quirks similar to those listed.
- **Critical Success** Choose an item quirk from the table and its specifics.
- **Success** The item gains a random item quirk with any specifics selected by the GM.

d10QuirkDescription1CavortingDances in place when not in use.2CleanRemains pristine despite filth.3EnvironmentalAppearance changes to match its environment.4FilthyA layer of filth always remains.5FloatingSlowly descends when dropped.6GlitteringShimmers and glows with light bright as a torch.7InvisibleThe item is invisible, but becomes visible for 1 round after being used.8LoyalFloats within 5 feet of its owner, as if on a tether (but can still be seized by someone else).9Mood colorationUser's mood affects the item's color.10SkillfulThe item grants a +1 item bonus to one type of skill checks.

**Source:** `= this.source` (`= this.source-type`)
