---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
cast: "4 hours"
range: "10 feet"
targets: "1 dead creature of up to 8th level"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth the target's soul and attempt to incarnate it into a brand-new body. As the soul won't be returning to the original body, only a small portion of the creature's remains are required. These remains must have been part of the original body at the time of death, and the target must have died within the past week. If Pharasma has decided that the target's time has come or the target's soul is trapped or doesn't wish to return, this ritual automatically fails, but you discover this after you succeed at the Religion check and can end the ritual without paying the cost.

If the ritual is successful, the target's new body has a random ancestry. Roll `r 1d20`. On a result of 1 through 14, the new body is one of a common ancestry, while on a 15 through 20 they become a member of an uncommon or rare ancestry. The GM chooses possible ancestries based on those found in the region and randomly determines the ancestry. For instance, the GM could roll 1d8 to choose a common ancestry from Player Core. The target replaces their ancestry Hit Points, size, Speeds, attribute boosts and flaws, traits, and special abilities with those of their new ancestry. The target loses their heritage and ancestry feats, selecting replacements from their new ancestry. The target's background, class features, and languages remain unaltered.
- **Critical Success** You reincarnate the target into a new adult body. This new body has full HP and has the same spells prepared as the original did when it died.
- **Success** As critical success, except the new body has 1 HP and no spells prepared. The soul takes some time to adjust to their new body, leaving them [[Clumsy]] 2, [[Drained]] 2, and [[Enfeebled]] 2 for 1 week; these conditions can't be removed or reduced by any means until the week has passed.
- **Failure** You fail to reincarnate the target.
- **Critical Failure** The target's soul becomes trapped in an unintelligent animal creature of the GM's choosing, with a level no greater than half the target's level. While trapped, the target has an Intelligence modifier of –5 and can't use any of their own abilities.

**Heightened (4th)** The maximum level of the target increases to 10. The cost is the target's level (minimum 1) × 40 gp.

**Heightened (5th)** The maximum level of the target increases to 12. The cost is the target's level (minimum 1) × 75 gp.

**Heightened (6th)** The maximum level of the target increases to 14. The cost is the target's level (minimum 1) × 125 gp. The target must have died within the past month.

**Heightened (7th)** The maximum level of the target increases to 16. The cost is the target's level (minimum 1) × 200 gp. The target must have died within the past month.

**Heightened (8th)** The maximum level of the target increases to 18. The cost is the target's level (minimum 1) × 300 gp. The target must have died within the past year.

**Heightened (9th)** The maximum level of the target increases to 20. The cost is the target's level (minimum 1) × 600 gp. The target must have died within the past decade.

**Source:** `= this.source` (`= this.source-type`)
