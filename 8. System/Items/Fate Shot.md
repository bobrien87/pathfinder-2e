---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 50}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (concentrate)

*Fate shot* is made of a nickel-steel alloy carved with the smiling face of a comedic player on one side, while the other side holds the frown of a tragic dramatist. When you hit a target with this ammunition, roll a DC 11 flat check. On a success, treat all the damage dice for your attack as though they rolled the average damage +1, rounded up (for example, a *fate shot* arrow fired from a shortbow would normally deal 1d6, which has an average of 3.5, so you deal 5 damage). This doesn't affect additional damage dice that only happen on a critical hit, such as those added by the deadly trait. On a failure, roll the damage, but your target takes half damage, and you take the remaining amount as mental damage.

**Source:** `= this.source` (`= this.source-type`)
