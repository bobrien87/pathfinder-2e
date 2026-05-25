---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

You become swifter and nimbler but also fragile.

**Benefit** You gain a +3 item bonus to Acrobatics checks, Stealth checks, Thievery checks, Reflex saves, and Dexterity-based attack rolls, and you gain a +15 foot status bonus to your Speed.

**Drawback** You take damage equal to twice your level; you can't recover Hit Points lost this way by any means while the mutagen lasts. You take a -2 penalty to Fortitude saves.

**Duration** 1 hour.

> [!danger] Effect: Quicksilver Mutagen (Greater)

**Source:** `= this.source` (`= this.source-type`)
