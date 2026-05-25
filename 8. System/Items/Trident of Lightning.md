---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Electricity]]", "[[Magical]]"]
price: "{'gp': 110}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

This item looks like a normal trident carved with Gozren motifs. If thrown without being activated, it wobbles in the air and fails to strike true.

When you Activate the trident, the carvings crackle with electricity. You then hurl the trident. It shatters immediately after leaving your hand and unleashes its magic as a 4th-rank [[Lightning Bolt]] originating from your space.

The bolt deals 5d12 electricity damage and has a DC 25 [[Reflex]] save.

**Craft Requirements** Supply a casting of *lightning bolt* (4th rank).

**Source:** `= this.source` (`= this.source-type`)
