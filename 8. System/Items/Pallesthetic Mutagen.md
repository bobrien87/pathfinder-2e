---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 150}"
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

You gain unparalleled sensitivity to the tiniest of vibrations through solid surfaces and even the very air around you, but your eyes become useless.

**Benefit** For 1 minute, you gain precise echolocation out to 40 feet, imprecise tremorsense out to 60 feet, and a +2 item bonus to Perception checks using either of these senses.

**Drawback** You are [[Blinded]] for 1 minute.

> [!danger] Effect: Pallesthetic Mutagen

**Source:** `= this.source` (`= this.source-type`)
