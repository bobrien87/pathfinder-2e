---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 340}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hand-polished pipe is carved from oak and releases small wisps of smoke even when unlit. As long as you're holding a vaporous pipe, you don't take a circumstance penalty to Perception checks due to thick smoke, and you can't suffocate from smoke and heated air (such as within a wildfire). As long as you are holding the pipe, you also gain resistance to fire equal to half your level.

**Activate** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You draw on the pipe and then blow a massive cloud of smoke that fills a @Template[type:emanation|distance:30] that includes your space. All creatures within the smoke cloud are [[Concealed]] from each other and from creatures outside the smoke, though you can still see clearly within it. The smoke dissipates after 3 rounds, or after 1 round if subjected to a strong wind.

**Source:** `= this.source` (`= this.source-type`)
