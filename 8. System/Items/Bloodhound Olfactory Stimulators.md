---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 136}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These *olfactory stimulators* can be enhanced to better localize scents.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** Your olfactory stimulators twitch as they gather even more information. You gain imprecise scent with a range of 30 feet for 1 minute.

> [!danger] Effect: Bloodhound Olfactory Stimulators

**Source:** `= this.source` (`= this.source-type`)
