---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1175}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magic ring seems like simple tarnished brass, but it enhances your curiosity about traps and devices of all kinds.

You can use an Interact action to pull a [[Thieves' Toolkit]] from the ring. This toolkit appears in your hand and any part of it folds back into the ring if they would leave your possession.

They grant you a +2 item bonus to Thievery checks to [[Disable a Device]] and to [[Pick a Lock]], and the ring's insights grant you the same bonus to Crafting checks to [[Craft]] and [[Repair]] snares and traps.

**Activate—Fireball Trap** 10 minutes (manipulate)

**Frequency** once per day

**Effect** You create the effects of a [[Rune Trap]] trap ritual containing [[Fireball]]. You can have only one trapped rune from a *ring of maniacal devices* active at a time, even if you have multiple rings, and the rune disappears if you lose your investiture in the ring.

**Source:** `= this.source` (`= this.source-type`)
