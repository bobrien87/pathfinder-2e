---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 25}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While dormant, this tattoo appears to be a simple flower bud, but when activated the flower swiftly blossoms, remaining that way until the next time you make your daily preparations. These blooms are colorful, elegant representations of lilac flowers.

**Activate** `pf2:2` envision

**Frequency** once per day

**Effect** Choose a willing ally you can see within 30 feet. Memories bubble to the surface of your ally's mind. The ally attempts to Recall Knowledge with a +2 status bonus to the check from these vibrant memories.

**Source:** `= this.source` (`= this.source-type`)
