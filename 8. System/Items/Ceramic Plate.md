---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Adjusted]]", "[[Noisy]]"]
price: "{'gp': 6}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Traditional armor from Senghor, ceramic plate alleviates the need for metallurgy and smithing, instead relying on ceramic firing, glazing, and strong cord work with a backing of leather and thick canvas. Ceramic plate that follows Senghor's style is colorful and artistic, and is built with the armor latches armor adjustment.

**Source:** `= this.source` (`= this.source-type`)
