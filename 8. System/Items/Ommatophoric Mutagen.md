---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 65}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

Your eyes bulge from their sockets and extend upwards from your head on long, prehensile stalks, greatly enhancing your eyesight and field of view but leaving you unable to close your eyes, increasing your vulnerability to harmful visual effects.

**Benefit** You gain all-around vision, a +2 item bonus to visual Perception checks, and low-light vision if you don't already have it. These effects last for 1 minute.

**Drawback** For 1 minute, you take a –2 penalty to saving throws against effects that have the visual trait.

> [!danger] Effect: Ommatophoric Mutagen

**Source:** `= this.source` (`= this.source-type`)
