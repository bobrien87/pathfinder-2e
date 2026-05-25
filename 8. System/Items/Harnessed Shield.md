---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Harnessed]]"]
price: "{'gp': 5}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large steel shield features a specialized opening to hold lances and similar weapons. Harnessed shields are a common backup for those who fight with jousting weapons in case they're forced into combat without their mounts. Balancing the weapon within the shield's hold is somewhat awkward, and longer weapons, like lances, need to be held closer to the body than usual for proper support.

**Source:** `= this.source` (`= this.source-type`)
