---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Brace]]", "[[Deadly d12]]", "[[Reach]]"]
price: "{'gp': 6}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Also known as a zhanmadao, the exceptionally long blade of the nodachi is designed to neutralize enemy mounts and counter the advantages of cavalry units. Its shape and size make it somewhat impractical for close combat but highly effective against charging opponents.

**Source:** `= this.source` (`= this.source-type`)
