---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 1200}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While dormant, this tattoo appears to be a simple flower bud, but when activated the flower swiftly blossoms, remaining that way until the next time you make your daily preparations. These blooms are colorful, elegant representations of purple iris flowers.

**Activate** `pf2:2` envision

**Frequency** once per day

**Effect** Choose a willing ally you can see within 30 feet. Your ally takes on a regal bearing, exuding the presence of confident royalty. The bloom casts a 5th-rank [[Command]] spell (DC 28) selecting targets within range of the ally. Each target that fails the save must fall [[Prone]] and pays homage to your ally.

**Source:** `= this.source` (`= this.source-type`)
