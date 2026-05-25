---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You tore your eye from the socket and offered it to whatever spirit would take it. In return, you received a glass eye in its place. This eye allows you to see as normal, and when you succeed at a Perception check against an illusion, you get a critical success instead. Once per day, from any distance, the entity that holds your *bargained contract* can overwhelm your cryolite eye with magical energy, causing images to float over your vision that inflict the [[Dazzled]] condition on you for 1 minute.

**Activate—Look Beyond** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You look through the glass eye sealing your *bargained contract*. The contract casts [[See the Unseen]] affecting you.

**Source:** `= this.source` (`= this.source-type`)
