---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "trained in Crafting"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your training focused on Crafting one particular kind of item. Select one of the specialties listed below; you gain a +1 circumstance bonus to Crafting checks to Craft items of that type. If you are a master in Crafting, this bonus increases to +2. If it's unclear whether the specialty applies, the GM decides. Some specialties might apply only partially. For example, if you were making a morningstar and had specialty in woodworking, the GM might give you half your bonus because the item requires both blacksmithing and woodworking.

Specialty
Applicable Items

Alchemy*
Alchemical items such as elixirs

Artistry
Fine art, including jewelry

Blacksmithing
Durable metal goods, including metal armor

Bookmaking
Books and paper

Glassmaking
Glass, including glassware and windows

Leatherworking
Leather goods, including leather armor

Pottery
Ceramic goods

Shipbuilding
Ships and boats

Stonemasonry
Stone goods and structures

Tailoring
Clothing

Weaving
Textiles, baskets, and rugs

Woodworking
Wooden goods and structures

* You must have the [[Alchemical Crafting]] skill feat to Craft alchemical items.

**Source:** `= this.source` (`= this.source-type`)
