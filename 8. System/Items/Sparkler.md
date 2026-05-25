---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Fire]]"]
price: "{'sp': 4}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Sparklers are common in Tian Xia and Vudra and can be Crafted by those who can specifically Craft fireworks.

**Activate** `pf2:1` (manipulate)

A sparkler gives off colorful sparks, burning for 1 minute. It provides bright light in a 10-foot radius (and dim light for the next 10 feet). While the *sparkler* burns, you can use it as an improvised weapon, dealing 1 fire on a hit. On a critical hit, you cause the target to become [[Dazzled]] for 1 round.

You can touch a *sparkler* to a flammable object as part of the action you spend Activating it or as a separate Interact action while the sparkler is already activated. If you do so, the sparkler can ignite flammable objects the way a [[Matchstick]] does.

> [!danger] Effect: Sparkler

**Source:** `= this.source` (`= this.source-type`)
