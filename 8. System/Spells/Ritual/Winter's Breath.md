---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
cast: "1 hour"
range: "40 feet"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The cold and dour months of winter are an excellent time to gather with friends and family to enjoy a pot of hot tea. The so-called "breath" in this ritual refers to the steam that wafts up from a freshly brewed cup while held in the hands and inhaled. Despite the ritual's name, it can be cast during any season, but unless it's cast during winter, the DCs for successfully casting *winter's breath* increase by 2 (or by 4 if the ritual is cast during summer).

When you cast this ritual, you call forth a magical pavilion consisting of a colorful tent or decorate an area within range with a large number of colorful banners. In either case, the ritual also creates a full supply of teas and tea ware for the casters to use and serve up to six guests (which can include the casters). During the ritual, all the guests must be polite and well-mannered. The tea created by *winter's breath* is always delicious, but the effects of the tea and taking part in the ceremony of its serving depend on the success of the magic. At the ceremony's end, the ritual is completed, and you and the secondary caster attempt your checks as normal. If the ceremony is interrupted at any point, the tea vanishes and the ritual is disrupted.
- **Critical Success** The ceremony is a true delight. The tea casts [[Clear Mind]], [[Environmental Endurance]], [[Sound Body]], and [[Sure Footing]] at a rank equal to that which *winter's breath* was cast on each guest. Each guest also gains 10 temporary Hit Points and a +1 status bonus to saves against emotion effects for the next 12 hours.
- **Success** As critical success, except guests must choose which one of the five spells are cast on them, and they don't gain the status bonus to saves.
- **Failure** The tea leaves a bitter, unpleasant taste in the mouth, and no benefits are granted.
- **Critical Failure** Rather than invigorate and delight, the tea is disappointing and depressing. You and your guests are [[Sickened]] 3 and can't reduce the condition for 12 hours.

**Heightened (+1)** The spells associated with a success or critical success are heightened by 1 rank, and the temporary Hit Points granted are increased by 2.

**Source:** `= this.source` (`= this.source-type`)
