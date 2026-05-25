---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Earth]]", "[[Splash]]"]
price: "{'gp': 16}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A Strike

This flask holds a pressurized red-brown gas flecked with bits of sublimated crystal. You gain a +1 item bonus to attack rolls. When the bomb explodes, it deals 2d4 piercing damage and @Damage[(4[splash])[piercing]]{4 piercing splash damage} as the mixture suddenly turns into solid crystals flying at high speeds.

On a hit, the target takes 1 persistent,bleed damage from the crystals embedded in its flesh. As long as the bleed damage persists, the target also takes a –5-foot penalty to its speed. The target can spend an Interact action to remove the crystals, reducing the DC to stop the bleeding.

**Source:** `= this.source` (`= this.source-type`)
