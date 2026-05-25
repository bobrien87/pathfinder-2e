---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]", "[[Revelation]]"]
price: "{'gp': 325}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *ethersight ring* is a glass band containing a swirling cloud of gray smoke. When you invest the ring, the smoke becomes as transparent as the glass encapsulating it, and you can see clearly into the Ethereal Plane with a range of 60 feet. Whether or not you have invested the ring, you are visible to creatures in the Ethereal Plane within the same range while wearing it. Although you can see these creatures and they can see you, you can affect each other only with abilities that cross between the Ethereal Plane and the Universe.

**Source:** `= this.source` (`= this.source-type`)
