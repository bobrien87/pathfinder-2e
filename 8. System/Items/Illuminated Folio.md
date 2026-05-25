---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 4200}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The pages of this part-spellbook, part-bestiary are illustrated with all manner of creatures, magical and mundane. The illustrations shift and move around the page when examined.

**Activate** `pf2:1` (concentrate, spellshape)

**Effect** If your next action is to cast a summon spell prepared from this grimoire, you summon creatures from the illuminated folio rather than their usual source. These summoned creatures appear as living illustrations, granting them resistance to physical damage equal to half their level and weakness 5 to fire and to any ability with the water trait. They can also fold themselves up to pass through spaces only an inch or so wide as part of their movement.

> [!danger] Effect: Illuminated Folio

**Source:** `= this.source` (`= this.source-type`)
