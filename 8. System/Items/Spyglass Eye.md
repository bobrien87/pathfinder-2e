---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 160}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Polished to a perfect surface and incredibly clear, this special [[Magical Prosthetic Eye]] allows you to clearly see small details as well as things a great distance away.

**Activate** `pf2:2` envision

**Frequency** once per hour

**Effect** A magical lens of hardened air comes into being in front of the eye, allowing you to see as though you were looking through a Fine Spyglass for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
