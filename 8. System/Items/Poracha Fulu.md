---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 30}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Folklore from near the Forest of Spirits tells of the origin of the *poracha fulu*. Once, a traveler saved an eight-legged feline who turned out to be a poracha prince. In return, the prince gave the traveler a fulu that later prevented a fast-acting poison from slaying them. Traditionally, one wears a string of up to nine *poracha fulus*, which counts as one talisman. Each time you take persistent damage, one *poracha fulu* affixed to you negates the damage and crumbles to dust. This response is automatic, but you can use a free action (envision) to prevent your fulus from responding. If you do, any *poracha fulus* affixed to you never respond to that persistent damage.

**Source:** `= this.source` (`= this.source-type`)
