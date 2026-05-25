---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 450}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The armor allows you to make a controlled descent.

**Activate**`pf2:1` (concentrate)

**Effect** You glide slowly toward the ground, 5 feet down and up to 25 feet forward through the air. Provided you spend at least 1 action gliding on your turn and haven't yet reached the ground, you remain in the air at the end of your turn. Otherwise, you fall.

**Source:** `= this.source` (`= this.source-type`)
