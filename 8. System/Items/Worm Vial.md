---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 600}"
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

Opening this vial unleashes its destructive contents: a reconstituted Gargantuan cave worm. The worm has two functions; choose which one to use when you Activate the item.

**Burrow** The worm Burrows up to 80 feet, leaving a tunnel behind it. It can burrow through solid stone, but if it does so it burrows 40 feet instead of 80 feet.

**Eat** The worm attempts to swallow a creature, crush it in its insides, then spit the creature out. The target must be within 15 feet, and it attempts a DC 30 [[Reflex]] save. If it fails, it takes @Damage[(3d6+9)[bludgeoning]] (doubled on a critical failure). The worm then spits the creature out to any empty space on the ground within 30 feet, causing the creature to take damage from a 20-foot fall.

**Craft Requirements** Supply the corpse of a cave worm.

**Source:** `= this.source` (`= this.source-type`)
