---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 1300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

A miniature mukradi, its chitin shrunken and pale, is coiled within this jar. Its hollow form grows to a Gargantuan shell when you open the jar. It emits one of three breath weapons, chosen by you. Each creature in the area must attempt a DC 34 basic Reflex save.

- **Acid Maw** (acid) 10-foot-wide, @Template[line|distance:60|width:10] of acid dealing @Damage[12d6[acid]|options:area-damage]. DC 34 [[Reflex]] save
- **Flame Maw** (fire) @Template[cone|distance:60] of fire dealing @Damage[12d6[fire]|options:area-damage]. DC 34 [[Reflex]] save
- **Shock Maw** (electricity) @Template[line|distance:120] of electricity dealing @Damage[12d6[electricity]|options:area-damage]. DC 34 [[Reflex]] save

**Craft Requirements** Supply a mukradi corpse.

**Source:** `= this.source` (`= this.source-type`)
