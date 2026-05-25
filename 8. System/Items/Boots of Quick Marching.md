---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These brown leather shoes have surprisingly thick soles, as though a cobbler had recently repaired them. The tan laces always pull to exactly the right tautness for your feet and ankles to feel supported. You can perform the [[Hustle]] exploration mode activity for twice as many minutes as normal, equal to your Constitution modifier × 20 (minimum 20).

**Activate—Big Step** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The soles on your boots grow even thicker for a moment, proving a bounce to your step. You Step twice.

**Source:** `= this.source` (`= this.source-type`)
