---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Divine]]", "[[Invested]]", "[[Unholy]]"]
price: "{'gp': 50}"
usage: "wornmask"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A patchwork of humanoid flesh makes up a *skinsaw mask*, which is stitched together with black silk or wire. It is distinctive for its bulbous orange eye—crafted from a magical glass bauble—and wide row of teeth. When worn, the mask amplifies your ability to sense fear in other creatures. You know the value of the frightened condition of any observed creature, and you gain a +1 item bonus to Perception checks to [[Seek]] frightened creatures. Whenever you deal precision damage to a frightened creature, you deal 1 additional precision damage. If you aren't unholy, you are [[Drained]] 2 while wearing a *skinsaw mask*.

**Source:** `= this.source` (`= this.source-type`)
