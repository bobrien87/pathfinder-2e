---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Holy]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 225}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A small, feathered wing is attached to either side of this ornate brass helmet. A visor on the front lowers to cover your face. While wearing the cassisian helmet, you gain a +1 status bonus to AC and saves against unholy creatures and effects.

**Activate** `pf2:2` (concentrate, holy, manipulate)

**Frequency** once per hour

**Effect** Lowering the visor, you send out eye beams that deal your choice of @Damage[2d6[cold]|options:area-damage] or @Damage[2d6[fire]|options:area-damage] damage (DC 20 [[Reflex]] save) to all creatures in a @Template[type:line|distance:15].

**Source:** `= this.source` (`= this.source-type`)
