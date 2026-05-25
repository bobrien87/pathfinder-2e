---
type: item
source-type: "Remaster"
level: "25"
traits: ["[[Artifact]]", "[[Cursed]]", "[[Primal]]", "[[Sweep]]", "[[Unholy]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Monster Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This potent weapon used by Treerazer is a *+4 greater corrosive major striking obsidian greataxe* that grants a +4 item bonus to attack rolls, deals an extra 2d6 damage to plants, and has the properties of adamantine. It deals an additional die of damage when wielded by Treerazer.

**Activate—Owner's Authority** `pf2:1` (concentrate, scrying)

**Requirements** You aren't wielding Blackaxe and you are its true owner

**Effect** You sense the world around Blackaxe as though you were in its location and can use any of your innate spells through the link as if it were the source of the spell. If another creature is wielding Blackaxe, it must succeed at a DC 50 [[Will]] save or be [[Slowed]] 2 until it relinquishes the weapon.

**Activate—Owner's Reclamation** `pf2:f` (concentrate, teleportation)

**Requirements** You aren't wielding Blackaxe and you are its true owner

**Effect** Blackaxe appears in your hands, teleporting instantly from its prior location.

**Activate—Rejuvenating Deforestation** `pf2:1` (concentrate, death, healing, positive)

**Frequency** once per minute

**Effect** Make a Strike against a living tree with Blackaxe. If it hits, the tree withers to ash and you heal 250 Hit Points and gain the benefit of a 6th-rank [[Restoration]] (6th) and [[Sound Body]] spell.

**Destruction** Chop a powerful magical tree with Blackaxe, and while the sap is still fresh, sever one of Cyth-V'sug's limbs. This makes Blackaxe explode violently.

**Source:** `= this.source` (`= this.source-type`)
