---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Modular]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *growth gun* is a *+1 striking hand cannon* made from the regenerative flesh of a hydra, troll, or other similar creature. It has an attached flesh sac that slowly replenishes one shot each round and can be loaded like a normal round of ammunition. It fires regenerating gobbets of flesh, bone, or teeth, determined by the damage type selected for its modular trait. A *growth gun* can be fired underwater, though it's still limited by the selected damage type as normal.

**Activate—Wart Shot** `pf2:2` (manipulate)

**Frequency** once per minute

**Effect** Make a ranged Strike. On a hit, the creature becomes covered in a mass of flesh that continues to grow on the target for a brief time. The creature becomes [[Slowed]] 1 for 1 round, after which the growth withers and falls off.

**Craft Requirements** The initial raw materials must include the flesh of a creature with regeneration.

**Source:** `= this.source` (`= this.source-type`)
