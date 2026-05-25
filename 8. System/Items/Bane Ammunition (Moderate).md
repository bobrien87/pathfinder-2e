---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Poison]]"]
price: "{'gp': 25}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (manipulate)

Monster hunters favor bane ammunition that contains a capsule of reagents tailored to a particular type of creature—aberration, animal, beast, dragon, fey, giant, ooze, or both fungus and plant. Each type requires a different formula. When activated bane ammunition hits a target that has a trait matching the selected type, it takes 2d6 persistent,poison damage in addition to the damage the attack normally deals.

**Source:** `= this.source` (`= this.source-type`)
