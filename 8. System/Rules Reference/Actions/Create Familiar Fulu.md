---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day or greater (see [[Fulu Familiar]]);

**Requirements** Your familiar is within 30 feet, and you have one hand free;

**Effect** You make a pinching motion, and your familiar dissolves into magical energy that re-forms between your fingers as a fulu magical item. The fulu must be at least two levels lower than your level, and you don't need to spend the normal monetary cost in magical components or attempt a Crafting check. You can then choose to [[Affix a Talisman]] as part of this activity to affix your familiar fulu. While transformed, your familiar doesn't grant its normal benefits, and it remains transformed until your next daily preparations or until you Activate the fulu, at which point your familiar reappears in an unoccupied space adjacent to you.

**Source:** `= this.source` (`= this.source-type`)
