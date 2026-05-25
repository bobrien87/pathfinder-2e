---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Lozenge]]"]
price: "{'gp': 80}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Made from a special mixture of honey and alchemical reagents, poison fizz is a zesty, sweet rock candy that pops and crackles in your mouth. For 1 hour, you have a +2 item bonus to saving throws against poison and being petrified.

**Secondary Effect** `pf2:2` (poison)

**Effect** You bite the poison fizz to release its poisonous liquid center and spray green mist in a @Template[cone|distance:15]. This deals @Damage[3d6[poison]|options:area-damage] with a DC 24 [[Reflex]] save. A creature that critically fails is also [[Blinded]] until the end of your next turn and is then temporarily immune to being blinded by poison fizz for 1 hour.

> [!danger] Effect: Poison Fizz

**Source:** `= this.source` (`= this.source-type`)
