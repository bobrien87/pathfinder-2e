---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Fortune]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 125}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Gaudy and sparkling, these intricately decorated epaulets have clearly never seen a battlefield. Worn by officers with more schooling or connections than actual fighting experience, these epaulets grant you a +1 item bonus to Society and Warfare Lore checks.

**Activate—I Meant to Say** `pf2:r` (concentrate, fortune)

**Frequency** once per day

**Trigger** You critically fail a Diplomacy check

**Effect** The pristine epaulets are often worn to both tense military negotiations and social events and can help you recover from a misstep. You can reroll the check, but you must take the new result.

**Source:** `= this.source` (`= this.source-type`)
