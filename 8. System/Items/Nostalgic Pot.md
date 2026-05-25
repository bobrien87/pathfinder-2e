---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small pot filled with pebbles is imbued with the nostalgia of its owner. While this pot is on your person, you get a +1 item bonus to saves against emotion effects.

**Jingling Memories** `pf2:1` (concentrate, emotion)

**Frequency** once per day

**Effect** You shake the pot, granting a +1 item bonus to an ally to save against an emotion effect.

**Source:** `= this.source` (`= this.source-type`)
